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
 In you particular case, every field will in principle be the same, except the path of `IdentityFile`.

 ## Telling Ansible about your Vagrant test server

 Ansible can only manage the servers it explicitly knows about, hence you need to declare them in an inventory file.

 Each server needs a name. You can use the hostname of the server, or give it an alias and pass some additional arguments to to tell Ansible how to connect to it.

 For example, create a file called <i>hosts</i> under a <i>playbooks</i> directory (this will serve for now as the inventory file) and add the following entry in one single line (notice the line breaks, don't include them in your file):

```
testserver ansible_ssh_host=127.0.0.1 ansible_ssh_port=2222 \
  ansible_ssh_user=vagrant \
  ansible_ssh_private_key_file/Users/joao/workspace/ansible-workshops/intro-workshop/vagrant/.vagrant/machines/default/virtualbox/private_key
```

Then let's call the `ansible` command to test the connection from Ansible to the Vagrant testserver:
```
joao@Joaos-MBP:~/workspace/ansible-workshops/intro-workshop/vagrant$ ansible testserver -i playbooks/hosts -m ping

```
If all goes well, you should get an output like this:
```
joao@Joaos-MBP:~/workspace/ansible-workshops/intro-workshop/vagrant$ ansible testserver -i playbooks/hosts -m ping
testserver | SUCCESS => {
   "changed": false,
   "ping": "pong"
}
```

## Vagrant and ansible.cfg
