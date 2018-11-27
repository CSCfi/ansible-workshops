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
  IdentityFile ./ansible-workshops/intro-workshop/vagrant/.vagrant/machines/default/virtualbox/private_key
  IdentitiesOnly yes
  LogLevel FATAL
```

Notice the lines:
```
HostName 127.0.0.1
  User vagrant
  Port 2222
  IdentityFile ./ansible-workshops/intro-workshop/vagrant/.vagrant/machines/default/virtualbox/private_key
```
 In you particular case, every field will in principle be the same, except the path of `IdentityFile`.

 ## Telling Ansible about your Vagrant test server

 Ansible can only manage the servers it explicitly knows about, hence you need to declare them in an inventory file.

 Each server needs a name. You can use the hostname of the server, or give it an alias and pass some additional arguments to to tell Ansible how to connect to it.

 For example, create a file called *hosts* under a *playbooks* directory (this will serve for now as the inventory file) and add the following entry in one single line (notice the line breaks, don't include them in your file):

```
testserver ansible_ssh_host=127.0.0.1 ansible_ssh_port=2222 \
  ansible_ssh_user=vagrant \
  ansible_ssh_private_key_file=./ansible-workshops/intro-workshop/vagrant/.vagrant/machines/default/virtualbox/private_key
```

Then let's call the `ansible` command to test the connection from Ansible to the Vagrant testserver:
```
All/ansible-workshops/intro-workshop/vagrant$ ansible testserver -i playbooks/hosts -m ping


```
If all goes well, you should get an output like this:
```
testserver | SUCCESS => {
   "changed": false,
   "ping": "pong"
}
```

## Vagrant and ansible.cfg

The above manual steps are just an example to illustrate how you can connect to your Vagrant machines with Ansible. Let's see how we can use *ansible.cfg* to set some default values to Ansible's so that we can have more automation (and not type that much).

Ansible looks for an *ansible.cfg* file in the following directories, in this order:

1. File specified by the ANSIBLE_CONFIG environment variable
2. *./ansible.cfg* (*ansible.cfg* in the current directory)
3. *~/.ansible.cfg* (*.ansible.cfg*) in your home directory
4. */etc/ansible/ansible.cfg*

Evidently, you know best which approach 1.-4. suits better your needs. Though some of us prefer to have their *ansible.cfg* alongside their playbooks (option 2.), in order to have "portable-and-yet-playbook-specific" variables for those playbooks.

Example of such an *ansible.cfg* for usage with Vagrant:

```
[defaults]
hostfile = hosts
remote_user = vagrant
private_key_file = ../vagrant/machines/default/virtualbox/private_key
host_key_checking = False
```

In this example *ansible.cfg* file, you can see the specification of the location of the *inventory* file (*hostfile*), the user to SSH to the Vagrant machine (*remote_user*), and the respective SSH private key (*private_key_file*).

Notice that SSH key checking (*host_key_checking*) is disabled. This is very handy when working with Vagrant machines, which can be created and destroyed often, otherwise we'd have to edit *~./ssh/known_hosts* all the time. Evidently, this can be a security risk when connecting to other servers over a network.

With *remote_user* and *private_key_file* we can even simplify our Ansible inventory *hosts* file:

```
testserver ansible_ssh_host=127.0.0.1 ansible_ssh_port=2222
```
