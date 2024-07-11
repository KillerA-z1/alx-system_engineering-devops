#!/usr/bin/env bash
# install and configure nginx

exec { 'update':
  command     => '/usr/bin/apt-get update',
  path        => '/usr/bin:/bin:/usr/sbin:/sbin',
  logoutput   => true,
  refreshonly => true,
}

package { 'nginx':
  ensure  => installed,
  require => Exec['update'],
}

file_line { 'header_served_by':
  path    => '/etc/nginx/sites-available/default',
  match   => '^server {',
  line    => "server {\n\tadd_header X-Served-By \"${::hostname}\";",
  require => Package['nginx'],
  notify  => Exec['restart_nginx'],
}

exec { 'restart_nginx':
  command     => '/usr/sbin/service nginx restart',
  refreshonly => true,
}
