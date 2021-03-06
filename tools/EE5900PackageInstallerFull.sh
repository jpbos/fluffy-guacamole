#!/bin/bash

#ROS Install run as sudoer
apt-get update 
sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'
apt-key adv --keyserver hkp://ha.pool.sks-keyservers.net --recv-key 0xB01FA116
apt-get update
apt-get install -y ros-indigo-desktop-full

#jackal specific ros install packages
apt-get install -y ros-indigo-jackal-simulator ros-indigo-jackal-desktop ros-indigo-jackal-navigation python-catkin-tools

#source ros so that you don't have to source it later
echo 'source /opt/ros/indigo/setup.bash' >> ~/.bashrc

#git install
apt-get install -y git 

#java install
apt-get install -y openjdk-7-jre

#pycharm edu install
cd /tmp 
wget https://download.jetbrains.com/python/pycharm-edu-3.0.tar.gz
tar xfz pycharm-edu-3.0.tar.gz
mv pycharm-edu-3.0 /opt/
rm pycharm-edu-3.0.tar.gz
ln -s /opt/pycharm-edu-3.0/bin/pycharm.sh /usr/local/bin/pycharm

mkdir -p /etc/pki/cert
cp ./chain.cer /etc/pki/cert/


