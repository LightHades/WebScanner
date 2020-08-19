#!/bin/bash
source "spinner.sh"

yellow='\033[0;33m'
bold_yellow='\033[1;33m'
bold_green='\033[1;32m'
null_color='\033[0m'
blue='\033[36m'
red='\e[91m'
bold_purple='\033[0;34m'

printf "$blue[*] Deseja ativar o modo verbose?(y/n) > $null_color"
read verbose

if [[ $(id -u) != 0 ]]
then
   echo -e ""$E""$red"Permission denied!$null_color"
   exit
fi
echo -e "$blue[*] Testando conexão...$null_color"
start_spinner
{
ASESR="$(ping -c 1 -q www.google.com >&/dev/null; echo $?)"
} &> /dev/null

if [[ "$ASESR" != 0 ]]
then 
   echo -e ""$E"$red""No Internet connection!$null_color"
   stop_spinner !$?
   exit
fi
stop_spinner $?

sleep 1
clear -x
sleep 0.5
echo -e "$bold_green"

cat banner.txt 2> /dev/null

echo -e "$null_color"

echo -e "$bold_purple[*] Instalando dependencias$null_color"
echo -e "$bold_yellow[!] Isso pode demorar um pouco... $null_color"

if [ "$verbose" = "s" ] || [ "$verbose" = "sim" ] || [ "$verbose" = "y" ] || [ "$verbose" = "yes" ]
then
   {
   apt-get update
   apt-get -y install uniscan
   apt-get -y install nikto
   apt-get -y install whois
   apt-get -y install nmap

   pkg update
   pkg -y install uniscan
   pkg -y install nikto
   pkg -y install whois
   pkg -y install nmap

   apk update
   apk add uniscan
   apk add nikto
   apk add whois
   apk add nmap

   pacman -Sy
   pacman -S --noconfirm uniscan
   pacman -S --noconfirm nikto
   pacman -S --noconfirm whois
   pacman -S --noconfirm nmap

   zypper refresh
   zypper install -y uniscan
   zypper install -y nikto
   zypper install -y whois
   zypper install -y nmap

   yum -y install uniscan
   yum -y install nikto
   yum -y install whois
   yum -y install nmap

   dnf -y install uniscan
   dnf -y install nikto
   dnf -y install whois
   dnf -y install nmap

   eopkg update-repo
   eopkg -y install uniscan
   eopkg -y install nikto
   eopkg -y install whois
   eopkg -y install nmap

   xbps-install -S
   xbps-install -y uniscan
   xbps-install -y nikto
   xbps-install -y whois
   xbps-install -y nmap

   mkdir /opt/webscanner
   mkdir /opt/webscanner/scans
   cp banner.rb /usr/lib/ruby/vendor_ruby/whatweb/
   chmod +x webscanner
   cp webscanner /usr/bin/
   } 2> /dev/null
else
   {
   apt-get update
   apt-get -y install uniscan
   apt-get -y install nikto
   apt-get -y install whois
   apt-get -y install nmap

   pkg update
   pkg -y install uniscan
   pkg -y install nikto
   pkg -y install whois
   pkg -y install nmap

   apk update
   apk add uniscan
   apk add nikto
   apk add whois
   apk add nmap

   pacman -Sy
   pacman -S --noconfirm uniscan
   pacman -S --noconfirm nikto
   pacman -S --noconfirm whois
   pacman -S --noconfirm nmap

   zypper refresh
   zypper install -y uniscan
   zypper install -y nikto
   zypper install -y whois
   zypper install -y nmap

   yum -y install uniscan
   yum -y install nikto
   yum -y install whois
   yum -y install nmap

   dnf -y install uniscan
   dnf -y install nikto
   dnf -y install whois
   dnf -y install nmap

   eopkg update-repo
   eopkg -y install uniscan
   eopkg -y install nikto
   eopkg -y install whois
   eopkg -y install nmap

   xbps-install -S
   xbps-install -y uniscan
   xbps-install -y nikto
   xbps-install -y whois
   xbps-install -y nmap

   mkdir /opt/webscanner
   mkdir /opt/webscanner/scans
   cp banner.rb /usr/lib/ruby/vendor_ruby/whatweb/
   chmod +x webscanner
   cp webscanner /usr/bin/
   } &> /dev/null
fi
clear -x
echo -e "$bold_green[+] Dependencia instalada com sucesso!$null_color"
echo -e "$yellow"'\n[+] O WebScanner está pronto para ser usado, digite '$bold_yellow"webscanner"$yellow' para executá-lo'
echo -e "$null_color"