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
read -p "Do you want any program to unstage?(y/n):" cho
if [[ $cho == "y" || $cho == "Y"]]; then
    while True; do
        read -p "Enter the name of the program: " de_pro
        git reset $de_pro
        read -p "Do you want remove more?(y/n)" in_cho
        if [[ $cho == "n" || $cho == "N"]]; then
            break
        fi
    done
fi
read -p "Enter msg to commit: " msg
git commit -m "$msg"
git push