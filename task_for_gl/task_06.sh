targer=/pathto/folder
declare -A arr

for entry in "$target"/*; do
  if [[ $(stat -c %Y "$entry") > $(date +%s -d "last week") ]];
  then
    arr["$entry"]=$(stat -c %Y "$entry");
    fi;
done

for k in "${!arr[@]}";
  do
    echo "$k" ' - ' ${arr["$k"]};
    done | sort -rn -k3
