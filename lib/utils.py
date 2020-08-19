from os import system

def connection_verify(site):
  print ('\033[36m[*] Testando conexão...\033[0m')
  connection = system(f'ping -c 1 -q {site} 1>/dev/null')

  if connection != 0:
    print ('\033[91m[✘] Site não responde\033[0m')
    exit()