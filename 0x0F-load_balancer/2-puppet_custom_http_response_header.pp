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
  path  => '/etc/nginx/sites-available/default',
  after => 'listen 80 default_server;',
  line  => '    location /redirect_me {return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;}',
}

exec { 'header':

command  => 'line_to_ad="\\\tadd_header X-Served-By \$hostname;\n" $$ sudo sed -i "23i $line_to_ad" /etc/nginx/sites-available/default',
provider => shell,
}

exec { 'restart server':
command  => 'sudo service nginx restart',
provider => shell,
}
