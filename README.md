[![Build Status](https://travis-ci.org/WillsherSystems/ansible-sshd.svg?branch=master)](https://travis-ci.org/WillsherSystems/ansible-sshd) [![Ansible Galaxy](http://img.shields.io/badge/galaxy-willshersystems.sshd-660198.svg?style=flat)](https://galaxy.ansible.com/list#/roles/2488)


OpenSSH Server
==============

This role configures the OpenSSH daemon. It:

* By default configures the SSH daemon with the normal OS defaults.
* Works across a variety of UN*X like distributions
* Can be configured by dict or simple variables
* Supports Match sets
* Supports all sshd_config options. Templates are programmatically generated.
  (see [meta/make_option_list](meta/make_option_list))
* Tests the sshd_config before reloading sshd.

Requirements
------------

Tested on:

* Ubuntu precise, trusty
* Debian wheezy, jessie
* FreeBSD 10.1
* EL 6,7 derived distributions

It will likely work on other flavours and more direct support via suitable
[vars/](vars/) files is welcome.

Role variables
---------------

* Unconfigured, this role will provide a sshd_config that matches the OS default,
minus the comments and in a different order.

* Defaults can be disabled by setting `sshd_skip_defaults: true`

* Supports use of a dict to configure items:

```yaml
sshd:
  Compression: delayed
  ListenAddress:
    - 0.0.0.0
```

* Simple variables can be used rather than a dict. Simple values override dict
values:

```yaml
sshd_Compression: off
```

* Correctly interprets booleans as yes and no in sshd configuration
* Supports lists for multi line configuration items:

```yaml
sshd_ListenAddress:
  - 0.0.0.0
  - '::'
```

* Supports match section either via Match in the sshd dict, sshd_match and any of sshd_match_1 through sshd_match_9. Match items can either be a dict or an array.

Example Playbook
----------------

```yaml
---
- hosts: all
  vars:
    sshd_skip_defaults: true
    sshd:
      Compression: true
      ListenAddress:
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
  roles:
    - role: willshersystems.sshd
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

License
-------

LGPLv3


Author
------

Matt Willsher <matt@willsher.systems>

Copyright 2014,2015 Willsher Systems
