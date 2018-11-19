### Getting Started with Vagrant for Ansible

If you want to quickly test your Ansible playbooks, it's a good idea to install [Vagrant](https://www.vagrantup.com/) on your development machine (Linux/MacOS/Windows).

Vagrant is a good open source tool for managing VirtualBox virtual machines, that you can use for booting up a Linux Virtual Machine in your machine. It needs the [VirtualBox](https://www.virtualbox.org) virtualiser to be installed in your machine. [Download VirtualBox](https://www.virtualbox.org/wiki/Downloads) and then [download Vagrant](https://www.vagrantup.com/downloads.html)

Once you have VirtualBox and Vagrant installed, you can initialise a Centos 7 Vagrant configuration file with the following commands inside your `/ansible-workshops/intro-workshop/vagrant` directory:

```
$ vagrant init centos/7
$ vagrant up
```
This will download a virtual machine onto which you should able to login to:

```
$ vagrant ssh
```
You should see the Centos command line prompt. Type `exit` to quit the SSH session.

This lets us interact with the shell, but Ansible needs to connect to the virtual machine using SSH, not the `vagrant ssh` command. For that, we need to know the Vagrant SSH connection details:

```
$ vagrant ssh-config
Host default
  HostName 127.0.0.1
  User vagrant
  Port 2222
  UserKnownHostsFile /dev/null
  StrictHostKeyChecking no
  PasswordAuthentication no
  IdentityFile /home/josilva/workspace/ansible-workshops/intro-workshop/vagrant/.vagrant/machines/default/virtualbox/private_key
  IdentitiesOnly yes
  LogLevel FATAL
```

Notice the lines:
```
HostName 127.0.0.1
  User vagrant
  Port 2222
  IdentityFile /home/josilva/workspace/ansible-workshops/intro-workshop/vagrant/.vagrant/machines/default/virtualbox/private_key
```
 In you particluar case, very field will in principle be the same, except the path of `IdentityFile`.
 
 ## Telling Ansible about your Vagrant test server
