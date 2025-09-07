Changelog
=========

[v0.28.0] - 2025-09-07
--------------------

### New Features

- feat: add Debian 13 support (#315)
- feat: Support for daemon reload, socket restart and systemd socket file to match Ubuntu 24.04 (#318)

### Bug Fixes

- fix: include external config files first so they can override all options (#316)

[v0.27.1] - 2025-08-01
--------------------

### Bug Fixes

- fix: New configuration option in CentOS 10 (#319)

[v0.27.0] - 2025-06-19
--------------------

### New Features

- feat: Add new options from OpenSSH 10.0 (#312)

### Bug Fixes

- fix: service: Add default Environment option (#308)

### Other Changes

- ci: use ansible-lint v25 - have to use requirements file for ansible-lint now (#309)
- refactor: Ansible 2.19 support (#311)

[v0.26.0] - 2025-01-06
--------------------

### New Features

- feat: New options in OpenSSH + fixes for bugx in OpenSSH 9.9p1 (#304)
- feat: Use sshd_config instead of sshd which has been deprecated (#299)

### Bug Fixes

- fix: use quote with command, shell and validate with variable (#298)
- fix: Reload the service when needed (#303)

### Other Changes

- test: set TMPDIR in block of role invocation (#300)

[v0.25.0] - 2024-08-19
--------------------

### New Features

- feat: Add new configuration options from OpenSSH 9.8

[v0.24.1] - 2024-07-03
--------------------

### Bug Fixes

- fix: add support for EL10 (#293)

[v0.24.0] - 2024-06-21
--------------------

### New Features

- feat:  Ubuntu Noble support (#290)

### Bug Fixes

- fix: Ubuntu 22.04 PrintMotd set default to false (#290)

### Other Changes

- build(deps): bump mathieudutour/github-tag-action from 6.1 to 6.2 (#283)

[v0.23.5] - 2024-04-09
--------------------

### Other Changes

- test: ensure that sshd2 is completely stopped and removed

[v0.23.4] - 2024-04-05
--------------------

### Bug Fixes

- fix: Document and streamline the sshd_main_config_file (#281)

[v0.23.3] - 2024-04-03
--------------------

### Other Changes

- build(deps): bump ansible/ansible-lint from 6 to 24 (#279)

[v0.23.2] - 2024-02-19
--------------------

### Bug Fixes

- fix: Fix service files generated on EL7 and workaround the tests for containers (#276)

### Other Changes

- docs: Fix spelling issues + fix reported issues (#274)
- build(deps): bump actions/checkout from 3 to 4 (#275)
- README.md typo in config word (#277)

[v0.23.1] - 2024-01-25
--------------------

### Bug Fixes

- fix: Review and update service units and socket unit to include distribution defaults

### Other Changes

- ci: fix ansible-lint 2.16 issues; use ansible-lint 2.16

[v0.23.0] - 2023-11-29
--------------------

### New Features

- feat: support for ostree systems (#270)

### Bug Fixes

- fix: Avoid creation of runtime directories in home (#265)

### Other Changes

- tests: Ensure backup/restore preserves file attributes (#269)

[v0.22.0] - 2023-10-18
--------------------

### Bug Fixes

- fix: Symlink sub-directories under tests/roles/ansible-sshd to avoid recursive loop (#262)

  Enhancement:
  Moved symlinking a level down in test/roles to avoid a recursive look via the test directory.
  
  Reason:
  Ansible Core >= 2.15.5 does not allow recursive directory trees. 
  
  Result:
  CI should still run correctly, the problem with the recursive symlinks with Ansible Core 2.15.5 should be fixed.
  
  Issue Tracker Tickets (Jira or BZ if any):
  #259 #260 #261

[v0.21.0] - 2023-09-12
--------------------

### New Features

- feat: manage ssh certificates (#252)

  **Enhancement:**
  - Deploy User CA on the system
  - Configure principals (optional)
  
  **Reason:**
  This allows you to configure and manage the SSH server to authenticate via certificates. 
  Improves SSH authentication security: certificates have a validity period, unlike SSH keys.
  
  More information on SSH certificates is available here: [Managing SSH Access at Scale with HashiCorp Vault](https://www.hashicorp.com/blog/managing-ssh-access-at-scale-with-hashicorp-vault).
  
  **Result:**
  All tests passed.
  The related documentation is available and an example can be found in ```examples/example-use-certificates.yml```.
  
  **Issue Tracker Tickets (Jira or BZ if any):** -

### Bug Fixes

- fix: Support inject_facts_as_vars = false (#244)

  Enhancement:
  
  Support `inject_facts_as_vars = false` in ansible.cfg.
  
  The setting is considered safer because a compromised host cannot inject facts into variables.
  
  Reason:
  
  Minor security enhancement.
  
  This setting is also recommended in some tuning guides like
  https://docs.openstack.org/kolla-ansible/wallaby/user/ansible-tuning.html#fact-variable-injection
  and issue mitigation guides:
  https://docs.ansible.com/ansible/latest/reference_appendices/faq.html#when-is-it-unsafe-to-bulk-set-task-arguments-from-a-variable
  
  `ansible_facts` are used only with one name. Previously for example `ansible_facts['os_family']` was also used as `ansible_os_family`. This helps maintainability.
  
  Result:
  
  Support `inject_facts_as_vars = false`. If setting is `true`, situation still works as expected.
  
  Also drop `ansible` prefix from local variables to avoid possible conflicts in namespace and avoid possible confusion.
  
  Issue Tracker Tickets (Jira or BZ if any): -

- fix: Makes runtime dir relative (#249)

  Enhancement:
  Makes systemd RuntimeDirectory service file directive relative (`sshd` instead of `/run/sshd`).
  
  Reason:
  The [docs](https://www.freedesktop.org/software/systemd/man/systemd.exec.html#RuntimeDirectory=) say it has to be relative.
  
  Result:
  The following error is gone from the journal:
  
  ```
  /etc/systemd/system/backdoor-ssh.service:14: RuntimeDirectory= path is not valid, ignoring assignment: /run/custom-ssh
  ```
  
  Waiting for the tests.
  
  Issue Tracker Tickets (Jira or BZ if any): none

### Other Changes

- chore: fix markdown for heading in CHANGELOG (#242)

  chore: add missing h2 heading for the 0.19.0 release
  
  There was no markdown h2 heading for the 0.19.0 release which
  broke the changelog parser in the collection release, causing
  the changelog to look like
  https://github.com/linux-system-roles/auto-maintenance/commit/0eade02032c55ffc008240ce44cfbee25276b51c#diff-ddbe2c1474f5ea331aef8eedcd595299f771578e4416a5f112ae69ed5a934bc0R4
  Add the correct markdown
  
  Signed-off-by: Rich Megginson <rmeggins@redhat.com>

- chore: drop support of Fedora 31, EOL 2020-11-24 (#243)

  Enhancement:
  
  -
  
  Reason:
  
  Fedora 31 is EOL.
  
  Result:
  
  Drop explicit support of EOL distro version. Less code to maintain.

- ci: Add markdownlint, test_converting_readme, and build_docs workflows (#247)

  Enhancement: Add markdownlint, test_converting_readme, and build_docs GitHub workflows
  
  Reason:
  * markdownlint runs against markdown files to ensure correct syntax and avoid any issues with converting README.md to HTML
  * test_converting_readme converts README.md > HTML and uploads this test artifact to ensure that conversion works fine
  * build_docs converts README.md > HTML and pushes the result to the docs branch to publish dosc to GitHub pages site
  * Rename commitlint.yml workflow into pr-title-lint for clarity

- ci: Ignore var-naming[no-role-prefix] ansible-lint rule that fails expectedly (#248)

  Enhancement: Ignore var-naming[no-role-prefix] ansible-lint rule that fails expectedly
  
  Reason: ansible-lint recently added a rule `var-naming[no-role-prefix]` that fails expectedly, this role generally uses `sshd` instead of `ansible_sshd`, and also vars from other roles e.g. `firewall_`.
  
  Result: ansible-lint ignores this rule and passes.

- build(deps): bump actions/checkout from 3 to 4 (#254)

  Bumps [actions/checkout](https://github.com/actions/checkout) from 3 to 4.

[v0.20.0] - 2023-06-19
--------------------

### New Features

- feat: debian 12 support and small config fixes for debian (#238)

  This PR adds Debian 12 (aka bookworm) support to the role.
  The workflow fails at the moment because there is no roles-ansible/check-ansible-debian-bookworm-action repo yet. As soon as @DO1JLR has created the repo it should pass all checks.
  
  Furthermore i fixed some small oversights in older debian defaults.

- feat: Fix alpine tests by adding a new configuration options (#240)

### Other Changes

- proper Subsystem sftp default for RHEL9 (#220)

  Basically the same as for RHEL6/7/8

- ci: Add pull request template and run commitlint on PR title only (#237)

  We now ensure the conventional commits format only on PR titles and not on
  commits to let developers keep commit messages targeted for other developers
  i.e. describe actual changes to code that users should not care about.
  And PR titles, on the contrary, must be aimed at end users.
  
  For more info, see
  https://linux-system-roles.github.io/contribute.html#write-a-good-pr-title-and-description

- chore: moved debian 7 (wheezy) config to explicit file (#239)

  This removes the `defaults/Debian.yml` file and moves it to the `defaults/Debian_7.yml` file. This prohibits rolling out ancient config on new Debian-Systems which aren't supported by this role.

[v0.19.0] - 2023-04-27
--------------------

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
