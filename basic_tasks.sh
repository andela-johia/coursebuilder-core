#!/bin/bash

# NAME
#      basic_tasks.sh -- automates some basic tasks while working on the course builder

# HOW TO RUN
#      1. Navigate to the folder containing the script
#      2. Ensure that the script is executable: `chmod 755 ./basic_tasks.sh`
#      3. Run the script: `./basic_tasks.sh <command>`

# DESCRIPTION
#      basic_tasks.sh is a simple script that automates some basic tasks while working on
#      the course builder app. For now it accepts just one argument 'img'

#      The options are as follows:

#      img      Sync the images on the frontend folder with that on the course builder app
#               usage: ./basic_tasks.sh img
#
# AUTHOR
#      Anthony Ngene (ngeneanthony@gmail.com)

if [ -z $1 ]
then
    echo "Usage: ./basic_tasks.sh <command>"
    exit 1
fi

if [ $1 = "img" ]
then
    rsync -r frontend/images coursebuilder/modules/explorer/_static
fi
