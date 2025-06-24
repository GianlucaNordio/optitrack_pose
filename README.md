# optitrack_pose
This package allows to get the position of the drone to a custom topic that you want to use. 

To set it up:
```
cd ~/crazyflie_ws/src
git clone https://github.com/GianlucaNordio/optitrack_pose.git
```

then add your drone information:
```
cd ~/crazyflie_ws/src/optitrack_pose/optitrack_pose/
gedit node.py
```

To build it run the following commonds:
```
cd ~/crazyflie_ws/
colcon build
source install/setup.bash
```
To run it use:
```
ros2 run optitrack_pose node
```

Feel free to report any issue to group 6.
