#!/bin/bash

ip link add name br0 type bridge
ip link set eth0 master br0 
ip link set tap0 master br0
ip link set dev br0 up
