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


exec { 'header':
command  => 'line_to_ad="	add_header X-Served-By $hostname" && sudo sed -i "42i $line_to_ad" /etc/nginx/sites-available/default',
provider => shell,
}

exec { 'restart server':
command  => 'sudo service nginx restart',
provider => shell,
}
