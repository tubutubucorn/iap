#!/bin/bash
OPT=${1} # up or down
for i in "web-server_badstore" "file-server_owncloud" "mail-server_rainloop" "pep" "pdp"
do
	cd $i
	make $OPT
	cd ..
done
