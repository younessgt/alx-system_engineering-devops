# using Puppet to install nginx and configure it

include stdlib

exec { 'Update':
command  => 'sudo apt-get update',
provider => shell,
}

exec { 'Install-nginx':
command  => 'sudo apt-get install -y nginx',
provider => shell,
}

file_line { 'hello world':
ensure => present,
line   => 'Hello World!',
path   => '/var/www/html/index.nginx-debian.html',
}

file_line { '301':
  path   => '/etc/nginx/sites-available/default',
  after  => 'listen 80 default_server;',
  line   => '    location /redirect_me {return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;}',
}

exec { 'restart server':
command  => 'sudo service nginx restart',
provider => shell,
}
