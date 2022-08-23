# Change SSH config file
exec { 'file':
  command  => '/urs/bin/echo "    IdentityFile ~/.ssh/school" >> /etc/ssh/ssh_config',
  provider => 'shell',
}

exec { 'file2':
  command  => '/urs/bin/echo "    PasswordAuthentication no" >> /etc/ssh/ssh_config',
  provider => 'shell',
}
