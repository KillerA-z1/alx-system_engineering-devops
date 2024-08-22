# Puppet manifest to modify Nginx request limit and restart the Nginx service

# Change requests limit
exec { 'sed -i s/15/2000/g /etc/default/nginx':
  # Specify the PATH environment variable for the command execution
  path     => '/usr/bin:/usr/sbin:/bin',
  # Use the shell provider to execute the command
  provider => shell,
}

# Restart the Nginx service
exec { 'sudo service nginx restart':
  # Specify the PATH environment variable for the command execution
  path     => '/usr/bin:/usr/sbin:/bin',
  # Use the shell provider to execute the command
  provider => shell,
}
