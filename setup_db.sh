#!/bin/bash
#
# Script to download and install software and database required for HMS
# Must be run as superuser with sudo
#
# IIT Kharagpur - Hall Management System
# System to manage Halls of residences, Warden grant requests, student complaints
# hall worker attendances and salary payments
#
# authors: Madhav Datt, Avikalp Srivastava
# MIT License
#

"""
@ authors: Madhav Datt, Avikalp Srivastava
"""

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
echo "Switching to secure installation..."
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

# Save encrypted password to local config file
echo ""
echo "hmsuser: Password has been set to hmspasstmp"
echo "Re-enter this password to start table creation"
mysql_config_editor set --login-path=local --host=localhost --user=hmsuser --password

# Create Student table
echo ""
echo "Creating Students Table..."
cat << EOF | /usr/bin/mysql --login-path=local
USE hmskgp;
CREATE TABLE student(
   student_ID INT NOT NULL AUTO_INCREMENT,
   password VARCHAR(200) NOT NULL,
   name VARCHAR(50),
   address VARCHAR(50),
   contact_number VARCHAR(15),
   hall_ID INT NOT NULL,
   room_no VARCHAR(5),
   mess_charge FLOAT(10,2),
   room_type CHAR,
   PRIMARY KEY (student_ID)
   );
EOF

# Create Warden table
echo ""
echo "Creating Wardens Table..."
cat << EOF | /usr/bin/mysql --login-path=local
USE hmskgp;
CREATE TABLE warden(
   warden_ID INT NOT NULL AUTO_INCREMENT,
   password VARCHAR(200) NOT NULL,
   name VARCHAR(50),
   email VARCHAR(50),
   hall_ID INT NOT NULL,
   controlling_warden VARCHAR(6),
   PRIMARY KEY (warden_ID)
   );
EOF

# Create GrantRequest Table
echo ""
echo "Creating Grant Request Table..."
cat << EOF | /usr/bin/mysql --login-path=local
USE hmskgp;
CREATE TABLE grant_request(
   grant_ID INT NOT NULL AUTO_INCREMENT,
   repair_charge FLOAT(10,2),
   other_charge FLOAT(10,2),
   salary_charge FLOAT(10,2),
   hall_ID INT NOT NULL,
   PRIMARY KEY (grant_ID)
   );
EOF

# Create HallManagement table
# Set password to hmspasstmp
echo ""
echo "Creating Hall Management Table..."
echo "HMC Password is set to: hmspasstmp"
cat << EOF | /usr/bin/mysql --login-path=local
USE hmskgp;
CREATE TABLE hmc(
   password VARCHAR(200) NOT NULL,
   payment_is_active VARCHAR(6)
   );
INSERT INTO hmc (password, payment_is_active) VALUES ("$2b$12$hV/Uk9ejKp70wSHhqT3.reyx7oPIkKQaN5mXanWJ3usYt3VwlENwK", "False");
EOF

# Create Hall table
echo ""
echo "Creating Halls Table..."
cat << EOF | /usr/bin/mysql --login-path=local
USE hmskgp;
CREATE TABLE hall(
   hall_ID INT NOT NULL AUTO_INCREMENT,
   name VARCHAR(50),
   warden_ID INT NOT NULL,
   clerk_ID INT NOT NULL,
   mess_manager_ID INT NOT NULL,
   status CHAR,
   single_room_count INT,
   double_room_count INT,
   single_room_occupancy INT,
   double_room_occupancy INT,
   single_room_rent FLOAT(10,2),
   double_room_rent FLOAT(10,2),
   amenities_charge FLOAT(10,2),
   mess_account FLOAT(10,2),
   amenities_account FLOAT(10,2),
   repair_account FLOAT(10,2),
   salary_account FLOAT(10,2),
   others_account FLOAT(10,2),
   rent_account FLOAT(10,2),
   PRIMARY KEY (hall_ID)
   );
EOF

# Create Worker table
echo ""
echo "Creating Workers Table..."
cat << EOF | /usr/bin/mysql --login-path=local
USE hmskgp;
CREATE TABLE worker(
   worker_ID INT NOT NULL AUTO_INCREMENT,
   password VARCHAR(200),
   name VARCHAR(50),
   worker_type CHAR,
   monthly_salary FLOAT(10,2),
   daily_wage FLOAT(10,2),
   hall_ID INT NOT NULL,
   monthly_attendance INT,
   PRIMARY KEY (worker_ID)
   );
EOF

# Create Worker Attendance Date Table
echo ""
echo "Creating Worker Attendance Date Table..."
cat << EOF | /usr/bin/mysql --login-path=local
USE hmskgp;
CREATE TABLE attend_date(
   last_attend DATE
   );
INSERT INTO attend_date VALUES (2000-01-01);
EOF

# Create Complaint Attendance table
echo ""
echo "Creating Student Complaints Table..."
cat << EOF | /usr/bin/mysql --login-path=local
USE hmskgp;
CREATE TABLE complaint(
   complaint_ID INT NOT NULL AUTO_INCREMENT,
   student_ID INT NOT NULL,
   action_status CHAR,
   description BLOB,
   action_report BLOB,
   PRIMARY KEY (complaint_ID)
   );
EOF
