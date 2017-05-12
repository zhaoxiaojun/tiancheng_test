#!/bin/sh

# find /home/jenkins/pkg/TianChengSystem/ -name "`date +'%Y'*`"  -mmin +120 -exec rm -rf {} \;
/usr/bin/find /home/jenkins/pkg/TianChengSystem/ -name "*_build-*"  -mmin +120 -exec rm -rf {} \;
