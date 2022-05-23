# dataset
for i in `seq 1 20`; do mkdir -p "folder$i"; find . -type f -maxdepth 1 | head -n 2000 | xargs -i mv "{}" "folder$i"; done
