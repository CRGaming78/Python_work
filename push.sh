#!/bin/bash
#####################################
## its not for your use, ignore it ##
#####################################

read -p "Do you want to add all programs(all/0-9):" des
if [[ $des == "all" ]]; then
    git add -A
elif [[ $des == "0-9" ]]; then
    for ((i=0;i>des;i++)); do
        read -p "Enter the name of the program: " pro
        git add $pro
    done
else #bass abhi ke liye use kar raha hu 
    echo "invaild input"
fi
read -p "Enter any msg: " msg
git commit -m "$msg"
git push