'''
Author: LOTEAT
Date: 2024-07-31 15:08:18
'''
from utils import read_sensor_data, read_world
from motion import OdometryMotion
from plot import plot_motion

data = read_sensor_data('data/sensor_data.txt')
landmarks = read_world('data/world.txt')
robot = OdometryMotion()
trajectory = [dict(sensor=[], pose=robot.get_pose())]

for snapshot in data:
    odometry = snapshot['odometry']
    sensor = snapshot['sensor']
    robot.update(odometry)
    trajectory.append(dict(sensor=sensor, pose=robot.get_pose()))

plot_motion(trajectory, landmarks)

