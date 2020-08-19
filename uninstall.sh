#!/bin/bash
bold_yellow='\033[1;33m'
green='\033[0;32m'
bold_green='\033[1;32m'
null_color='\033[0m'
blue='\033[36m'
red='\e[91m'
bold_red='\e[1;91m'

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

printf 'Deseja excluir os scans salvos?:(y/n) '"$null_color"
read scan

echo -e "$bold_yellow"
echo "Você tem 5 segundos para cancelar(Ctrl+C)"

sleep 5

echo -e "$null_color"

{
if [ "$scan" = 'y' ] || [ "$scan" = 'yes' ] || [ "$scan" = 's' ] || [ "$scan" = 'sim' ]
then
  {
  rm /opt/webscanner
  rm /usr/bin/webscanner
  } &> /dev/null
elif [ "$scan" = 'n' ] || [ "$scan" = 'no' ] || [ "$scan" = 'not' ] || [ "$scan" = 'não' ]
then
  rm /usr/bin/webscanner
else
  echo "opção invalida"
fi
}
if [ $? = '0' ]
then
  echo -e "$bold_green""WebScanner excluido com sucesso""$null_color"
else
  echo -e "$bold_red""Ocorreu um erro ao excluir WebScanner""$null_color"
fi