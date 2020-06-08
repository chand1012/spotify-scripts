#!/bin/bash

#example use:
# ./run.sh spotify-username

#populate these variables
export SPOTIPY_CLIENT_ID=
export SPOTIPY_CLIENT_SECRET=
export SPOTIPY_REDIRECT_URI=

python3 main.py $1