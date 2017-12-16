#!/bin/bash
which chromedriver
if [ $(ps -ef | grep -c "article_list") -gt 0 ]
then 
  echo "Start the program...."
  python -u /data/taobaoke/article_list.py > /tmp/6
fi
