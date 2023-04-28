Changelog
=========

[v0.19.0] - 2023-04-27

### New Features

- feat: add support for FreeBSD, OpenBSD

### Bug Fixes

- none

### Other Changes

- test: skip selinux or firewall role test where not supported
- test: check generated files for ansible_managed, fingerprint
- ci: Add commitlint GitHub action to ensure conventional commits
- ci: Drop testing on Debian stretch (9)
- ci: add dependabot check for github action updates
- style: ansible-lint - align with current Ansible recommendations

[v0.18.2] - 2023-04-06
--------------------

### New Features

- none

### Bug Fixes

- Fedora 38 has no longer non-standard hostkey permissions

### Other Changes

- Fingerprint ansible-sshd managed config files
    
[v0.18.1] - 2023-01-17
--------------------

### New Features

 - Add support for Alpine OS (#212)
 - Add support for managing selinux and firewall on RHEL-based systems (#211)

### Bug Fixes

 - Update tests to not use configuration options available in system defaults (#213)
 - Improve manual pages processing in tests to accommodate Alpine's busybox man (#213)

### Other Changes

 - Add a Github action to check for non-inclusive language (#215)

[v0.18.0] - 2022-09-27
--------------------

### New Features

- Adding support for OpenWrt 21.03

- Add final version of RequiredRSASize

Keep the old version for backward compatibility

Upstream commit:
https://github.com/openssh/openssh-portable/commit/1875042c

### Bug Fixes

- Update source template to match generated files

### Other Changes

- Remove legacy files

- Update pre-commit plugins to latest

- Linting fixes

- keep v prefix in version/tag

Keep the `v` prefix in the version/tag

[v0.17.0] - 2022-08-31
--------------------

### New Features

- Make drop-in config file functionality configurable by user

This PR simplifies the logic behind the drop-in config files and also
allows the user to use drop-in configs even if the distribution does not
support it out of the box.

### Bug Fixes

- Allow user to override variables

A previous commit hardcoded many variables to the values under vars/,
making it impossible for the user to parameterize things like the systemd
service name. The assumption was that the __sshd_* variables were useless
in an effort to blindly adhere to best practices, but they were crucial in
allowing flexibility to the user.

### Other Changes

- none

[v0.16.1] - 2022-07-28
--------------------

### New Features

- add parameter RSAMinSize

Add support for the new RSAMinSize parameter.

### Bug Fixes

- Ensure values are cast to correct type

https://github.com/willshersystems/ansible-sshd/issues/188
This shouldn't be necessary, but there seems no way to
guarantee using a version of Jinja which doesn't have this
problem.

In addition - it is not good practice to compare values to
`true` or `false` - instead, just ensure the value is a `bool`
type and evaluate in a boolean context.

### Other Changes

- Addition notes about secondary variables
- Fix various linting issues
- Revert incorrect module name
- tests: Do not be picky about spaces/tabs

When testing with cloud-init, it modifies the sshd_configuration and can
replace some tabs with whitespaces. This happens frequently around the
subsystem keyword. There are no functional changes, but the matching
did not work as expected.

Signed-off-by: Jakub Jelen <jjelen@redhat.com>

- the role still supports ansible 2.9

- Add CHANGELOG.md

- Add changelog_to_tag.yml to .github/workflows

Description:
When a new changelog section is added to CHANGELOG.md and pushed,
changelog_to_tag.yml is triggered, which generates a new tag and
a new release.

[v0.15.1] - 2022-06-02
----------------------

### New Features

- none

### Bug Fixes

- Remove kvm from virtualization platforms

### Other Changes

- none

[v0.15.0] - 2022-05-10
----------------------

### New Features

- Unbreak FIPS detection and stabilize failing tests and GH actions
- Make sure Include is in the main configuration file when drop-in directory is used
- Make the role FIPS-aware

### Bug Fixes

- Fix runtime directory check condition
- README: fix meta/make\_option\_lists link

### Other Changes

- none

[v0.14.1] - 2021-09-23
----------------------

### New Features

- none

### Bug Fixes

- Use {{ ansible\_managed | comment }} to fix multi-line ansible\_managed

### Other Changes

- none

[v0.14.0] - 2021-08-18
----------------------

### New Features

- Drop support for Ansible 2.8 by bumping the Ansible version to 2.9

### Bug Fixes

- none

### Other Changes

- none

[v0.13.2] - 2021-08-18
----------------------

### New Features

- Add Debian 11 \(bullseye\) support

### Bug Fixes

- Fix wrong template file

### Other Changes

- Remove travis configuration and update readme with new badges
- Add CentOS 6 to CI

[v0.13.1] - 2021-08-03
----------------------

### New Features

- Add support for RHEL 9 and adjust tests for it

### Bug Fixes

- none

### Other Changes

- none

[v0.13.0] - 2021-06-12
----------------------

### New Features

- Add configuration options from OpenSSH 8.6p1
- Rename sshd\_namespace\_append to sshd\_config\_namespace
- Support for appending a snippet to configuration file
- Update meta data and README
- use state: absent instead of state: missing
- \[FreeBSD\] Add Subsystem to \_sshd\_defaults
- UsePrivilegeSeparation is deprecated since 2017/OpenSSH 7.5 - https://www.openssh.com/txt/release-7.5
- examples: Provide simple example playbook

### Bug Fixes

- Fix variable precedence when invoked through legacy "roles:"
- Fix issues found by linters - enable all tests on all repos - remove suppressions
- README: Document missing exported variable

### Other Changes

- Improve test coverage with new test cases and new distros, fixing minor issues on the way

[v0.12.0] - 2020-11-16
----------------------

### New Features

- none

### Bug Fixes

- none

### Other Changes

- Run tests with Github Actions and fix things on the way

[v0.11.1] - 2020-10-28
----------------------

### New Features

- none

### Bug Fixes

- none

### Other Changes

- Rename tests to follow best practices and make galaxy linters happy

[v0.11.0] - 2020-10-15
----------------------

### New Features

- Implement more natural match blocks and test them
- Support /etc/sysconfig/sshd to override crypto policies and handle more advanced use cases

### Bug Fixes

- README: Fix missing code block termination
- subsystem appears to be ignored

### Other Changes

- none

[v0.10.2] - 2020-09-24
----------------------

### New Features

- none

### Bug Fixes

- Remove extra blank line
- Disable broken ansible-lint-actions
- Cleanup lint issues, update documentation, fix typos

### Other Changes

- Implement more coherence check tests

[v0.10.1] - 2020-09-23
----------------------

### New Features

- Use ansible\_distribution\_major\_version in variables
- Create CODE\_OF\_CONDUCT.md

### Bug Fixes

- none

### Other Changes

- none

[v0.10.0] - 2020-09-18
----------------------

### New Features

- Minimum version is now Ansible 2.8
- exit\_host on ansible \>= 2.8
- OpenBSD and ansible\_distribution\_major\_version

### Bug Fixes

- none

### Other Changes

- none

[v0.9.1] - 2020-09-18
---------------------

### New Features

- none

### Bug Fixes

- none

### Other Changes

- Ubuntu focal, CI updates, code quality improvements

[v0.9.0] - 2020-09-18
---------------------

### New Features

- Add new options from OpenSSH 8.3p1 \(including CASignatureAlgorithms\)

### Bug Fixes

- none

### Other Changes

- none

[v0.8.2] - 2020-03-17
---------------------

### New Features

- Add Gentoo support \(with secure sshd defaults\)

### Bug Fixes

- none

### Other Changes

- none

[v0.8.1] - 2019-11-19
---------------------

### New Features

- add debian 10 \(buster\) support
- Add vars for openSUSE Leap 15 and CentOS 8

### Bug Fixes

- none

### Other Changes

- none

[v0.8.0] - 2019-07-10
---------------------

### New Features

- Remove duplicate GatewayPorts
- AIX support \(including new AIX handler\)
- Updates syntax to Ansible 2.7 era

### Bug Fixes

- none

### Other Changes

- none

[v0.7.6] - 2019-05-23
---------------------

### New Features

- none

### Bug Fixes

- Travis fixes
- Resolve lint errors

### Other Changes

- none

[v0.7.5] - 2019-04-29
---------------------

### New Features

- Remove 'UsePrivilegeSeparation' from Fedora defaults
- Backup of sshd\_config dependent on variable

### Bug Fixes

- none

### Other Changes

- none

[v0.7.4] - 2019-03-03
---------------------

### New Features

- none

### Bug Fixes

- Fix variable loading.

### Other Changes

- none

[v0.7.3] - 2019-02-20
---------------------

### New Features

- Make role work with chroot connections on EL 7.

### Bug Fixes

- Remove deprecated options

### Other Changes

- none

[v0.7.2] - 2018-09-11
---------------------

### New Features

- none

### Bug Fixes

- Fixes bad option in systemd service file

### Other Changes

- none

[v0.7.1] - 2018-09-08
---------------------

### New Features

- Adds on/off toggle

### Bug Fixes

- none

### Other Changes

- none

[v0.7.0] - 2018-09-07
---------------------

### New Features

- Adds ability to install a systemd service
- Add Ubuntu\_18.yml
- Add missing options
- expose sshd\_config template backup option with sshd\_backup variable

### Bug Fixes

- none

### Other Changes

- none

[v0.6.2] - 2018-06-16
---------------------

### New Features

- Add CoreOS support

### Bug Fixes

- none

### Other Changes

- none

[v0.6.1] - 2018-06-05
---------------------

### New Features

- none

### Bug Fixes

- Amazon var name should be sshd\_defaults

### Other Changes

- none

[v0.6.0] - 2018-04-24
---------------------

### New Features

- Remove Deprecated options in default SSH config
- Add StreamLocalBindUnlink option
- Makes handler use listen: option
- Removes tags
- change `ansible_pkg_mgr` for package

### Bug Fixes

- Fix for ansible\_virtualization\_type not being defined in Ansible \> 2.5
- Fix Arch Linux var file

### Other Changes

- none

[v0.5.1] - 2017-06-24
---------------------

### New Features

- Add Debian 9 \(stretch\) vars

### Bug Fixes

- none

### Other Changes

- none

[v0.5.0] - 2017-05-04
---------------------

### New Features

- Add note about UsePAM on RHEL 7

### Bug Fixes

- Ansible23 fixes
- Remove circular symlink in tests dir

### Other Changes

- none

[v0.4.10] - 2017-04-07
----------------------

### New Features

- none

### Bug Fixes

- Fixed sshd\_match blocks

### Other Changes

- none

[v0.4.9] - 2017-03-20
---------------------

### New Features

- none

### Bug Fixes

- Fix sshd service state

### Other Changes

- none

[v0.4.8] - 2017-02-11
---------------------

### New Features

- clean Archlinux support to match the current package \(openssh-7.4p1-2\)
- vars: SUSE: Add default variables for SUSE based distributions

### Bug Fixes

- none

### Other Changes

- none

[v0.4.7] - 2016-12-26
---------------------

### New Features

- Don't fail without package manager

### Bug Fixes

- none

### Other Changes

- none

[v0.4.6] - 2016-10-20
---------------------

### New Features

- Support for OpenBSD

### Bug Fixes

- none

### Other Changes

- none

[v0.4.5] - 2016-08-03
---------------------

### New Features

- show xenial support on galaxy

### Bug Fixes

- none

### Other Changes

- none

[v0.4.4] - 2016-04-16
---------------------

### New Features

- Added ubuntu 16.04 config

### Bug Fixes

- none

### Other Changes

- none

[v0.4.3] - 2016-03-09
---------------------

### New Features

- none

### Bug Fixes

- fix deprecation warning for sshd\_packages

### Other Changes

- Housekeeping

[v0.4.2] - 2016-01-24
---------------------

### New Features

- none

### Bug Fixes

- Fix for CentOS 6 l\_value issue
- Update example so not to break old SSH versions and add a warning

### Other Changes

- none

[v0.4.1] - 2016-01-11
---------------------

### New Features

- Fedora HostKey\(s\)

### Bug Fixes

- none

### Other Changes

- none

[v0.4.0] - 2015-08-25
---------------------

### New Features

- none

### Bug Fixes

- Do not manage /var/run/sshd on CentOS7 fixes \#27

### Other Changes

- none

[v0.3.2] - 2015-07-23
---------------------

### New Features

- DebianBanner support

### Bug Fixes

- none

### Other Changes

- none

[v0.3.1] - 2015-06-28
---------------------

### New Features

- Verify SSHd config early
- Add Fedora support
- fix type in AcceptEnv for RedHat7

### Bug Fixes

- Fix issues - not reloading with default sshd\_allow\_reload value

### Other Changes

- none

[v0.3.0] - 2015-06-25
---------------------

### New Features

- Make the role more container friendly
- Remove apt role dependency

### Bug Fixes

- fix type in AcceptEnv

### Other Changes

- none

[v0.2.5] - 2015-01-23
---------------------

### New Features

- none

### Bug Fixes

- Don't install openssh-sftp-server on Debian

### Other Changes

- none

[v0.2.0] - 2015-01-04
---------------------

### New Features

- none

### Bug Fixes

- none

### Other Changes

- Add precise, move 14.04 to specific configuration
- Feature/debian defaults
- Minor typo fixes and add Archlinux support

[v0.1.0] - 2014-12-25
---------------------

### Initial Release
