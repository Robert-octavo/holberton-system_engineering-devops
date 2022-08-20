# Using Puppet, create a file in /tmp
file { 'school':
  ensure  => present,
  path    => '/tmp/school',
  owner   => 'www-data',
  group   => 'www-data',
  mode    => '0744',
  content => 'I Love Puppet',
}
