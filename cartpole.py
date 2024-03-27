import gym

env = gym.make("CartPole-v1")

env.reset()

terminated = False
total_reward = 0
while not terminated:
   env.render()
   observation, reward, terminated, truncated, info = env.step(env.action_space.sample())
   total_reward += reward
   print(f"{observation} -> {reward}")
print(f"Total reward: {total_reward}")