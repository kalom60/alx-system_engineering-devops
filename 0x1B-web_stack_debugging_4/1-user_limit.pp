# Fix problem of high amount files opened

exec {'increase-hard-file-limit':
  provider => shell,
  command  => 'sudo sed -i "s/nofile 5/nofile 50000/" /etc/security/limits.conf',
  before   => Exec['increase-soft-file-limit'],
}

exec {'increase-soft-file-limit':
  provider => shell,
  command  => 'sudo sed -i "s/nofile 4/nofile 40000/" /etc/security/limits.conf',
}
