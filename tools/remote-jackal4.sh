export ROS_MASTER_URI=http://jackal4:11311   # Hostname for Jackal 1
#export ROS_HOSTNAME=jackal1
export ROS_IP="$(ifconfig | grep -A 1 'wlan0' | tail -1 | cut -d ':' -f 2 | cut -d ' ' -f 1)"
