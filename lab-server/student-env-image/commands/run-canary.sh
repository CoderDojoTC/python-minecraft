#!/bin/dash -e

# This script should be run by Supervisor to start up a Canary server
# instance (Minecraft server) to support the python-minecraft lab
# activities. It is configured through environment variables which get
# passed in from the `docker run` command line.

# ----------------------------------------------------------------------------
# Determine a few things

LAB_USER=student
MINECRAFT_LAB=/home/${LAB_USER}/minecraft-lab


# ----------------------------------------------------------------------------
# Copy the necessary files into place

if [ ! -d ${MINECRAFT_LAB}/server-files ]; then
    mkdir -p ${MINECRAFT_LAB}
    cp -pr /usr/local/share/default-canary-files ${MINECRAFT_LAB}/server-files

    # Fix up permissions
    chown -R ${LAB_USER}:${LAB_USER} ${MINECRAFT_LAB}/server-files
fi

# Open up permissions on the Canary jar
chmod go+r /usr/local/bin/CanaryMod-*.jar


# ----------------------------------------------------------------------------
# Start the server

# Op the users
echo ${MOJANG_ACCOUNTS} | perl -pe "s{,}{\n}g" >>${MINECRAFT_LAB}/server-files/config/ops.cfg

cd ${MINECRAFT_LAB}/server-files
chown -R ${LAB_USER}:${LAB_USER} .

SESSION_NAME=minecraft

tmux new-session -d -s ${SESSION_NAME} -n minecraft "su ${LAB_USER} -c \"java -Xincgc -Xmx1G -jar /usr/local/bin/CanaryMod-*.jar nogui\"; tmux wait-for -S minecraft-out"

# Wait for server to start
sleep 5
while ! (tmux capture-pane \; save-buffer - |grep -q Done) && killall -0 java ; do
    sleep 1
done

# Do some server configuration
tmux send-keys -t ${SESSION_NAME} 'gamerule doMobSpawning false' C-m
tmux send-keys -t ${SESSION_NAME} 'gamerule doDaylightCycle false' C-m
tmux send-keys -t ${SESSION_NAME} 'time set 1000' C-m
tmux send-keys -t ${SESSION_NAME} 'defaultgamemode 1' C-m
tmux send-keys -t ${SESSION_NAME} 'weather clear 999999' C-m

# Check for receipt of signals indicating we should exit. Send the
# 'stop' command to Canary if we get one.
trap "tmux send-keys -t ${SESSION_NAME} stop C-m" TERM INT QUIT

# -- DIRTY HACK WARNING ------------------------------------------------------

# NOTE: This is a dirty hack. For some reason, Canary is failing to
# determine the UUID of the players listed in ops.txt on startup, so
# I've had to put this reactive code here to do the job after the
# player joins the server.

sleep 10
while ! ( grep -iq "\[INFO\]: ${MOJANG_ACCOUNTS} joined the game" ${MINECRAFT_LAB}/server-files/logs/latest.log  && tmux send-keys -t ${SESSION_NAME} "op ${MOJANG_ACCOUNTS}" C-m ) ; do
    tmux send-keys -t ${SESSION_NAME} "say Waiting for ${MOJANG_ACCOUNTS} to join the game..." C-m
    sleep 5
done
# -- DIRTY HACK WARNING ------------------------------------------------------

# Pause here until the original session kicks out the "minecraft-out"
# signal (generated with the tmux wait-for -S).
tmux wait-for minecraft-out
