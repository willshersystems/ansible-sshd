
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
  end

  config.vm.provision "shell", inline: <<-SHELL
    sudo yum install -y libselinux-python
  SHELL

  config.vm.provision "ansible_local" do |ansible|
    ansible.playbook = "tests/test.yml"
    ansible.install  = true
  end

end
