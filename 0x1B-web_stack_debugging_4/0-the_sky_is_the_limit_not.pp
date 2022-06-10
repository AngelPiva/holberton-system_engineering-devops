# fixes amount of max requests permitted

exec { 'fix--for-nginx':
  command => 'sed -i "s/15/10000/" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin/'
}

exec { 'nginx restart':
  command => '/usr/sbin/service nginx restart'
}
