'''
Author: LOTEAT
Date: 2024-07-31 15:21:49
'''
import numpy as np


class OdometryMotion:
    def __init__(self, pose=np.zeros(3)):
        self.pose = pose

    def update(self, u):
        # odemetry motion model update
        self.pose[0] += u['t'] * (np.cos(self.pose[2] + u['r1']))
        self.pose[1] += u['t'] * (np.sin(self.pose[2] + u['r1']))
        self.pose[2] = self.pose[2] + u['r1'] + u['r2']

    def get_pose(self):
        return self.pose.copy()
