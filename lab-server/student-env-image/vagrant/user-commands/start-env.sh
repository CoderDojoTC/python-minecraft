#!/bin/dash -e

# This script starts Minecraft and IPython running inside a tmux
# session.
#
# Afterwards, you can connect to it with the following command:
#
#    tmux attach -t minecraft-lab

. $HOME/minecraft_lab/settings

SESSION_NAME=minecraft-lab

# See if the server has been configured
if ! grep -q 'eula=true' ${MINECRAFT_LAB}/run/eula.txt
then
    # Start the server so that it creates its standard files. It will
    # exit very quickly because the eula file hasn't been tweaked
    # yet. Then, we can make our edits.
    cd ${MINECRAFT_LAB}/run
    java -jar ${MINECRAFT_LAB}/bin/CanaryMod-1.7.10-1.1.2.jar nogui

    perl -pi.old -e "s{player-idle-timeout=1}{player-idle-timeout=15};
                     s{rcon-enabled=false}{rcon-enabled=true};
                     s{rcon-password=}{rcon-password=${PASSWORD_PLAINTEXT}};" \
			 ${MINECRAFT_LAB}/run/config/server.cfg
    echo "eula=true" > ${MINECRAFT_LAB}/run/eula.txt
fi

# Start up Minecraft
cd ${MINECRAFT_LAB}/run
tmux new-session -d -s ${SESSION_NAME} -n minecraft "java -Xincgc -Xmx1G -jar ${MINECRAFT_LAB}/bin/CanaryMod-1.7.10-1.1.2.jar nogui"

# Wait for server to start
while ! ((tmux capture-pane; tmux save-buffer -) |grep -q Done) && killall -0 java ; do
    sleep 1
done

# Do some server configuration
tmux send-keys -t ${SESSION_NAME} -l '
gamerule doMobSpawning false
gamerule doDaylightCycle false
time set 1000
defaultgamemode 1
'

# Start up IPython
cd ${MINECRAFT_LAB}/python-minecraft
tmux new-window -d -t ${SESSION_NAME} -n ipython "ipython notebook --profile=nbserver"

# Start some other useful windows
tmux new-window -d -t ${SESSION_NAME} -n top "top"
tmux new-window -d -t ${SESSION_NAME} -n bash "bash"

cat <<EOF
Environment started. Use 'attach-env.sh' to connect to the controlling
terminals. Use 'stop-env.sh' to halt the environment.
EOF
