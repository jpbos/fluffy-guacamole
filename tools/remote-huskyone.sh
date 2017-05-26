export ROS_MASTER_URI=http://HuskyOne:11311   # Hostname for HuskyOne
#export ROS_HOSTNAME=HuskyOne
export ROS_IP="$(ifconfig | grep -A 1 'wlan0' | tail -1 | cut -d ':' -f 2 | cut -d ' ' -f 1)"
