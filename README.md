# TA-Shell
Splunk scripted input for opening a backconnect shell on a remote forwarder

This app uses a variant of the "undetectable" backconnect python shell from TrustedSec,
leveraged as a scripted input to have it execute the python code that will spawn a shell as the user splunk is running as.
All configuration is handled in ./etc/shell.conf

Needed configuration variables are the LPORT and LHOST for where the netcat listener is running for the backconnect to attach.
