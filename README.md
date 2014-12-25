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
- Supports lists for multi line configuration items:

```yaml
sshd_ListenAddress:
  - 0.0.0.0
  - ::
```

- Tests the sshd_config before reloading sshd
- Template is programmatically generated. See the files in the meta folder. It should cover all valid SSH options. To regenerate the template, in the meta directory run `./make_option_list  >../templates/sshd_config.j2`
- Supports match section either via Match in the sshd dict, sshd_match and any of sshd_match_1 through sshd_match_9. Match items can either be a dict or an array.

## Complete example

```yaml
---
sshd_skip_defaults: true
sshd:
  Compression: true
  ListenAddres:
    - "0.0.0.0"
    - "::"
  GSSAPIAuthentication: no
  Match:
    - Condition: "Group user"
      GSSAPIAuthentication: yes
sshd_UsePrivilegeSeparation: sandbox
sshd_match:
    - Condition: "Group xusers"
      X11Forwarding: yes
```

Results in:

```
# Ansible managed: ...
Compression yes
GSSAPIAuthentication no
UsePrivilegeSeparation sandbox
Match Group user
  GSSAPIAuthentication yes
Match Group xusers
  X11Forwarding yes
```
