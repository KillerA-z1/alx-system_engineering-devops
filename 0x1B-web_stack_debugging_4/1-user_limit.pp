# Change the OS configuration so that it is possible to login with the
# holberton user and open a file without any error message.

# Puppet exec resource to modify the OS security configuration
exec {'OS security config':
  # Command to replace 'holberton' with 'foo' in /etc/security/limits.conf
  command => 'sed -i "s/holberton/foo/" /etc/security/limits.conf',
  # Specify the PATH environment variable for the command execution
  path    => '/usr/bin/env/:/bin/:/usr/bin/:/usr/sbin/'
}
