# Killing a process named killmenow:

exec { 'terminate_killmenow':
command => 'pkill -f killmenow',
onlyif  => 'pgrep -f killmenow',
path    => '/usr/bin'
}
