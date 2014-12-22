# Ansible OpenSSH Daemon Role

This role configures the OpenSSH daemon. It:

- By default configures the SSH daemon with the normal OS defaults. Defaults can be disabled by setting `sshd_skip_defaults: true`
- Supports use of a dict to configure items:

```yaml
sshd:
  Compression: delayed
  ListenAddress:
    - 0.0.0.0
```

- Can use scalars rather than a dict. Scalar values override dict values:

```yaml
sshd_Compression: off
```

- Correctly interprets booleans as yes and no in sshd configuration
- Supports lists for multi line configuration items
- Tests the sshd_config before reloading sshd
- Template is programmatically generated. See the files in the meta folder. It should cover all valid SSH options.
