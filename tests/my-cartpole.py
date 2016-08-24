import gym
import numpy as np
import time

np.random.seed(1000)


class CPController(object):
    def __init__(self):
        self.n_input = 0

    def action(self):
        print "pass"

if __name__ == '__main__':
    print "starting cart pole"
    env = gym.make('CartPole-v0')
    # env.monitor.start(result_location, force=True)
    for i_episode in range(209):
        observation = env.reset()
        for t in range(20):
            env.render()
            action = 0
            observation, reward, done, info = env.step(action)
            print observation, reward, done, info
            print action
            if done:
                print("Episode finished after {} timesteps".format(t+1))
        
