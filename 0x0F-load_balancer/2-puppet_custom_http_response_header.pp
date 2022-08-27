# to install nginx

$host = "add_header X-Served-by [${hostname}];"

exec {'update':
  provider => shell,
  command  => 'sudo apt-get -y update',
}

exec {'install':
  provider => shell,
  command  => 'sudo apt-get -y install nginx',
}

#package { 'nginx':a
#  ensure => installed,
#}

file_line { 'custom_header':
  ensure => 'present',
  path   => '/etc/nginx/sites-enabled/default',
  line   => $host,
}

#exec { 'file':
#  command  => 'sudo sed -i "/server_name _;/a \        add_header X-Served-By $host;" /etc/nginx/sites-enabled/default',
#  provider => shell,
#}

exec { 'restart-nginx':
  provider => shell,
  command  => 'sudo service nginx restart',
}
