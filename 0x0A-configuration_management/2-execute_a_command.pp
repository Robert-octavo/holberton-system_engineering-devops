# Using Puppet, create a manifest that kills a process named killmenow.
exec { 'kill_process':
  path    => '/urs/bin',
  command => 'pkill killmenow',
}
