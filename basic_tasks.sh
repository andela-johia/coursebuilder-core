#!/bin/bash

# NAME
#      basic_tasks.sh -- automates some basic tasks while working on the course builder

# HOW TO RUN
#      1. Navigate to the folder containing the script
#      2. Ensure that the script is executable: `chmod 755 ./basic_tasks.sh`
#      3. Run the script: `./basic_tasks.sh <command>`

# DESCRIPTION
#      basic_tasks.sh is a simple script that automates some basic tasks while working on
#      the course builder app.

#      The options are as follows:

#       img         Sync the images on the frontend folder with that on the course builder app
#                   usage: ./basic_tasks.sh img
#
#       setuptest   Set environmental variables needed for running tests. Replace the paths below with
#                   the appropriate folders on your machine.
#                   usage: source basic_task.sh setuptest
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

if [ $1 = "setuptest" ]
then
    export COURSEBUILDER_RESOURCES=$HOME/Documents/cfa/coursebuilder-core/coursebuilder
    export PYTHONPATH=$PYTHONPATH:$HOME/Documents/cfa/coursebuilder-core/coursebuilder
    export PYTHONPATH=$PYTHONPATH:$HOME/Documents/dev/google-cloud-sdk/platform/google_appengine/lib/webapp2-2.5.1
    export PYTHONPATH=$PYTHONPATH:$HOME/Documents/dev/google-cloud-sdk/platform/google_appengine/lib/jinja2-2.6
    export PYTHONPATH=$PYTHONPATH:$HOME/Documents/dev/google-cloud-sdk/platform/google_appengine
fi
