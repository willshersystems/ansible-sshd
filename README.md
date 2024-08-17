# OpenSSH Server

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

## Requirements

Tested on:

* Ubuntu precise, trusty, xenial, bionic, focal, jammy, noble
  * [![Run tests on Ubuntu latest](https://github.com/willshersystems/ansible-sshd/actions/workflows/ansible-ubuntu.yml/badge.svg)](https://github.com/willshersystems/ansible-sshd/actions/workflows/ansible-ubuntu.yml)
* Debian wheezy, jessie, stretch, buster, bullseye, bookworm
  * [![Run tests on Debian](https://github.com/willshersystems/ansible-sshd/actions/workflows/ansible-debian-check.yml/badge.svg)](https://github.com/willshersystems/ansible-sshd/actions/workflows/ansible-debian-check.yml)
* EL 6, 7, 8, 9, 10 derived distributions
  * [![Run tests on CentOS](https://github.com/willshersystems/ansible-sshd/actions/workflows/ansible-centos-check.yml/badge.svg)](https://github.com/willshersystems/ansible-sshd/actions/workflows/ansible-centos-check.yml)
* All Fedora
  * [![Run tests on Fedora latest](https://github.com/willshersystems/ansible-sshd/actions/workflows/ansible-fedora.yml/badge.svg)](https://github.com/willshersystems/ansible-sshd/actions/workflows/ansible-fedora.yml)
* Latest Alpine
  * [![Run tests on Alpine](https://github.com/willshersystems/ansible-sshd/actions/workflows/ansible-alpine.yml/badge.svg)](https://github.com/willshersystems/ansible-sshd/actions/workflows/ansible-alpine.yml)
* FreeBSD 10.1
* OpenBSD 6.0
* AIX 7.1, 7.2
* OpenWrt 21.03

It will likely work on other flavours and more direct support via suitable
[vars/](vars/) files is welcome.

### Optional requirements

If you want to use advanced functionality of this role that can configure
firewall and selinux for you, which is mostly useful when custom port is used,
the role requires additional collections which are specified in
`meta/collection-requirements.yml`. These are not automatically installed.
If you want to manage `rpm-ostree` systems, additional collections are required.
You must install them like this:

```bash
ansible-galaxy install -vv -r meta/collection-requirements.yml
```

For more information, see `sshd_manage_firewall` and `sshd_manage_selinux`
options below, and the `rpm-ostree` section.  This additional functionality is
supported only on Red Hat based Linux.

## Role variables

### Primary role variables

Unconfigured, this role will provide a `sshd_config` that matches the OS default,
minus the comments and in a different order.

#### sshd_enable

If set to *false*, the role will be completely disabled. Defaults to *true*.

#### sshd_skip_defaults

If set to *true*, don't apply default values. This means that you must have a
complete set of configuration defaults via either the `sshd` dict, or
`sshd_Key` variables. Defaults to *false* unless `sshd_config_namespace` is
set or `sshd_config_file` points to a drop-in directory to avoid recursive include.

#### sshd_manage_service

If set to *false*, the service/daemon won't be **managed** at all, i.e. will not
try to enable on boot or start or reload the service.  Defaults to *true*
unless: Running inside a docker container (it is assumed ansible is used during
build phase) or AIX (Ansible `service` module does not currently support `enabled`
for AIX)

#### sshd_allow_reload

If set to *false*, a reload of sshd won't happen on change. This can help with
troubleshooting. You'll need to manually reload sshd if you want to apply the
changed configuration. Defaults to the same value as `sshd_manage_service`.
(Except on AIX, where `sshd_manage_service` is default *false*, but
`sshd_allow_reload` is default *true*)

#### sshd_install_service

If set to *true*, the role will install service files for the ssh service.
Defaults to *false*.

The templates for the service files to be used are pointed to by the variables

* `sshd_service_template_service` (**default**: `templates/sshd.service.j2`)
* `sshd_service_template_at_service` (**default**: `templates/sshd@.service.j2`)
* `sshd_service_template_socket` (**default**: `templates/sshd.socket.j2`)

Using these variables, you can use your own custom templates. With the above
default templates, the name of the installed ssh service will be provided by
the `sshd_service` variable.

#### sshd_manage_firewall

If set to *true*, the SSH port(s) will be opened in firewall. Note, this
works only on Red Hat based OS. The default is *false*.

NOTE: `sshd_manage_firewall` is limited to *adding* ports. It cannot be used
for *removing* ports. If you want to remove ports, you will need to use the
firewall system role directly.

#### sshd_manage_selinux

If set to *true*, the selinux will be configured to allow sshd listening
on the given SSH port(s). Note, this works only on Red Hat based OS.
The default is *false*.

NOTE: `sshd_manage_selinux` is limited to *adding* policy. It cannot be used
for *removing* policy. If you want to remove ports, you will need to use the
selinux system role directly.

#### sshd

A dict containing configuration.  e.g.

```yaml
sshd:
  Compression: delayed
  ListenAddress:
    - 0.0.0.0
```

#### sshd_`<OptionName>`

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

```text
ListenAddress 0.0.0.0
ListenAddress ::
```

#### sshd_match, sshd_match_1 through sshd_match_9

A list of dicts or just a dict for a Match section. Note, that these variables
do not override match blocks as defined in the `sshd` dict. All of the sources
will be reflected in the resulting configuration file. The use of
`sshd_match_*` variant is deprecated and no longer recommended.

#### sshd_backup

When set to *false*, the original `sshd_config` file is not backed up. Default
is *true*.

#### sshd_sysconfig

On RHEL-based systems, sysconfig is used for configuring more details of sshd
service. If set to *true*, this role will manage also the `/etc/sysconfig/sshd`
configuration file based on the following configurations. Default is *false*.

#### sshd_sysconfig_override_crypto_policy

In RHEL8-based systems, this can be used to override system-wide crypto policy
by setting to *true*. Without this option, changes to ciphers, MACs, public
key algorithms will have no effect on the resulting service in RHEL8. Defaults
to *false*.

#### sshd_sysconfig_use_strong_rng

In RHEL-based systems (before RHEL9), this can be used to force sshd to reseed
openssl random number generator with the given amount of bytes as an argument.
The default is *0*, which disables this functionality. It is not recommended to
turn this on if the system does not have hardware random number generator.

#### sshd_config_file

The path where the openssh configuration produced by this role should be saved.
This is useful mostly when generating configuration snippets to Include from
drop-in directory (default in Fedora and RHEL9).

When this path points to a drop-in directory (like
`/etc/ssh/sshd_config.d/00-custom.conf`), the main configuration file (defined
with the variable `sshd_main_config_file`) is checked to contain a proper
`Include` directive.

#### sshd_main_config_file

When the system is using drop-in directory, this option can be used to set
a path to the main configuration file and let you configure only the drop-in
configuration file using `sshd_config_file`. This is useful in cases when
you need to configure second independent sshd service with different
configuration file. This is also the file used in the service file.

On systems without drop-in directory, it defaults to `None`. Otherwise it
defaults to `/etc/ssh/sshd_config`. When the `sshd_config_file` is set
outside of the drop in directory (its parent directory is not
`sshd_main_config_file` ~ '.d'), this variable is ignored.

#### sshd_config_namespace

By default (*null*), the role defines whole content of the configuration file
including system defaults. You can use this variable to invoke this role from
other roles or from multiple places in a single playbook as an alternative to
using a drop-in directory. The `sshd_skip_defaults` is ignored and no system
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

#### sshd_config_owner, sshd_config_group, sshd_config_mode

Use these variables to set the ownership and permissions for the openssh
configuration file that this role produces.

#### sshd_verify_hostkeys

By default (*auto*), this list contains all the host keys that are present in
the produced configuration file. If there are none, the OpenSSH default list
will be used after excluding non-FIPS approved keys in FIPS mode. The paths
are checked for presence and new keys are generated if they are missing.
Additionally, permissions and file owners are set to sane defaults. This is
useful if the role is used in deployment stage to make sure the service is
able to start on the first attempt.

To disable this check, set this to empty list.

#### sshd_hostkey_owner, sshd_hostkey_group, sshd_hostkey_mode

Use these variables to set the ownership and permissions for the host keys from
the above list.

### Secondary role variables

These variables are used by the role internals and can be used to override the
defaults that correspond to each supported platform. They are not tested and
generally are not needed as the role will determine them from the OS type.

#### sshd_packages

Use this variable to override the default list of packages to install.

#### sshd_binary

The path to the openssh executable

#### sshd_service

The name of the openssh service. By default, this variable contains the name of
the ssh service that the target platform uses. But it can also be used to set
the name of the custom ssh service when the `sshd_install_service` variable is
used.

#### sshd_sftp_server

Default path to the sftp server binary.

### Variables Exported by the Role

#### sshd_has_run

This variable is set to *true* after the role was successfully executed.

## Configure SSH certificate authentication

To configure SSH certificate authentication on your SSH server, you need to provide at least the trusted user CA key, which will be used to validate client certificates against.
This is done with the `sshd_trusted_user_ca_keys_list` variable.

If you need to map some of the authorized principals to system users, you can do that using the `sshd_principals` variable.

### Additional variables

#### sshd_trusted_user_ca_keys_list

List of the trusted user CA public keys in OpenSSH (one-line) format (mandatory).

#### sshd_trustedusercakeys_directory_owner, shsd_trustedusercakeys_directory_group, sshd_trustedusercakeys_directory_mode

Use these variables to set the ownership and permissions for the Trusted User CA Keys directory. Defaults are respectively *root*, *root* and *0755*.

#### sshd_trustedusercakeys_file_owner, shsd_trustedusercakeys_file_group, sshd_trustedusercakeys_file_mode

Use these variables to set the ownership and permissions for the Trusted User CA Keys file. Defaults are respectively *root*, *root* and *0640*.

#### sshd_principals

A dict containing principals for users in the os (optional). e.g.

```yaml
sshd_principals:
  admin:
    - frontend-admin
    - backend-admin
  somelinuxuser:
    - some-principal-defined-in-certificate
```

#### sshd_authorizedprincipals_directory_owner, shsd_authorizedprincipals_directory_group, sshd_authorizedprincipals_directory_mode

Use these variables to set the ownership and permissions for the Authorized Principals directory. Defaults are respectively *root*, *root* and *0755*.

#### sshd_authorizedprincipals_file_owner, shsd_authorizedprincipals_file_group, sshd_authorizedprincipals_file_mode

Use these variables to set the ownership and permissions for the Authorized Principals file. Defaults are respectively *root*, *root* and *0644*.

### Additional configuration

The SSH server needs this information stored in files so in addition to the above variables, respective configuration options `TrustedUserCAKeys` (mandatory) and `AuthorizedPrincipalsFile` (optional) need to be present the `sshd` dictionary when invoking the role. For example:

```yaml
sshd:
  TrustedUserCAKeys: /etc/ssh/path-to-trusted-user-ca-keys/trusted-user-ca-keys.pub
  AuthorizedPrincipalsFile: "/etc/ssh/path-to-auth-principals/auth_principals/%u"
```

To learn more about SSH Certificates, here is a [nice tutorial to pure SSH certificates, from wikibooks](https://en.wikibooks.org/wiki/OpenSSH/Cookbook/Certificate-based_Authentication).

To understand principals and to set up SSH certificates with Vault, this is a [well-explained tutorial from Hashicorp](https://www.hashicorp.com/blog/managing-ssh-access-at-scale-with-hashicorp-vault).

## Dependencies

None

For tests, the `ansible.posix` collection is required for the `mount` role to
emulate FIPS mode.

## Example Playbook

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
      GSSAPIAuthentication: false
      Match:
        - Condition: "Group user"
          GSSAPIAuthentication: true
    sshd_UsePrivilegeSeparation: false
    sshd_match:
        - Condition: "Group xusers"
          X11Forwarding: true
  roles:
    - role: willshersystems.sshd
```

Results in:

```text
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
        GSSAPIAuthentication: false
        Match:
          - Condition: "Group user"
            GSSAPIAuthentication: true
      sshd_UsePrivilegeSeparation: false
      sshd_match:
          - Condition: "Group xusers"
            X11Forwarding: true
```

You can just add a configuration snippet with the `sshd_config_namespace`
option:

```yaml
---
- hosts: all
  tasks:
  - name: Configure sshd to accept some useful environment variables
    include_role:
      name: willshersystems.sshd
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

```text
# BEGIN sshd system role managed block: namespace accept-env
Match all
  AcceptEnv LANG LS_COLORS EDITOR
# END sshd system role managed block: namespace accept-env
```

More example playbooks can be found in [`examples/`](examples/) directory.

## Template Generation

The [`sshd_config.j2`](templates/sshd_config.j2) and
[`sshd_config_snippet.j2`](templates/sshd_config_snippet.j2) templates are
programmatically generated by the scripts in meta. New options should be added
to the `options_body` and/or `options_match`.

To regenerate the templates, from within the `meta/` directory run:
`./make_option_lists`

## rpm-ostree

See README-ostree.md

## License

LGPLv3

## Authors

Matt Willsher <matt@willsher.systems>

&copy; 2014,2015 Willsher Systems Ltd.

Jakub Jelen <jjelen@redhat.com>

&copy; 2020 - 2024 Red Hat, Inc.
