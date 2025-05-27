#!/usr/bin/env python3
import copy
import rospy
import moveit_commander
import geometry_msgs.msg
import numpy as np
import sys
import tf2_ros
import tf2_geometry_msgs
import tf.transformations as tf_trans
import math

class DemoRobot:
    def __init__(self, nodename, groupname, reference_frame, eef_link):
        rospy.init_node(nodename, anonymous=False)
        moveit_commander.roscpp_initialize(sys.argv)

        self.robot = moveit_commander.RobotCommander()
        self.move_group = moveit_commander.MoveGroupCommander(groupname)
        self.reference_frame = reference_frame
        self.eef_link = eef_link

        self.move_group.set_pose_reference_frame(reference_frame)  # Targets müssen in base_link angegeben werden!
        self.move_group.set_end_effector_link(self.eef_link)  # WICHTIG: Explizit EEF setzen
        self.move_group.set_max_acceleration_scaling_factor(1.0)
        self.move_group.set_max_velocity_scaling_factor(1.0)
        self.move_group.set_goal_tolerance(0.001)
        self.move_group.set_planning_time(10.0)

        #self.tf_buffer = tf2_ros.Buffer()
        #self.tf_listener = tf2_ros.TransformListener(self.tf_buffer)
        self.goals = []

    def getPoseAndPrint(self):
        cp = self.move_group.get_current_pose(self.eef_link).pose
        print(f"Current Pose of {self.eef_link} in base_link:")
        print(f"x: {cp.position.x:.3f}, y: {cp.position.y:.3f}, z: {cp.position.z:.3f}")
        print(f"qx: {cp.orientation.x:.3f}, qy: {cp.orientation.y:.3f}, qz: {cp.orientation.z:.3f}, qw: {cp.orientation.w:.3f}")

    def getPoseInFrame(self, target_frame):
        cp = self.move_group.get_current_pose(self.eef_link).pose
        stamped_pose = geometry_msgs.msg.PoseStamped()
        stamped_pose.header.frame_id = self.move_group.get_pose_reference_frame()
        stamped_pose.header.stamp = rospy.Time.now()
        stamped_pose.pose = cp
        #try:
        #    #trans_pose = self.tf_buffer.transform(stamped_pose, target_frame, rospy.Duration(1.0))
        #    #print(f"Pose von {self.eef_link} relativ zu {target_frame}:")
        #    #print(f"x: {trans_pose.pose.position.x:.3f}, y: {trans_pose.pose.position.y:.3f}, z: {trans_pose.pose.position.z:.3f}")
        #    #print(f"qx: {trans_pose.pose.orientation.x:.3f}, qy: {trans_pose.pose.orientation.y:.3f}, qz: {trans_pose.pose.orientation.z:.3f}, qw: {trans_pose.pose.orientation.w:.3f}")
        #    #return trans_pose.pose
        #except Exception as e:
        #    rospy.logerr(f"Transformation in Frame {target_frame} fehlgeschlagen: {e}")
        #    return None

    def setTargetRelativeToReference(self, x, y, z, roll, pitch, yaw):
        """
        Setzt ein Ziel für den Endeffektor, das relativ zum reference_frame (z.B. rim_link_1) definiert ist.
        """
        try:
            # Zielpose im reference_frame definieren
            pose_in_ref = geometry_msgs.msg.PoseStamped()
            pose_in_ref.header.frame_id = self.reference_frame
            pose_in_ref.header.stamp = rospy.Time.now()
            pose_in_ref.pose.position.x = x
            pose_in_ref.pose.position.y = y
            pose_in_ref.pose.position.z = z
            quat = tf_trans.quaternion_from_euler(roll, pitch, yaw)
            pose_in_ref.pose.orientation.x = quat[0]
            pose_in_ref.pose.orientation.y = quat[1]
            pose_in_ref.pose.orientation.z = quat[2]
            pose_in_ref.pose.orientation.w = quat[3]

            # In base_link transformieren (MoveIt benötigt das Ziel IMMER in base_link!)
            #pose_in_base = self.tf_buffer.transform(pose_in_ref, "base_link", rospy.Duration(3.0))

            #print("[DEBUG] Zielpose in rim_link_1:")
            #print(f"  x: {x:.3f}, y: {y:.3f}, z: {z:.3f}")
            #print(f"  roll: {roll:.3f}, pitch: {pitch:.3f}, yaw: {yaw:.3f}")
            #print("[DEBUG] Zielpose in base_link (wird an MoveIt übergeben):")
            #print(f"  x: {pose_in_base.pose.position.x:.3f}, y: {pose_in_base.pose.position.y:.3f}, z: {pose_in_base.pose.position.z:.3f}")
            #print(f"  qx: {pose_in_base.pose.orientation.x:.3f}, qy: {pose_in_base.pose.orientation.y:.3f}, qz: {pose_in_base.pose.orientation.z:.3f}, qw: {pose_in_base.pose.orientation.w:.3f}")

            self.goals.append(copy.deepcopy(pose_in_base.pose))
        #except Exception as e:
        #    rospy.logerr(f"Target Transform Error: {e}")

    def move(self):
        self.move_group.clear_pose_targets()
        try:
            for g in self.goals:
                print("[DEBUG] Sende Ziel an MoveIt!")
                self.move_group.set_pose_target(g, self.eef_link)
                result = self.move_group.go(wait=True)
                print(f"[DEBUG] MoveIt! Rückgabe: {result}")
                if not result:
                    rospy.logerr("Kein gültiger Plan für das Ziel!")
        except Exception as e:
            rospy.logerr(f"Planungs-/Ausführungsfehler: {e}")
        finally:
            self.move_group.stop()
            self.move_group.clear_pose_targets()
            self.goals = []

if __name__ == "__main__":
    groupname_1 = "igus_robot_arm"
    reference_frame_1 = "rim_link_1"
    eef_link_1 = "igus_tcp_link"  # Passe ggf. an deinen Endeffektor an!

    r = DemoRobot(nodename="demo_robot", groupname=groupname_1, reference_frame=reference_frame_1, eef_link=eef_link_1)
    igus_orientation = [math.pi / 2, -math.pi / 2.0, 0.0]

    # Zielpose RELATIV zu rim_link_1 angeben:
    r.setTargetRelativeToReference(0, 0,0, *igus_orientation)  # Beispiel: 10 cm Z nach oben in rim_link_1

    print("Aktuelle Roboterpose vor Bewegung:")
    #r.getPoseInFrame("rim_link_1")

    r.move()

    print("Aktuelle Roboterpose nach Bewegung:")
    #r.getPoseInFrame("rim_link_1")

    del r
