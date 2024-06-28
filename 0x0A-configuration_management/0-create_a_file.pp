# This Puppet manifest creates a file named 'school' in the '/tmp' directory.
# The file has the content 'I love Puppet' and the permissions are set to '0744'.
# The owner and group of the file are set to 'www-data'.
file { '/tmp/school':
    ensure  => 'file',
    content => 'I love Puppet',
    mode    => '0744',
    owner   => 'www-data',
    group   => 'www-data',
}
