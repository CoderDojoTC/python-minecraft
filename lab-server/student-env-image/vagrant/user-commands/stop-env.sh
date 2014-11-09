#!/bin/dash -e

# This script stops Minecraft and IPython inside the tmux session

MINECRAFT_LAB=$HOME/minecraft_lab

SESSION_NAME=minecraft-lab

# Kill off anything that's already running
tmux kill-session -t ${SESSION_NAME}
