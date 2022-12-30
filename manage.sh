#!/bin/bash

# variables
type=$1
. ./.env
terminalColorClear='\033[0m'
terminalColorEmphasis='\033[1;32m'
terminalColorError='\033[1;31m'
terminalColorWarning='\033[1;33m'
 
# functions
echoDefault() {
    echo -e "${terminalColorClear}$1${terminalColorClear}"
}
echoWarning() {
    echo -e "${terminalColorWarning}$1${terminalColorClear}"
} 
echoError() {
    echo -e "${terminalColorError}$1${terminalColorClear}"
} 

# code
if [[ -z $1 ]]; then 
    echoWarning "No parameter passed."
fi

if [ "$type" = "build" ]; then
	echoDefault "building containers"
    sudo docker compose build

elif [ "$type" = "update" ]; then
	echoDefault "updating containers"
    sudo docker compose pull

elif [ "$type" = "start" ]; then
	echoDefault "starting containers"
    sudo docker compose up -d

elif [ "$type" = "stop" ]; then
	echoDefault "stopping containers"
    sudo docker compose down

else
	echoWarning "you can chose the options build, update, start, stop. selected $type"
fi