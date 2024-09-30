## synetix WRO Future Engineers team

This repository provides information and knowledge regarding the ongoing progress, evolution, and development of our self-driving robot vehicle, which was created and coded by us, Mohammed bin Fahd and Rawad Alghanim, as participants in the Future Engineers 2024 division of the World Robot Olympiad (WRO).


## Engineering materials

This repository contains engineering materials of a self-driven vehicle's model participating in the WRO Future Engineers competition in the season 2024.

## Content

- `t-photos`: Contains 2 photos of the team, including an official one and a funny photo with all team members.
- `v-photos`: Contains 6 photos of the vehicle, showcasing it from every side as well as from the top and bottom.
- `schemes`: Contains one or several schematic diagrams (JPEG, PNG, or PDF) illustrating all electromechanical components used in the vehicle, including electronic components and motors, and how they connect to each other.
- `src`: Contains the control software code for all components programmed to participate in the competition.
- `other` (optional): Contains additional files that can help understand how to prepare the vehicle for the competition, such as documentation on connecting to a SBC/SBM, uploading files, datasets, hardware specifications, and communication protocols descriptions. If not needed, this directory can be removed.

## Introduction
Autonomous Driving System: The Convergence of Artificial Intelligence and Precision Engineering

In this meticulously designed project, the Raspberry Pi is employed as an advanced brain that manages the robot's main operations, while the Arduino Mega functions as a controller that interacts with sensors to ensure immediate precision in responding to the surrounding environment.

1. Sensors as the Robot's Eyes
Ultrasonic Sensors: These sensors play a key role in providing a three-dimensional sense of the environment. By utilizing ultrasonic wave reflection technology, the robot can calculate distances with remarkable accuracy, allowing it to precisely and swiftly detect obstacles, enabling it to make critical decisions in real-time.
Color Sensor: This sensor distinguishes colors on the path, helping the robot identify specific routes or perform tasks related to colors, such as changing direction based on colored signals on the road.
2. The Camera as an Advanced Eye: OpenCV and Image Processing
Using the Raspberry Pi camera, the robot becomes capable of "seeing" and analyzing the world in a way similar to humans. The camera captures live images of the track or surrounding environment, which are immediately processed using OpenCV. Through image processing, the robot can recognize shapes, obstacles, and targets in its surroundings, enhancing its real-time decision-making.

OpenCV allows the robot to recognize objects and quickly detect changes in the environment. For instance, the robot can identify the correct paths and adapt to changes in signals or moving obstacles.

3. Coordination Between Arduino and Raspberry Pi
The Arduino Mega acts as a low-level sensor system that handles real-time communication with the ultrasonic and color sensors. Every sensor reading is passed to the Raspberry Pi, which analyzes the data and makes decisions based on advanced AI algorithms.

The Raspberry Pi receives data from the Arduino and combines it with what it "sees" through the camera. This data is analyzed in real-time, enabling the robot to make critical decisions, such as avoiding obstacles or identifying pathways.

4. Autonomous Driving Algorithms
Once the data from the sensors and camera is processed, the Raspberry Pi activates autonomous driving algorithms. These algorithms allow the robot to make decisions such as changing directions or adjusting speed based on immediate conditions.

For example, if the sensors detect a nearby obstacle, the robot slows down or changes its course using data from the camera to determine the next safe direction. This type of intelligent interaction mimics the autonomous driving found in advanced vehicles.

The Perfect Integration: Smooth and Safe Driving
Through the seamless coordination between sensors, the camera, and the Raspberry Pi, the robot becomes capable of making smart and instantaneous decisions. Autonomous driving does not rely solely on sensors; it combines vision and data processing, allowing the robot to navigate smoothly and precisely in complex environments.

This system represents a remarkable fusion of mechanical engineering, advanced electronics, and AI algorithms, enabling the robot to autonomously navigate in a way that closely resembles human driving.


