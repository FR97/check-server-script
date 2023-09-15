## Description

Small script which can be run inside crontab to check if Java process is running and if it is not to restart the server.

Example:

```text
* * * * * /usr/bin/python /path/to/file/check_server.py > /tmp/<log-file-name>.log 2>&1
```
