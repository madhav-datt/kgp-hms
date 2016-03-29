#!/bin/bash
#
# Script to download and install software and database required for HMS
# Must be run as superuser with sudo
#
# Software Engineering Lab - Assignment 5
# IIT Kharagpur - Hall Management System
#
# authors: Madhav Datt (14CS30015), Avikalp Srivastava (14CS10008)
#

# Install MySQL Server
# Will be prompted to enter and confirm root password
echo "Installing MySQL Server"
echo ""
apt-get install mysql-server

# Start MySQl service/Ensure service is running
service mysql start
/usr/sbin/update-rc.d mysql defaults

# Address security concerns in default MySQL installation
# For use in production environment: Recommended answers N Y Y Y Y to run all
# required parts of the script
mysql_secure_installation

echo ""
