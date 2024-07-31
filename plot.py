'''
Author: LOTEAT
Date: 2024-07-31 15:47:31
'''

import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.animation import PillowWriter
import threading


def plot_motion(trajectory, landmarks):
    fig, ax = plt.subplots()
    ax.set_xlim(-2, 12)
    ax.set_ylim(-2, 12)
    landmarks_x = []
    landmarks_y = []
    for landmark_coord in landmarks.values():
        landmarks_x.append(landmark_coord[0])
        landmarks_y.append(landmark_coord[1])
    ax.scatter(landmarks_x, landmarks_y, c='red', label='Landmarks')

    robot, = ax.plot([], [], 'bo', label='Robot')
    connections, = ax.plot([], [], 'k-')

    def init():
        robot.set_data([], [])
        connections.set_data([], [])
        return [robot, connections]

    def update(frame):
        pose = frame['pose']
        sensors = frame['sensor']
        robot.set_data(pose[0], pose[1])
        x_data = []
        y_data = []
        for sensor_data in sensors:
            landmark_id = sensor_data['id']
            landmark_coord = landmarks[landmark_id]
            x_data.extend([pose[0], landmark_coord[0]])
            y_data.extend([pose[1], landmark_coord[1]])
        connections.set_data(x_data, y_data)

        if frame == trajectory[-1]:
            threading.Timer(1, plt.close, [fig]).start()

        return [robot, connections]

    ani = animation.FuncAnimation(fig,
                                  update,
                                  frames=trajectory,
                                  init_func=init,
                                  blit=True,
                                  interval=50,
                                  repeat=False)
    ax.legend()
    plt.show()
    writer = PillowWriter(fps=20)
    ani.save("motion.gif", writer=writer)
