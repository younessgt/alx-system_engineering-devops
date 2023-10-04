this directory is for web_stack_debugging_1

Note 0: To enable for example a configuration in /etc/nginx/sites-available/default1 you should create a symbolic link(symlink)
from sites-available to sites-enabled  using ```sudo ln -s /etc/nginx/sites-available/default1 /etc/nginx/sites-enabled/default1```

and to desactivate a configuartion we use
```sudo rm /etc/nginx/sites-enabled/default1```

Note 1: when using pkill to terminate a worker process the command ```service nginx status ``` don/t provide real-time status info and may not reflect the actual running state
