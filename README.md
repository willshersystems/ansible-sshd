# Ansible OpenSSH Daemon Role

This role configures OpenSSH. It:

- Uses Ansible variables of the form `sshd_ListenAddress` for options
- Allows the use of booleans for keys with yes/no values, including those with additional non-boolean values such as `Compression`, which has the additional `delayed` option
- Tests the sshd_config before reloading sshd
- Template is programmatically generated. See the files in the meta folder.

It should cover all valid SSH options. 

This is the initial commit
