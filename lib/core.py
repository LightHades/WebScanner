from os import system

def core(opcao, save, site, http, path):
    if opcao == 1:
        if save == 1:
            system(f'echo "whois output:" >> {path}')
            system(f'\nwhois {site} >> {path}')
        else:
            system(f'\nwhois {site}')

    elif opcao == 2:
        print('\n(1) > Simples')
        print('(2) > Completo')
        nmap = int(input('\n-> \033[0m'))
        if nmap == 1:
            if save == 1:
                system(f'echo "Nmap output:" >> {path}')
                system(f'\nnmap {site} >> {path}')
            else:
                system(f'\nnmap {site}')
        elif nmap == 2:
            if save == 1:
                system(f'echo "Nmap output:" >> {path}')
                system(f'\nnmap -sV -A -O {site} >> {path}')
            else:
                system(f'\nnmap -sV -A -O {site}')

    elif opcao == 3:
        if http == 1:
            if save == 1:
                system(f'echo "Whatweb output:" >> {path}')
                system(f'\nwhatweb http://{site} >> {path}')
            else:
                system(f'\nwhatweb http://{site}')
        elif http == 2:
            if save == 1:
                system(f'echo "Whatweb output:" >> {path}')
                system(f'\nwhatweb https://{site} >> {path}')
            else:
                system(f'\nwhatweb https://{site}')

    elif opcao == 4:
        if http == 1:
            if save == 1:
                system(f'echo "Nikto output:" >> {path}')
                system(f'\nnikto -host http://{site} >> {path}')
            else:
                system(f'\nnikto -host http://{site}')            
        elif http == 2:
            if save == 1:
                system(f'echo "Nikto output:" >> {path}')
                system(f'\nnikto -host https://{site} >> {path}')
            else:
                system(f'\nnikto -host https://{site}')
            

    elif opcao == 5:
        if http == 1:
            if save == 1:
                system(f'echo "UniScan output:" >> {path}')
                system(f'\nuniscan -u http://{site} -qweds >> {path}')
            else:
                system(f'\nuniscan -u http://{site} -qweds')
        elif https == 2:
            if save == 1:
                system(f'echo "UniScan output:" >> {path}')
                system(f'\nuniscan -u https://{site} -qweds >> {path}')
            else:
                system(f'\nuniscan -u https://{site} -qweds')
            
    elif opcao == 6:
        if http == 1:
            print('\nWHOIS\n')
            if save == 1:
                system(f'echo "Whois output:" >> {path}')
                system(f'\nwhois {site} >> {path}')
            else:
                system(f'\nwhois {site}')
            

            print('\nWHATWEB\n')
            if save == 1:
                system(f'echo "Whatweb output:" >> {path}')
                system(f'\nwhatweb http://{site} >> {path}')
            else:
                system(f'\nwhatweb http://{site}')

            
            print('\n(1) > Simples')
            print('(2) > Completo')
            nmap = int(input('\n-> \033[0m'))

            if not nmap in range(1, 3):
                print('\033[91m[✘]' + '\nOpção Inválida')
                print('\033[0m')
                exit()
            
            if nmap == 1:
                print('\nNMAP (simples)\n')
                if save == 1:
                    system(f'echo "Nmap output:" >> {path}')
                    system(f'\nnmap {site} >> {path}')
                else:
                    system(f'\nnmap {site}')
                    
            elif nmap == 2:
                print('\nNMAP (completo)\n')
                if save == 1:
                    system(f'echo "Nmap output:" >> {path}')
                    system(f'\nnmap -sV -A -O {site} >> {path}')
                else:
                    system(f'\nnmap -sV -A -O {site}')


            print('\nNIKTO\n')
            if save == 1:
                system(f'echo "Nikto output:" >> {path}')
                system(f'\nnikto -host http://{site} >> {path}')
            else:
                system(f'\nnikto -host http://{site}')

            print('\nUNISCAN\n')
            if save == 1:
                system(f'echo "UniScan output:" >> {path}')
                system(f'\nuniscan -u http://{site} -qweds >> {path}')
            else:
                system(f'\nuniscan -u http://{site} -qweds')

        elif http == 2:
            print('\nWHOIS\n')
            if save == 1:
                system(f'echo "Whois output:" >> {path}')
                system(f'\nwhois {site} >> {path}')
            else:
                system(f'\nwhois {site}')
            

            print('\nWHATWEB\n')
            if save == 1:
                system(f'echo "Whatweb output:" >> {path}')
                system(f'\nwhatweb https://{site} >> {path}')
            else:
                system(f'\nwhatweb https://{site}')

            print('NMAP')
            print('\n(1) > Simples')
            print('(2) > Completo')
            nmap = int(input('\n-> \033[0m'))

            if not nmap in range(1, 3):
                print('\033[91m[✘]' + '\nOpção Inválida')
                print('\033[0m')
                exit()
            
            if nmap == 1:
                print('\nNMAP (simples)\n')
                if save == 1:
                    system(f'echo "Nmap output:" >> {path}')
                    system(f'\nnmap {site} >> {path}')
                else:
                    system(f'\nnmap {site}')
                    
            elif nmap == 2:
                print('\nNMAP (completo)\n')
                if save == 1:
                    system(f'echo "Nmap output:" >> {path}')
                    system(f'\nnmap -sV -A -O {site} >> {path}')
                else:
                    system(f'\nnmap -sV -A -O {site}')


            print('\nNIKTO\n')
            if save == 1:
                system(f'echo "Nikto output:" >> {path}')
                system(f'\nnikto -host https://{site} >> {path}')
            else:
                system(f'\nnikto -host https://{site}')

            print('\nUNISCAN\n')
            if save == 1:
                system(f'echo "UniScan output:" >> {path}')
                system(f'\nuniscan -u https://{site} -qweds >> {path}')
            else:
                system(f'\nuniscan -u https://{site} -qweds')