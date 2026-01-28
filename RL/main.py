import gymnasium as gym
import numpy as np
import pygame
import matplotlib.pyplot as plt
from IPython.display import display, clear_output
import time
from PIL import Image # For consistency, though not directly used in the final display part below.

# --- 1. Pygame Setup (from previous cells) ---
# Initialize Pygame
pygame.init()

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

# Define dimensions for the Taxi-v3 grid
CELL_SIZE = 100  # pixels per cell
GRID_SIZE = 5    # Taxi-v3 is a 5x5 grid
WIDTH = GRID_SIZE * CELL_SIZE
HEIGHT = GRID_SIZE * CELL_SIZE

# Set up the display window (for rendering to rgb_array)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Taxi-v3 Environment")
clock = pygame.time.Clock()

# --- 2. Rendering Function (from previous cells) ---
# Helper function to convert state indices to row/column for rendering
def decode_state_to_coords(env, state):
    taxi_row, taxi_col, pass_idx, dest_idx = env.unwrapped.decode(state)
    return taxi_row, taxi_col, pass_idx, dest_idx

# Define the rendering function adapted for Colab
def render_taxi_env(screen, env_state, env_obj):
    screen.fill(BLACK)

    for x in range(0, WIDTH + 1, CELL_SIZE):
        pygame.draw.line(screen, WHITE, (x, 0), (x, HEIGHT), 1)
    for y in range(0, HEIGHT + 1, CELL_SIZE):
        pygame.draw.line(screen, WHITE, (0, y), (WIDTH, y), 1)

    taxi_row, taxi_col, pass_idx, dest_idx = decode_state_to_coords(env_obj, env_state)

    passenger_locations = [
        (0, 0), (0, 4), (4, 0), (4, 3)
    ]
    destination_locations = [
        (0, 0), (0, 4), (4, 0), (4, 3)
    ]

    dest_row, dest_col = destination_locations[dest_idx]
    dest_rect = pygame.Rect(dest_col * CELL_SIZE + 1, dest_row * CELL_SIZE + 1, CELL_SIZE - 2, CELL_SIZE - 2)
    pygame.draw.rect(screen, GREEN, dest_rect)

    if pass_idx < 4:
        pass_row, pass_col = passenger_locations[pass_idx]
        center_x = pass_col * CELL_SIZE + CELL_SIZE // 2
        center_y = pass_row * CELL_SIZE + CELL_SIZE // 2
        pygame.draw.circle(screen, BLUE, (center_x, center_y), CELL_SIZE // 3)

    taxi_rect = pygame.Rect(taxi_col * CELL_SIZE + 5, taxi_row * CELL_SIZE + 5, CELL_SIZE - 10, CELL_SIZE - 10)
    pygame.draw.rect(screen, YELLOW, taxi_rect)
    if pass_idx == 4:
        pygame.draw.rect(screen, RED, taxi_rect, 5)

    img_data = np.transpose(pygame.surfarray.array3d(screen), (1, 0, 2))
    return img_data

print("Pygame setup and rendering function defined.")

# --- 3. Q-learning Training Loop (from cell 5wYFkSReEDXL) ---
print("\n--- Starting Q-learning Training ---")
env = gym.make("Taxi-v3", render_mode="rgb_array")

q_table = np.zeros([env.observation_space.n, env.action_space.n])

alpha = 0.1    # Learning rate
gamma = 0.6    # Discount factor
epsilon = 0.1  # Exploration rate (10% chance to try something random)

for i in range(1, 1001):
    state, info = env.reset()
    terminated = False
    
    while not terminated:
        if np.random.uniform(0, 1) < epsilon:
            action = env.action_space.sample()
        else:
            action = np.argmax(q_table[state])

        next_state, reward, terminated, truncated, info = env.step(action)
        
        old_value = q_table[state, action]
        next_max = np.max(q_table[next_state])
        
        new_value = (1 - alpha) * old_value + alpha * (reward + gamma * next_max)
        q_table[state, action] = new_value
        
        state = next_state

print("Training finished! Q-table updated.")

# --- 4. Evaluation Loop with Visualization (from cell a4c3445d) ---
print("\n--- Starting Agent Evaluation with Pygame Rendering (Colab compatible) ---")

# Reset the environment for evaluation
state, info = env.reset()
done = False
current_episode_rewards = []

# Setup matplotlib figure for displaying frames
fig, ax = plt.subplots(1, 1, figsize=(GRID_SIZE, GRID_SIZE))
ax.set_xticks([])
ax.set_yticks([])

# Get initial frame and display it
initial_frame = render_taxi_env(screen, state, env)
img_plot = ax.imshow(initial_frame)
display(fig)
clear_output(wait=True)

while not done:
    action = np.argmax(q_table[state])
    next_state, reward, terminated, truncated, info = env.step(action)

    current_episode_rewards.append(reward)

    frame = render_taxi_env(screen, state, env)
    img_plot.set_data(frame)
    display(fig)
    clear_output(wait=True)

    time.sleep(0.1)

    state = next_state
    done = terminated or truncated

print("Agent evaluation finished.")
plt.close(fig) # Close the matplotlib figure after evaluation
pygame.quit() # Quit Pygame components cleanly

# --- Display Rewards --- 
plt.figure(figsize=(10, 3))
plt.plot(current_episode_rewards)
plt.title("Rewards per Step during Evaluation Episode")
plt.xlabel("Step")
plt.ylabel("Reward")
plt.grid(True)
plt.show()
print(f"Total reward during evaluation: {sum(current_episode_rewards)}")
