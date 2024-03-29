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
command  => 'line_to_ad="\\\tadd_header X-Served-By \$hostname;\n" && sudo sed -i "46i $line_to_ad" /etc/nginx/nginx.conf',
provider => shell,
}

exec { 'restart server':
command  => 'sudo service nginx restart',
provider => shell,
}
