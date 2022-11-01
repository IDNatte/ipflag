#!/bin/bash

#
#
# ![NOTICE ME]
# Configure ipflag application path according to your home folder or where your put your ipflag plugin
# e.g flag=$(path/to/ipflag/executable/file/ipflag --app-type text)
#

flag=$(~/.config/polybar/ipflag/ipflag --app-type text)


echo "$flag"
