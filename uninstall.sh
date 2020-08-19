#!/bin/bash
bold_yellow='\033[1;33m'
green='\033[0;32m'
bold_green='\033[1;32m'
null_color='\033[0m'
blue='\033[36m'
red='\e[91m'

if [[ $(id -u) != 0 ]]
then
   echo -e ""$E"$red""Permission denied!$null_color"
   exit 1
fi

trap ctrl_c INT

function ctrl_c() {
  echo -e "$green""Cancelando...$null_color"
  exit 2
}

printf "$bold_green"

cat banner.txt

echo -e "$red\n"

echo "Webscanner está sendo excluido"

printf 'Deseja excluir os scans salvos?:(y/n) '"$null_color"
read scan

echo -e "$red"
echo "Você tem 5 segundos para cancelar(Ctrl+C)"

sleep 5

echo -e "$null_color"

if [ "$scan" = 'y' ] || [ "$scan" = 'yes' ] || [ "$scan" = 's' ] || [ "$scan" = 'sim' ]
then
  {
  rm /usr/bin/webscanner
  rm -r /opt/webscanner
  } &> /dev/null
elif [ "$scan" = 'n' ] || [ "$scan" = 'no' ] || [ "$scan" = 'not' ] || [ "$scan" = 'não' ]
then
  {
  rm /usr/bin/webscanner
  } &> /dev/null
else
  echo "opção invalida"
fi

echo -e "$bold_yellow""WebScanner excluido com sucesso""$null_color"