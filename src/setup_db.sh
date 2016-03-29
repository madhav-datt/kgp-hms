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
echo "Installing MySQL Server..."
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
echo "Configuring MySQL User for system..."
echo "Creating Database and Tables..."
echo "Managing Privileges..."

# Create user on localhost for HMS
# User: hmsuser
# Password: hmspasstmp
cat << EOF | /usr/bin/mysql -u root -p
CREATE USER 'hmsuser'@'localhost' IDENTIFIED BY 'hmspasstmp';
CREATE DATABASE hmskgp;
GRANT ALL PRIVILEGES ON hmskgp . * TO 'hmsuser'@'localhost';
FLUSH PRIVILEGES;
EOF

# Create Student table
echo ""
echo "Creating Students Table..."
cat << EOF | /usr/bin/mysql -u hmsuser -phmspasstmp
USE hmskgp;
CREATE TABLE student(
   student_ID INT NOT NULL AUTO_INCREMENT,
   password VARCHAR(200) NOT NULL
   name VARCHAR(50)
   address VARCHAR(50)
   contact_number VARCHAR(15)
   hall_ID INT NOT NULL
   room_no VARCHAR(5)
   mess_charge FLOAT(10,2)
   room_type CHAR
   PRIMARY KEY (student_ID)
   FOREIGN KEY (hall_ID) REFERENCES hall(hall_ID)
   );
EOF
