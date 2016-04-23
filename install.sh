
#!/bin/bash
#
# Script to install HMS program and set-up all requirements and dependencies
# Must be run as superuser with sudo
#
# IIT Kharagpur - Hall Management System
# System to manage Halls of residences, Warden grant requests, student complaints
# hall worker attendances and salary payments
#
# authors: Madhav Datt, Avikalp Srivastava
# MIT License
#

# Move kgp-hms to /etc
cd /etc
mkdir kgp-hms
mv ~/Downloads/kgp-hms/* /etc/kgp-hms
cd kgp-hms

# Grant execute permissions to shell scripts
chmod 755 setup_db.sh
./setup_db.sh
chmod 755 setup_lib.sh
./setup_lib.sh

# Add permanent aliases to run programs
cat aliases.txt >> ~/.bash_aliases
. ~/.bashrc

# Clean downloaded folders
rm -rf ~/Downloads/kgp-hms
rm ~/Downloads/kgp-hms-v1.0.zip
