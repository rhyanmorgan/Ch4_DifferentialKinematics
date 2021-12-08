# Ch4_DifferentialKinematics
## Problem Statement
Approximate the differential kinematics of the Niryo_One robotic manipulator in a specific orientation using the geometric Jacobian. Create a simulation of the Niryo_One manipulator with the same input target angular velocities of its revolute links. Use Python to get the differential kinematics of the end effector and compare them to the approximation made previously. 
## Pre-Requisites
- Software: Coppeliasim (for simulating the pre-made Niryo_One robotic manipulator), Spyder (for Python coding)
- Mathematica/MATLAB recommended (for calculating the geometric Jacobian)
- Basic coding capabilities
- Package commands in Python: https://www.coppeliarobotics.com/helpFiles/en/remoteApiFunctionsPython.htm
## Solution to Approximation

![image](https://user-images.githubusercontent.com/95330513/145285885-e8007800-17c9-4e74-ae6c-3a723d8de2ab.png)

Shown above is a simplified representation of the Niryo_One manipulator where only the world frame (frame 0), the end-effector frame (frame 7), and the frames of joints 2, 3, and 4 from Coppeliasim are shown. These joints were chosen to simplify the example and calcuations, so that the results could be easily compared and simpler to troubleshoot. Note that all joints in the simulation and in the model are revolute joints. Therefore, the geometric Jacobian entry for each joint is found as follows:

  ![image169](https://user-images.githubusercontent.com/95330513/145286636-e9938530-f0c1-4f3f-ae65-17d74f402aa5.png)      
  
  ![image157](https://user-images.githubusercontent.com/95330513/145286529-5d3e6ec4-e7fe-4384-b53d-754552eca6a9.png)

While the orientation of the manipulator joints is approximated using the diagram above, the position of each joint with respect to the world frame (![image](https://user-images.githubusercontent.com/95330513/145287126-0ee31e31-d637-47d0-8e4e-658379b1202b.png)
) is found using the simulation. The ouput of these positions have the handles "Joint_Position_#" respectively in the Python coding. The position of the end-effector with respect to the world frame is also needed and its handle in the Python code is "EndEffector_Position"

These positions are needed directly from the code because the orientation of the world frame in Coppeliasim may not be aligned with the world frame of the robotic manipulator. Also, the output of the velocities found using the simulation will be with respect to the world frame of Coppeliasim. The following position vectors represent each of the positions:

![image](https://user-images.githubusercontent.com/95330513/145290590-1a74bcb3-f9e9-4102-948c-6497526ec635.png)

Once the positions are known, ![image](https://user-images.githubusercontent.com/95330513/145290458-a6199ff8-583d-40b3-8322-887f1e01b605.png)
can be calculated by simply subtracting the corresponding joint positions from the end effector's position. This gives the following results:

![image](https://user-images.githubusercontent.com/95330513/145290655-6f98bbec-5c75-45fe-a710-c824b8ed4d13.png)

Next, we can use the diagram to get an opproximation of the final orientation of the manipulator. Alternatively, one could use the Python code to get the orienations as well, doing so will lead to even more accurate results. Finding the orientation of each joint with respect to the world frame is fairly simple from the diagram as all of the links are either in line with each other or in a perpendicular orientation. For finding the geometric Jacobian of this simple model, we only need the z-orientation of each joint with respect to the world frame. In this diagram, those vecotors represent the orienation of the current z-axes with respect to the world frame

- For joint #2, the current z-axis is aligned with the world frame's positive x-axis, therefore: ![image](https://user-images.githubusercontent.com/95330513/145291633-c9b58426-837b-4fe6-a41b-07b1f223d9a0.png)

- For joint #3, the current z-axis is aligned with the world frame's positive x-axis, therefore: ![image](https://user-images.githubusercontent.com/95330513/145291737-1d67426e-27ca-484b-892c-4873a094ef04.png)

- For joint #4, the current z-axis is aligned with the world frame's positive y-axis, therefore: ![image](https://user-images.githubusercontent.com/95330513/145291822-3bce1a13-fc1d-4780-86ea-edf521739311.png)

Note that these values are equivalent to the bottom 3 values of each column of the final geometric Jacobian matrix. Therefore, the last step to finding the inputs of the rest of the Jacobian is to take the cross product: ![image169](https://user-images.githubusercontent.com/95330513/145292103-231dfd74-501b-40c4-a63a-9bfd1d5d907b.png) The results are as follows:

![image](https://user-images.githubusercontent.com/95330513/145292836-e4853b69-0ec4-4620-8b9b-8db0e71f051f.png)

Finally, we can combine all of the values to get the final geometric Jacobian:

![image](https://user-images.githubusercontent.com/95330513/145293575-ea59948a-deef-4cd3-b517-d2abf4e598c3.png)




