# !/bin/bash
for filename in *.ui; do
    IFS='.' 
    read var1 var2 <<< "$filename"
    echo "$var1" 
    echo "$var2"
    newFileName="$var1.py"
    pyuic5 "$filename" > newFileName
done
IFS=' '