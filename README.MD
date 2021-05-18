# Introduction 

Little Python app to load the ADIF log changes from WSJ-X, JS8Call, JTDX and possibly ohers into MagicBug Cloudlog (https://github.com/magicbug/Cloudlog) which has been written by Peter Goodhall (2M0SQL) automatically as the QSOs happen. 2M0SQL has solutions that work on Windows but I needed a Linux application hence wrote this for myself. I probably spent more time writing this Readme than the actual code so don't expect bells & whistles, it works for me.

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
1. Will add JSON configuration file sometime later and also enable file logging instead of simple stderr.
