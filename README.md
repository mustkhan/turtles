# ROB521 - Mobile Robotics and Perception
**By:** Mustafa Khan, Joshua Zimmerman, Gurpreet Mukker

## Setup
To complete the ROB521 labs, you need an **Ubuntu 20.04** environment capable of running **ROS Noetic** and **Gazebo**. Follow these steps to set up your environment:

### **1. Build the Docker Image**
Navigate to the `docker/` folder and build the Docker image:
```bash
cd docker/
mkdir user_files
docker build -t vnc_image .
```

### **2. Run the Docker Container**
Once the image is built, mount the `user_files` folder and run the container:
```bash
docker run -it --name ros_vnc -v ./user_files:/home/ubuntu/ -p 6080:80 --shm-size=512m vnc_image
```
**Note:** Once you have run this, go to your browser and enter `http://127.0.0.1:6080/`. You will be able to access an Ubuntu 20.04 desktop.

### **3. Source ROS Noetic**
Once inside the Docker container, source ROS Noetic:
```bash
source /opt/ros/noetic/setup.bash
```
If there are no errors, add this command to your `.bashrc` file:
```bash
echo 'source /opt/ros/noetic/setup.bash' >> ~/.bashrc
```

### **4. Install TurtleBot3 ROS Packages**
#### **Install Required ROS Packages**
Before you proceed, run:
```bash
sudo apt-get update
sudo apt-get upgrade
```
Then, run:
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

#### **Install TurtleBot3 Packages**
```bash
sudo apt install ros-noetic-dynamixel-sdk
sudo apt install ros-noetic-turtlebot3-msgs
sudo apt install ros-noetic-turtlebot3
```

#### **Install TurtleBot3 Gazebo Simulation Package**
Clone the TurtleBot3 simulation repository and build it in your catkin workspace:
```bash
mkdir ~/catkin_ws
mkdir ~/catkin_ws/src
cd ~/catkin_ws/src/
git clone -b noetic-devel https://github.com/ROBOTIS-GIT/turtlebot3_simulations.git
cd ~/catkin_ws && catkin_make
```

#### **Source the Catkin Workspace**
```bash
source devel/setup.bash
```

### **5. Configure the TurtleBot3 Model**
Set the TurtleBot3 model environment variable as one of the following:
```bash
echo 'export TURTLEBOT3_MODEL=waffle' >> ~/.bashrc # Use this if running in simulation
echo 'export TURTLEBOT3_MODEL=waffle_pi' >> ~/.bashrc # Use this if running on real robot
```
Note: As a sanity check you can run:
```bash
cd ~/catkin_ws
catkin_make # builds files
source devel/setup.bash # source files
roslaunch turtlebot3_gazebo turtlebot3_world.launch # launch gazebo
```
In another terminal, run:
```bash
roslaunch turtlebot3_teleop turtlebot3_teleop_key.launch