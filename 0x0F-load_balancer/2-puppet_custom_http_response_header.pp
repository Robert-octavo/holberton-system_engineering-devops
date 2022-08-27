# to install nginx
exec {'update':
  provider => shell,
  command  => 'sudo apt-get -y update',
}

package { 'nginx':
  ensure => installed,
}

#file_line { 'custom_header':
#  ensure => 'present',
#  path   => '/etc/nginx/sites-enabled/default',
#  line   => 'add_header X-Served-By ${HOSTNAME};',
#}

exec { 'file':
  command  => 'sudo sed -i "/server_name _;/a \        add_header X-Served-By ${HOSTNAME};" /etc/nginx/sites-enabled/default',
  provider => 'shell',
}

service { 'nginx':
  ensure  => running,
  require => Package['nginx'],
}
