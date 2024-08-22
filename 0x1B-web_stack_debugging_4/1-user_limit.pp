# Change the OS configuration so that it is possible to login with the
# holberton user and open a file without any error message.

# Puppet exec resource to modify the OS security configuration
exec {'increase-file-descriptor-limit':
  # Command to increase the file descriptor limit for all users
  command  => 'echo "* soft nofile 65535\n* hard nofile 65535" >> /etc/security/limits.conf',
  # Specify the PATH environment variable for the command execution
  path     => '/usr/bin:/usr/sbin:/bin:/usr/local/bin',
  # Ensure the command is only run if the file descriptor limit is not already set
  unless   => 'grep -q "65535" /etc/security/limits.conf',
  provider => shell,
}
