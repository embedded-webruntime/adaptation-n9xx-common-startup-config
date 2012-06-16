#!/bin/bash
#export SWRENDER=1
unset SWRENDER
export DISPLAY=:0

if [ ! -d ~/.embedded-webruntime/stamp ]; then
rm -rf ~/.embedded-webruntime
mkdir ~/.embedded-webruntime
mkdir ~/.embedded-webruntime/profile

cp -rf /data/local/* ~/.embedded-webruntime/profile
touch ~/.embedded-webruntime/stamp
fi

/usr/lib/ewrt/bin/b2g -profile ~/.embedded-webruntime/profile > ~/.embedded-webruntime/output.log 2>&1