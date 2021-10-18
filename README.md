OpenSSH Server
==============

[![Ansible Lint](https://github.com/willshersystems/ansible-sshd/actions/workflows/ansible-lint.yml/badge.svg)](https://github.com/willshersystems/ansible-sshd/actions/workflows/ansible-lint.yml)
[![Ansible Galaxy](http://img.shields.io/badge/galaxy-willshersystems.sshd-660198.svg?style=flat)](https://galaxy.ansible.com/willshersystems/sshd/)

This role configures the OpenSSH daemon. It:

* By default configures the SSH daemon with the normal OS defaults.
* Works across a variety of `UN*X` distributions
* Can be configured by dict or simple variables
* Supports Match sets
* Supports all `sshd_config` options. Templates are programmatically generated.
  (see [`meta/make_option_lists`](meta/make_option_lists))
* Tests the `sshd_config` before reloading sshd.

**WARNING** Misconfiguration of this role can lock you out of your server!
Please test your configuration and its interaction with your users configuration
before using in production!

**WARNING** Digital Ocean allows root with passwords via SSH on Debian and
Ubuntu. This is not the default assigned by this module - it will set
`PermitRootLogin without-password` which will allow access via SSH key but not
via simple password. If you need this functionality, be sure to set
`sshd_PermitRootLogin yes` for those hosts.

Requirements
------------

Tested on:

* Ubuntu precise, trusty, xenial, bionic, focal
  * [![Run tests on Ubuntu latest](https://github.com/willshersystems/ansible-sshd/actions/workflows/ansible-ubuntu.yml/badge.svg)](https://github.com/willshersystems/ansible-sshd/actions/workflows/ansible-ubuntu.yml)
* Debian wheezy, jessie, stretch, buster, bullseye
  * [![Run tests on Debian bullseye (11)](https://github.com/willshersystems/ansible-sshd/actions/workflows/ansible-debian-bullseye.yml/badge.svg)](https://github.com/willshersystems/ansible-sshd/actions/workflows/ansible-debian-bullseye.yml)
  * [![Run tests on Debian buster (10)](https://github.com/willshersystems/ansible-sshd/actions/workflows/ansible-debian-buster.yml/badge.svg)](https://github.com/willshersystems/ansible-sshd/actions/workflows/ansible-debian-buster.yml)
  * [![Run tests on Debian stretch (9)](https://github.com/willshersystems/ansible-sshd/actions/workflows/ansible-debian-stretch.yml/badge.svg)](https://github.com/willshersystems/ansible-sshd/actions/workflows/ansible-debian-stretch.yml)
* EL 6, 7, 8, 9 derived distributions
  * [![Run tests on CentOS 8](https://github.com/willshersystems/ansible-sshd/actions/workflows/ansible-centos8.yml/badge.svg)](https://github.com/willshersystems/ansible-sshd/actions/workflows/ansible-centos8.yml)
  * [![Run tests on CentOS 7](https://github.com/willshersystems/ansible-sshd/actions/workflows/ansible-centos7.yml/badge.svg)](https://github.com/willshersystems/ansible-sshd/actions/workflows/ansible-centos7.yml)
  * [![Run tests on CentOS 6](https://github.com/willshersystems/ansible-sshd/actions/workflows/ansible-centos6.yml/badge.svg)](https://github.com/willshersystems/ansible-sshd/actions/workflows/ansible-centos6.yml)
* Fedora 31, 32, 33, 34
  * [![Run tests on Fedora latest](https://github.com/willshersystems/ansible-sshd/actions/workflows/ansible-fedora.yml/badge.svg)](https://github.com/willshersystems/ansible-sshd/actions/workflows/ansible-fedora.yml)
* FreeBSD 10.1
* OpenBSD 6.0
* AIX 7.1, 7.2

It will likely work on other flavours and more direct support via suitable
[vars/](vars/) files is welcome.

Role variables
---------------

Unconfigured, this role will provide a `sshd_config` that matches the OS default,
minus the comments and in a different order.

* `sshd_enable`

If set to *false*, the role will be completely disabled. Defaults to *true*.

* `sshd_skip_defaults`

If set to *true*, don't apply default values. This means that you must have a
complete set of configuration defaults via either the `sshd` dict, or
`sshd_Key` variables. Defaults to *false* unless `sshd_config_namespace` is
set.

* `sshd_manage_service`

If set to *false*, the service/daemon won't be **managed** at all, i.e. will not
try to enable on boot or start or reload the service.  Defaults to *true*
unless: Running inside a docker container (it is assumed ansible is used during
build phase) or AIX (Ansible `service` module does not currently support `enabled`
for AIX)

* `sshd_allow_reload`

If set to *false*, a reload of sshd wont happen on change. This can help with
troubleshooting. You'll need to manually reload sshd if you want to apply the
changed configuration. Defaults to the same value as `sshd_manage_service`.
(Except on AIX, where `sshd_manage_service` is default *false*, but
`sshd_allow_reload` is default *true*)

* `sshd_install_service`

If set to *true*, the role will install service files for the ssh service.
Defaults to *false*.

The templates for the service files to be used are pointed to by the variables

  - `sshd_service_template_service` (__default__: `templates/sshd.service.j2`)
  - `sshd_service_template_at_service` (__default__: `templates/sshd@.service.j2`)
  - `sshd_service_template_socket` (__default__: `templates/sshd.socket.j2`)

Using these variables, you can use your own custom templates. With the above
default templates, the name of the installed ssh service will be provided by
the `sshd_service` variable.

* `sshd`

A dict containing configuration.  e.g.

```yaml
sshd:
  Compression: delayed
  ListenAddress:
    - 0.0.0.0
```

* `sshd_...`

Simple variables can be used rather than a dict. Simple values override dict
values. e.g.:

```yaml
sshd_Compression: off
```

In all cases, booleans are correctly rendered as yes and no in sshd
configuration. Lists can be used for multiline configuration items. e.g.

```yaml
sshd_ListenAddress:
  - 0.0.0.0
  - '::'
```

Renders as:

```
ListenAddress 0.0.0.0
ListenAddress ::
```

* `sshd_match`, `sshd_match_1` through `sshd_match_9`

A list of dicts or just a dict for a Match section. Note, that these variables
do not override match blocks as defined in the `sshd` dict. All of the sources
will be reflected in the resulting configuration file.

* `sshd_backup`

When set to *false*, the original `sshd_config` file is not backed up. Default
is *true*.

* `sshd_sysconfig`

On RHEL-based systems, sysconfig is used for configuring more details of sshd
service. If set to *true*, this role will manage also the `/etc/sysconfig/sshd`
configuration file based on the following configuration. Default is *false*.

* `sshd_sysconfig_override_crypto_policy`

In RHEL8-based systems, this can be used to override system-wide crypto policy
by setting to *true*. Defaults to *false*.

* `sshd_sysconfig_use_strong_rng`

In RHEL-based systems, this can be used to force sshd to reseed openssl random
number generator with the given amount of bytes as an argument. The default is
*0*, which disables this functionality. It is not recommended to turn this on
if the system does not have hardware random number generator.

* `sshd_config_file`

The path where the openssh configuration produced by this role should be saved.
This is useful mostly when generating configuration snippets to Include.

* `sshd_config_namespace`

By default (*null*), the role defines whole content of the configuration file
including system defaults. You can use this variable to invoke this role from
other roles or from multiple places in a single playbook on systems that do not
support drop-in directory. The `sshd_skip_defaults` is ignored and no system
defaults are used in this case.

When this variable is set, the role places the configuration that you specify
to configuration snippets in a existing configuration file under the given
namespace. You need to select different namespaces when invoking the role
several times.

Note that limitations of the openssh configuration file still apply. For
example, only the first option specified in a configuration file is effective
for most of the variables.

Technically, the role places snippets in `Match all` blocks, unless they contain
other match blocks, to ensure they are applied regardless of the previous match
blocks in the existing configuration file. This allows configuring any
non-conflicting options from different roles invocations.

* `sshd_config_owner`, `sshd_config_group`, `sshd_config_mode`

Use these variables to set the ownership and permissions for the openssh config
file that this role produces.

* `sshd_verify_hostkeys`

By default (*auto*), this list contains all the host keys that are present in
the produced configuration file. The paths are checked for presence and
generated if missing. Additionally, permissions and file owners are set to sane
defaults. This is useful if the role is used in deployment stage to make sure
the service is able to start on the first attempt. To disable this check, set
this to empty list.

* `sshd_hostkey_owner`, `sshd_hostkey_group`, `sshd_hostkey_mode`

Use these variables to set the ownership and permissions for the host keys from
the above list.

### Secondary role variables

These variables are used by the role internals and can be used to override the
defaults that correspond to each supported platform.

* `sshd_packages`

Use this variable to override the default list of packages to install.

* `sshd_binary`

The path to the openssh executable

* `sshd_service`

The name of the openssh service. By default, this variable contains the name of
the ssh service that the target platform uses. But it can also be used to set
the name of the custom ssh service when the `sshd_install_service` variable is
used.

* `sshd_sftp_server`

Default path to the sftp server binary.

### Variables Exported by the Role

* `sshd_has_run`

This variable is set to *true* after the role was successfully executed.

Dependencies
------------

None

Example Playbook
----------------

**DANGER!** This example is to show the range of configuration this role
provides. Running it will likely break your SSH access to the server!

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
    sshd_UsePrivilegeSeparation: no
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
UsePrivilegeSeparation no
Match Group user
  GSSAPIAuthentication yes
Match Group xusers
  X11Forwarding yes
```

Since Ansible 2.4, the role can be invoked using `include_role` keyword,
for example:

```yaml
---
- hosts: all
  become: true
  tasks:
  - name: "Configure sshd"
    include_role:
      name: willshersystems.sshd
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
      sshd_UsePrivilegeSeparation: no
      sshd_match:
          - Condition: "Group xusers"
            X11Forwarding: yes
```

You can just add a configuration snippet with the `sshd_config_namespace`
option:
```
---
- hosts: all
  tasks:
  - name: Configure sshd to accept some useful environment variables
    include_role:
      name: ansible-sshd
    vars:
      sshd_config_namespace: accept-env
      sshd:
        # there are some handy environment variables to accept
        AcceptEnv:
          LANG
          LS_COLORS
          EDITOR
```
The following snippet will be added to the default configuration file
(if not yet present):
```
# BEGIN sshd system role managed block: namespace accept-env
Match all
  AcceptEnv LANG LS_COLORS EDITOR
# END sshd system role managed block: namespace accept-env
```


More example playbooks can be found in [`examples/`](examples/) directory.

Template Generation
-------------------

The [`sshd_config.j2`](templates/sshd_config.j2) template is programatically
generated by the scripts in meta. New options should be added to the
`options_body` or `options_match`.

To regenerate the template, from within the meta/ directory run:
`./make_option_lists`

License
-------

LGPLv3


Author
------

Matt Willsher <matt@willsher.systems>

&copy; 2014,2015 Willsher Systems Ltd.
