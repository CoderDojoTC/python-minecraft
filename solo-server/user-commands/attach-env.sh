#!/bin/dash -e

# This script attaches to the tmux session hosting Minecraft

MINECRAFT_LAB=$HOME/minecraft_lab

SESSION_NAME=minecraft-lab

# Connect
tmux attach -t ${SESSION_NAME}
