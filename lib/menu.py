#!/bin/python3
from os import system
import datetime
from lib.utils import connection_verify

d1 = str(datetime.datetime.now().time())

def main_menu():
    print('''\033[1;32m
    __        __   _    ____
    \ \      / /__| |__/ ___|  ___ __ _ _ __  _ __   ___ _ __
     \ \ /\ / / _ \ '_ \___ \ / __/ _` | '_ \| '_ \ / _ \ '__|
      \ V  V /  __/ |_) |__) | (_| (_| | | | | | | |  __/ |
       \_/\_/ \___|_.__/____/ \___\__,_|_| |_|_| |_|\___|_|
    \033[33m           (Ex: www.site.com)
    \033[0m''')
    try:
        site = str(input('\033[0m' + '> Site: '))
    except (KeyboardInterrupt, EOFError, SystemExit):
        print('\033[91mOperação cancelada pelo usuario')
        exit()

    if site == '':
        print('\033[91m[✘]' + '\nOpção Inválida')
        print('\033[0m')
        exit()

    connection_verify(site)

    path = "/opt/webscanner/scans/"+site+'_'+d1
    try:
        http = int(input('> http (1) - https (2): '))
    except:
        print('\033[91m[✘] Essa entrada não pode ser nula nem uma string')
        exit()
    if http != 1 and http != 2:
            print('\033[91m[✘] Selecione 1 ou 2')
            exit()

    system('clear -x')
    return {
      "http": http,
      "site": site,
      "path": path
    }

def choice_menu():
    print('\033[32m' + '(1) Whois Scan')
    print('(2) Nmap Scan')
    print('(3) Whatweb')
    print('(4) Nikto')
    print('(5) Uniscan')
    print('(6) Tudo')

    print('\033[36m')
    try:
        opcao = int(input('[*] Opção > ' + '\033[0m'))
    except (KeyboardInterrupt, EOFError, SystemExit):
        print('Operação cancelada pelo usuario')
        exit()
    if not opcao in range(1, 7):
        print('\033[91m[✘]' + '\nOpção Inválida')
        print('\033[0m')
        exit()

    print('\033[32m' + 'Deseja Salvar o resultado?')
    print('Obs,se escolher 1, o resultado só sera visivel apos a conclução do script')
    print('(1) Sim')
    print('(2) Não')

    print('\033[36m')
    try:
        save = int(input('[*] Opção > ' + '\033[0m'))
    except (KeyboardInterrupt, EOFError, SystemExit):
        print('\033[91mOperação cancelada pelo usuario')
        exit()
    if not save in range(1, 3):
        print('\033[91m[✘]' + '\nOpção Inválida')
        print('\033[0m')
        exit()
    print('\033[93mIsso pode demorar um pouco...\033[0m')
    return {
        'opcao': opcao,
        'save': save
    }