# login with holberton user without any error message

exec {'changing soft and hard nofile':
  command => "sed -i 's/nofile \+[0-9]\+/nofile 6000/g' /etc/security/limits.conf",
  path    => ['/bin', '/usr/bin'],
}
