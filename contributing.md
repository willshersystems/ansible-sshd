# Contributing to ansible-sshd

## Where to start

The first place to go is [Contribute](https://linux-system-roles.github.io/contribute.html).
This has all of the common information that all role developers need:

* Role structure and layout
* Development tools - How to run tests and checks
* Ansible recommended practices
* Basic git and github information
* How to create git commits and submit pull requests

**Bugs and needed implementations** are listed on
[Github Issues](https://github.com/willshersystems/ansible-sshd/issues).
Issues labeled with
[**help wanted**](https://github.com/willshersystems/ansible-sshd/issues?q=is%3Aissue+is%3Aopen+label%3A%22help+wanted%22)
are likely to be suitable for new contributors!

**Code** is managed on [Github](https://github.com/willshersystems/ansible-sshd), using
[Pull Requests](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/about-pull-requests).

## Creating a release

You must use automation to create releases consistently. The process of creating a release is the following:

1. Clone ansible-sshd, ensure that you have a remote for your fork configured and checkout a new branch to use for a release PR:

    ```bash
    git clone git@github.com:willshersystems/ansible-sshd.git
    git remote add <your_gh_username> git@github.com:<your_gh_username>/ansible-sshd.git
    git checkout -b new-ver
    ```

2. Get the [linux-system-roles/auto-maintenance/role-make-version-changelog.sh](https://github.com/linux-system-roles/auto-maintenance/blob/main/role-make-version-changelog.sh) script:

    ```bash
    wget https://raw.githubusercontent.com/linux-system-roles/auto-maintenance/main/role-make-version-changelog.sh
    ```

3. Run the [linux-system-roles/auto-maintenance/role-make-version-changelog.sh](https://github.com/linux-system-roles/auto-maintenance/blob/main/role-make-version-changelog.sh) script:

    ```bash
    sh role-make-version-changelog.sh
    ```

    This script creates updates CHANGELOG.md with a summary of pull requests added since the previous release and with automatically identified new version based on the PR types.
    It also optionally updates .README.html with changes to README.md made since the previous release.

    To learn more about available script options, see [role-make-version-changelog.sh documentation](https://github.com/linux-system-roles/auto-maintenance#role-make-version-changelogsh).

4. Verify that the script added a commit for new release by running `git log`.

5. Push the changes to your fork and create a PR.

These are all the manual steps that you must do to initiate a new release.
After the PR is reviewed and merged, i.e. after changes are made to CHANGELOG.md, the [changelog_to_tag.yml](https://github.com/willshersystems/ansible-sshd/blob/main/.github/workflows/changelog_to_tag.yml) workflow triggers and creates tag and release.
