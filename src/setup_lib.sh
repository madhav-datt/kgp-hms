#!/bin/bash
#
# Script to download and install miscellaneous libraries required for HMS
# Must be run as superuser with sudo
#
# IIT Kharagpur - Hall Management System
# System to manage Halls of residences, Warden grant requests, student complaints
# hall worker attendances and salary payments
#
# authors: Madhav Datt, Avikalp Srivastava
# MIT License
#

# Install bcrypt for password hashing and authentication
apt-get install python.bcrpyt

# Install PyFPDF - a library for PDF document generation under Python
git clone https://github.com/reingart/pyfpdf.git
cd pyfpdf
python setup.py install
cd ..

# Install MySQL Python Connector API
wget -P ~/Downloads http://dev.mysql.com/get/Downloads/Connector-Python/mysql-connector-python_2.1.3-1ubuntu15.04_all.deb
cd Downloads
dpkg -i mysql-connector-python_2.1.3-1ubuntu15.04_all.deb
rm mysql-connector-python_2.1.3-1ubuntu15.04_all.deb
