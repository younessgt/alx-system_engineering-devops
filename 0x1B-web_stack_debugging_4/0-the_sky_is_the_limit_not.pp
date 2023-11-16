# puppet script that increase the limit of number open files

exec {'replace 15 with 4096':
  command => "sed -i 's/15/4096/' /etc/default/nginx",
  path    => ['/bin', '/usr/bin'],
}

-> exec {'restart nginx':
  command => 'service nginx restart',
  path    => ['/bin', '/usr/bin'],
}
