#!/bin/bash

do_start() {
    screen -d -m python siteonlinechecker/scheduler.py
}

do_stop() {
    ps aux | grep scheduler.py | grep -v grep | awk '{print $2;}' | xargs kill
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
