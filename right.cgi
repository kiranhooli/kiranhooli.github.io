#!/bin/bash
gpio -g write 5 0
gpio -g write 6 1
gpio -g write 13 0
gpio -g write 19 1
gpio pwm 1 1023

