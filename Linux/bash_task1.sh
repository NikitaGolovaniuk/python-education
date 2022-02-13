#! /usr/bin/env bash

#Ask the user if he wants files or directories too.
echo "1 - Only files. 2 - with DIRs"
read SEARCH_TYPE

echo "Which kind of sort do you prefer?:
1.Alphabeticaly 2.By size 3.By date"
read SORT_TYPE

#Forming command 
case $SORT_TYPE in
  1)
    if [ $SEARCH_TYPE -eq 1 ] 
    then
      find * -maxdepth 0 -type f
    else
      ls -l
    fi
    ;;
  2)
    if [ $SEARCH_TYPE -eq 1 ] 
    then
      find * -maxdepth 0 -type f -printf "%p %kkB\n" | sort -n -k2
    else
      ls -lS
    fi
    ;; 
  3)
    if [ $SEARCH_TYPE -eq 1 ] 
    then
      find * -maxdepth 0 -type f -printf "%T@ %Tc %p\n" | sort -n
    else
      ls -r --sort=time
    fi
    ;;
esac

echo "Current date: "$(date)
