#!/usr/bin/env bash

RANDOM_STRING=$(echo $RANDOM | md5sum | head -c 3)

# Sends the stdout to script.log
exec > "${RANDOM_STRING}-script.log"

# Time and Date
date

# List all Users
users

# Computer Uptime
uptime


