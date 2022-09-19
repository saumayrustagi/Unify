#!/bin/bash

git status

echo -e "\nBackup all the files? [y/n]"
read answer
if [[ $answer = y ]] ; then
	git add .
	git commit -am 'w'
	git push
fi
