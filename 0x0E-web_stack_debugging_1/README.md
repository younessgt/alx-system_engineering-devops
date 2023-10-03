this directory is for web_stack_debugging_1

note: To enable for example a configuration in /etc/nginx/sites-available/default1 you should create a symbolic link(symlink)
from sites-available to sites-enabled  using ```sudo ln -s /etc/nginx/sites-available/default1 /etc/nginx/sites-enabled/```

and to desactivate a configuartion we use
```sudo rm /etc/nginx/sites-enabled/default1```
