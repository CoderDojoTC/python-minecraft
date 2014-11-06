#!/bin/dash -e

# This script starts Minecraft and IPython running inside a tmux
# session.
#
# Afterwards, you can connect to it with the following command:
#
#    tmux attach -t minecraft-lab

MINECRAFT_LAB=$HOME/minecraft_lab

SESSION_NAME=minecraft-lab

# See if the server has been configured
if ! grep -q 'eula=true' ${MINECRAFT_LAB}/run/eula.txt
then
    echo "eula=true" > ${MINECRAFT_LAB}/run/eula.txt
    perl -pi.old -e "s{player-idle-timeout=1}{player-idle-timeout=15};" ${MINECRAFT_LAB}/run/config/server.cfg
fi

# Start up Minecraft
cd ${MINECRAFT_LAB}/run
tmux new-session -d -s ${SESSION_NAME} -n minecraft "java -Xincgc -Xmx1G -jar ${MINECRAFT_LAB}/bin/CanaryMod-1.7.10-1.1.2.jar nogui"

# Start up IPython
cd ${MINECRAFT_LAB}/python-minecraft
tmux new-window -d -t ${SESSION_NAME} -n ipython "ipython notebook --profile=nbserver"

# Start some other useful windows
tmux new-window -d -t ${SESSION_NAME} -n top "top"
tmux new-window -d -t ${SESSION_NAME} -n bash "bash"
