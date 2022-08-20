# Using Puppet, create a manifest that kills a process named killmenow.
exec { 'kill_process':
  path    => '/bin/:/urs/bin',
  command => 'pkill -f killmenow',
}
