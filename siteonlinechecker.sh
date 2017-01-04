#!/bin/bash

do_start() {
    screen -d -m python siteonlinechecker/scheduler.py
}

do_stop() {
    echo 'stop'
}

case "$1" in
  start)
    do_start
	;;
  stop)
    do_stop

	;;
  *)
	echo "Usage: $SCRIPTNAME {start|stop}" >&2
	exit 3

	;;
esac
