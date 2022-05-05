# fix too many files error
exec { 'config nginx':
  command  => 'sed -i -e "s/-n 15/-n 4096/" /etc/default/nginx; service nginx restart',
  provider => shell,
}
