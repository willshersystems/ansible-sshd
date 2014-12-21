# Ansible OpenSSH Daemon Role

This role configures OpenSSH. It:

- By default, with no set options, creates an empty configuration file.
- Can use a dict of the form:
```
sshd:
  Compression: delayed
  ListenAddress:
    - 0.0.0.0
    - ::
```
- Can also use scalar variables of the form `sshd_ListenAddress`
- Scalar override dict values.
- Allows the use of booleans for keys with yes/no values, including those with additional non-boolean values such as `Compression`, which has the additional `delayed` option
- Tests the sshd_config before reloading sshd
- Template is programmatically generated. See the files in the meta folder.

It should cover all valid SSH options.
