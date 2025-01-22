# ROB521 - Mobile Robotics and Perception
By: Mustafa Khan, Joshua Zimmerman, Gurpreet Mukker

# Setup
In order to complete the ROB521 labs, we need to have an Ubuntu 20.04 environment that can run ROS Noetic and Gazebo. To setup your environment:
1. Navigate to the docker folder and build the docker image:
```bash
cd docker/
mkdir user_files
docker build -t vnc_image .
```
2. Once the image is built you can mount the `user_files`` folder and build a container by running:
```bash
docker run -it --name ros_vnc -v ./user_files:/home/ubuntu/ -p 6080:80 --shm-size=512m vnc_image
```
3. Once you are inside the docker container, source ROS Noetic:
```bash
source /opt/ros/noetic/setup.bash
```
If there are no errors, add the source command to your `.bashrc` file by running:
```bash
echo 'source /opt/ros/noetic/setup.bash' >> ~/.bashrc
```
4. Finally, install TurtleBot3 ROS packages.

Install Dependent ROS Packages for TurtleBot:
```bash
sudo apt-get install ros-noetic-joy ros-noetic-teleop-twist-joy \
ros-noetic-teleop-twist-keyboard ros-noetic-laser-proc \
ros-noetic-rgbd-launch ros-noetic-rosserial-arduino \
ros-noetic-rosserial-python ros-noetic-rosserial-client \
ros-noetic-rosserial-msgs ros-noetic-amcl ros-noetic-map-server \
ros-noetic-move-base ros-noetic-urdf ros-noetic-xacro \
ros-noetic-compressed-image-transport ros-noetic-rqt* \
ros-noetic-rviz ros-noetic-gmapping \
ros-noetic-navigation ros-noetic-interactive-markers
```
Install TurtleBot3 Packages:
```bash
sudo apt install ros-noetic-dynamixel-sdk
sudo apt install ros-noetic-turtlebot3-msgs
sudo apt install ros-noetic-turtlebot3
```
Install TurtleBot3 Gazebo Simulation Package under your catkin workspace:
```bash
cd ~/catkin_ws/src/
git clone -b noetic-devel https://github.com/ROBOTIS-GIT/turtlebot3_simulations.git
cd ~/catkin_ws && catkin_make
```
Additionally, source the setup bash from your catkin workspace:
```bash
source devel/setup.bash
```
Finally, setup the environment variable to identify the TurtleBot 3 model
we are using.
```bash
echo 'export TURTLEBOT3_MODEL=waffle_pi' >> ~/.bashrc
```
