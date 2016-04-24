#!/bin/bash
#
# Script to run Hall Office Clerk System
# Must be run as superuser with sudo
#
# IIT Kharagpur - Hall Management System
# System to manage Halls of residences, Warden grant requests, student complaints
# hall worker attendances and salary payments
#
# authors: Madhav Datt, Avikalp Srivastava
# MIT License
#

cd /etc/kgp-hms
python -m src.ui.Clerk_Window_GUI

