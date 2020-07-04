#!/usr/bin/python3

from os import system
print('')
system('apt-get update')
system('apt-get install uniscan')
system('apt-get install nikto')
system('apt-get install whois')
system('apt-get install nmap')
system('cp banner.rb /usr/lib/ruby/vendor_ruby/whatweb/')
system('chmod +x webscanner')
system('cp webscanner /usr/bin/')
print('\033[33;1m' + '\n[+] O WebScanner está pronto para ser usado, digite "webscanner" para executá-lo')
print('\033[0m')
