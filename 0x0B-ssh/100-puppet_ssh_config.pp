# changing ssh config file using Puppet
# we will use file_line and it's not a built-in Puppet resource type
# so we should make sure that the module puppetlabs/stdlib is installed using "puppet module install puppetlabs/stdlib"
# and then we include stdlib in our puppet file

include stdlib

file_line {'ssh private key':
  path   => '/etc/ssh/ssh_config',
  line   => 'IdentityFile ~/.ssh/school',
  ensure => present,
}

file_line {'authenticate using a password set to no ':
  path   => '/etc/ssh/ssh_config',
  line   => 'PasswordAuthentication no',
  ensure => present,
}
