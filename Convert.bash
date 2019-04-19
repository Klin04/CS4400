# !/bin/bash
for filename in *.ui; do
    IFS='.' 
    read var1 var2 <<< "$filename"
    echo "$var1" 
    echo "$var2"
    pyuic5 "$filename" > "$var1.py"
done