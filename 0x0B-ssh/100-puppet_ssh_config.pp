# This Puppet manifest file configures the SSH client on a system by modifying the ssh_config file.
# It uses the `file_line` resource type to add or modify specific lines in the ssh_config file.

# Resource: file_line { 'Declare identity file' }
#   - Path: Specifies the path to the ssh_config file.
#   - Ensure: Specifies whether the line should be present or absent in the file.
#   - Line: Specifies the line to be added or modified in the file. In this case, it declares the identity file as "~/.ssh/school".

# Resource: file_line { 'Turn off passwd auth' }
#   - Path: Specifies the path to the ssh_config file.
#   - Ensure: Specifies whether the line should be present or absent in the file.
#   - Line: Specifies the line to be added or modified in the file. In this case, it turns off password authentication.

file_line { 'Declare identity file':
	path    => '/etc/ssh/ssh_config',
	ensure  => 'present',
	line    => '    IdentityFile ~/.ssh/school',
}

file_line { 'Turn off passwd auth':
	path    => '/etc/ssh/ssh_config',
	ensure  => 'present',
	line    => '    PasswordAuthentication no',
}
