# Change the OS configuration so that it is possible to login
# with the holberton user and open a file without any error message.

exec { 'change-os-configuration-for-holberton-user':
  command => 'sed -i "s/hard nofile 5/hard nofile 1000/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/'
}

exec { 'change-os-configuration-for-holberton-user-soft':
  command => 'sed -i "s/soft nofile 4/soft nofile 1000/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/'
}
