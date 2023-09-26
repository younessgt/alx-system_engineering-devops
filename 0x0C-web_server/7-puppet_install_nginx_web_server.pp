# using Puppet to install nginx and configure it

include stdlib

exec {'Update':
command  => 'sudo apt-get update',
provider => shell,
}

exec {'Install-nginx':
command  => 'sudo apt-get install -y nginx',
provider => shell,
}

file_line {'hello world':
ensure => present,
line   => 'Hello World!',
path   => '/var/www/html/index.nginx-debian.html',
}

exec {'301':
command  => 'sudo sed -i "42i \\\tlocation /redirect_me {\n\t\treturn 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;\n\t}\n" /etc/nginx/sites-available/default',
provider => present,
}

exec {'restart server':
command  => 'sudo service nginx restart',
provider => shell,
}
