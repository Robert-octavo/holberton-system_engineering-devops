# Change SSH config file
exec { 'file':
  command  => '/urs/bin/echo "    IdentityFile ~/.ssh/school\n    PasswordAuthentication no" >> /etc/ssh/ssh_config',
  provider => 'shell',
}
