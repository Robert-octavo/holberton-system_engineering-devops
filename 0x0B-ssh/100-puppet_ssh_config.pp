# Change SSH config file
file {'/etc/ssh/ssh_config':
  ensure => 'present',
}
exec { 'file':
  command  => '/usr/bin/echo "    IdentityFile ~/.ssh/school\n    PasswordAuthentication no" >> /etc/ssh/ssh_config',
  provider => 'shell',
}
