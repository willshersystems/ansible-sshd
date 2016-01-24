# -*- mode: ruby -*-
# vi: set ft=ruby :

VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  # config.vm.define "ubuntu" do |ubuntu|
  #   ubuntu.vm.box = "ubuntu/trusty64"
  #   ubuntu.vm.provision "shell", inline: <<-SHELL
  #     sudo add-apt-repository -y ppa:ansible/ansible
  #     sudo apt-get update -qq
  #     sudo apt-get -qq install ansible
  #   SHELL
  # end

  config.vm.define "centos6" do |centos|
    centos.vm.box = "bento/centos-6.7"
    centos.vm.provision "shell", inline: <<-SHELL
      sudo yum install -y https://dl.fedoraproject.org/pub/epel/epel-release-latest-6.noarch.rpm
      sudo yum install -y ansible libselinux-python
    SHELL
  end

  config.vm.synced_folder ".", "/etc/ansible/roles/ansible-sshd"
  config.vm.provision :ansibleLocal, :playbook => "tests/test.yml"

end
