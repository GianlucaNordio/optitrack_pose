#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Pose
from motion_capture_tracking_interfaces.msg import NamedPoseArray, NamedPose
from rclpy.qos import QoSProfile, QoSReliabilityPolicy

class DronePoseFilter(Node):
    def __init__(self):
        super().__init__('pose_filter')


        qos_profile = QoSProfile(
            reliability=QoSReliabilityPolicy.RMW_QOS_POLICY_RELIABILITY_BEST_EFFORT,
            depth=10
        )

        self.pose_publisher = self.create_publisher(Pose, '/your_drone_name_such_as_cf1/position', 10)
        self.pose_subscriber = self.create_subscription(
            NamedPoseArray,
            '/poses',
            self.poses_callback,
            qos_profile
        )

    def poses_callback(self, data):
        for named_pose in data.poses:
            if named_pose.name == 'your_drone_name_such_as_cf1':
                pose = named_pose.pose
                self.get_logger().info(f"Pos: {pose}") 
                self.pose_publisher.publish(pose)
                break

def main(args=None):
    rclpy.init(args=args)
    filter_node = DronePoseFilter()
    rclpy.spin(filter_node)
    filter_node.destroy_node()

if __name__ == '__main__':
    main()