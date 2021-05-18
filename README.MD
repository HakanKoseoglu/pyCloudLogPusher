# Prerequisites

pip3 install watchdog

# Running

python3 pyCloudLogWatcher.py

# Config
To make it docker-friendly, the app uses environment variables. 

Generate an API key from Cloudlog.

export CloudlogAPIKey=<your API key here>

export ProfileID=<your profile ID here, 1 for the first one you have created>

export LogfilePath=/home/hakan/.local/share/WSJT-X

export LogBookServer='https://logbook.koseoglu.org'

This should also work on non-Linux environments but it's not tested.

# Future
1. Will add JSON configuration file sometime later this week.
