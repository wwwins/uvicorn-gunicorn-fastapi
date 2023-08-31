#!/usr/bin/env bash
set -e

usage()
{
  echo ""
  echo "Usage: $0 -c 10"
  echo ""
  exit 1
}

while getopts "c:" opt
do
  case "$opt" in
    c ) CNT="$OPTARG" ;;
    ? ) usage ;;
  esac
done

if [ -z "$CNT" ]
then
  usage
fi

for c in $(seq 1 $CNT)
do
  echo "loop-$c"
  for i in {1..9}; do curl --request POST --url http://localhost/predict -F file=@assets/zespri-$i.jpg; echo ""; done
done
