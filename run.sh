#!/bin/bash
which chromedriver
if [ $(ps -ef | grep -c "article_list") -gt 1 ]
then 
  echo "true"; 
fi
