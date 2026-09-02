#!/bin/bash
cd ~/Documents/git_repos/computation_for_linguists/LIN_301/homework/hw1
mkdir backup_check
curl -o ./backup_check/holmes.txt https://www.gutenberg.org/cache/epub/1661/pg1661.txt
echo "Download of holmes.txt to directory backup_check complete."
