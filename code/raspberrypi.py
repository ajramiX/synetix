import cv2
import numpy as np
import serial
from picamera2 import Picamera2
import time

cv2.startWindowThread()
picam2 = Picamera2()
picam2.configure(picam2.create_preview_configuration(main={"format": 'XRGB8888', "size": (1280, 720)}))
picam2.start()

ser = serial.Serial('/dev/ttyUSB0', 9600)

color_ranges = {
    'Red': [(0, 120, 70), (10, 255, 255)],
    'Green': [(36, 100, 100), (86, 255, 255)],
    'Pink': [(140, 50, 50), (180, 255, 255)]
}

cv2.namedWindow("Camera", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Camera", 1280, 720)

pink_count = 0
last_pink_time = time.time()

while True:
    frame = picam2.capture_array()
    blurred_frame = cv2.GaussianBlur(frame, (15, 15), 0)
    height, width, _ = blurred_frame.shape
    left_bound = width // 3
    right_bound = 2 * (width // 3)

    hsv_frame = cv2.cvtColor(blurred_frame, cv2.COLOR_BGR2HSV)
    result = None

    for color_name, (lower_range, upper_range) in color_ranges.items():
        lower = np.array(lower_range, np.uint8)
        upper = np.array(upper_range, np.uint8)

        mask = cv2.inRange(hsv_frame, lower, upper)
        mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, np.ones((5, 5), np.uint8))
        mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, np.ones((5, 5), np.uint8))

        contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        object_centers = []

        for contour in contours:
            area = cv2.contourArea(contour)
            if area > 1000:
                x, y, w, h = cv2.boundingRect(contour)
                object_center_x = x + w // 2
                object_centers.append(object_center_x)

                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                cv2.putText(frame, color_name, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

        if object_centers:
            avg_center = sum(object_centers) // len(object_centers)

            if avg_center < left_bound:
                if color_name == 'Green':
                    result = 3
                elif color_name == 'Red':
                    result = 5
            elif avg_center > right_bound:
                if color_name == 'Green':
                    result = 1
                elif color_name == 'Red':
                    result = 4
                elif color_name == 'Pink':
                    pink_count += 1
                    last_pink_time = time.time()
            else:
                if color_name == 'Green':
                    result = 2
                elif color_name == 'Red':
                    result = 6

            if pink_count >= 3:
                if time.time() - last_pink_time > 30:
                    result = 9
                    print("9 Arduino.")

    if result is not None:
        ser.write(str(result).encode())
        print(f"Sent to Arduino: {result}")

    cv2.imshow("Camera", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
ser.close()