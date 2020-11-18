[![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/f8al/TA-Shell.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/f8al/TA-Shell/context:python)

# TA-Shell
## Splunk scripted input for opening a backconnect shell on a remote forwarder

This app uses a variant of a python shellwritten by DaveK from TrustedSec in 2012, leveraged as a scripted input to have it execute the python code that will spawn a shell as the user splunk is running as.

This is useful when you need to make configuration changes to a host you have Deployment server access to, but not SSH/Remote management.

**All configuration is handled in ./etc/shell.conf**


### Please modify the config prior to intall, by default this is configured to use the following:


    [global]
    lhost: 127.0.0.1
    lport: 9997

To create the listener on the box you wish to connect back to run:
```bash
 nc -vv -l -p 9997
 ```
 
 Upon a successful connection you will see
 ```
 $ nc -vv -l -p 9997
listening on [any] 9997 ...
connect to [server] from ip24-252-37-155.om.om.cox.net [24.252.37.155] 64190
[*] Connection Established!
```
Ctrl+c to break connection
