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

Whose accessibility we can test with a few commands:

```
~/ansible-workshops/intro-workshop/vagrant/playbooks$ ansible testserver -m ping
[DEPRECATION WARNING]: [defaults]hostfile option, The key is misleading as it can also be a list of hosts, a directory or a list of paths , use [defaults] inventory=/path/to/file|dir instead. This
feature will be removed in version 2.8. Deprecation warnings can be disabled by setting deprecation_warnings=False in ansible.cfg.
testserver | SUCCESS => {
    "changed": false,
    "ping": "pong"
}


~/workspace/ansible-workshops/intro-workshop/vagrant/playbooks$ ansible testserver -a uptime
[DEPRECATION WARNING]: [defaults]hostfile option, The key is misleading as it can also be a list of hosts, a directory or a list of paths , use [defaults] inventory=/path/to/file|dir instead. This
feature will be removed in version 2.8. Deprecation warnings can be disabled by setting deprecation_warnings=False in ansible.cfg.
testserver | SUCCESS | rc=0 >>
 10:41:14 up  4:54,  1 user,  load average: 0.00, 0.01, 0.05


 ~/workspace/ansible-workshops/intro-workshop/vagrant/playbooks$ ansible testserver -a "tail /var/log/dmesg"
 [DEPRECATION WARNING]: [defaults]hostfile option, The key is misleading as it can also be a list of hosts, a directory or a list of paths , use [defaults] inventory=/path/to/file|dir instead. This
 feature will be removed in version 2.8. Deprecation warnings can be disabled by setting deprecation_warnings=False in ansible.cfg.
 testserver | SUCCESS | rc=0 >>
 [    2.109063] RPC: Registered tcp NFSv4.1 backchannel transport module.
 [    2.407574] random: crng init done
 [    2.498185] ACPI: Video Device [GFX0] (multi-head: yes  rom: no  post: no)
 [    2.505287] input: Video Bus as /devices/LNXSYSTM:00/device:00/PNP0A03:00/LNXVIDEO:00/input/input4
 [    2.594221] input: PC Speaker as /devices/platform/pcspkr/input/input5
 [    2.597606] piix4_smbus 0000:00:07.0: SMBus Host Controller at 0x4100, revision 0
 [    2.622759] e1000: Intel(R) PRO/1000 Network Driver - version 7.3.21-k8-NAPI
 [    2.623674] e1000: Copyright (c) 1999-2006 Intel Corporation.
 [    2.629690] cryptd: max_cpu_qlen set to 100
 [    2.640313] sd 0:0:0:0: Attached scsi generic sg0 type 0


 ~/workspace/ansible-workshops/intro-workshop/vagrant/playbooks$ ansible testserver -s -a "tail /var/log/messages"
 [DEPRECATION WARNING]: [defaults]hostfile option, The key is misleading as it can also be a list of hosts, a directory or a list of paths , use [defaults] inventory=/path/to/file|dir instead. This
 feature will be removed in version 2.8. Deprecation warnings can be disabled by setting deprecation_warnings=False in ansible.cfg.
 [DEPRECATION WARNING]: The sudo command line option has been deprecated in favor of the "become" command line arguments. This feature will be removed in version 2.6. Deprecation warnings can be
 disabled by setting deprecation_warnings=False in ansible.cfg.
 testserver | SUCCESS | rc=0 >>
 Nov 27 10:41:13 localhost systemd: Stopping User Slice of vagrant.
 Nov 27 10:41:14 localhost systemd: Created slice User Slice of vagrant.
 Nov 27 10:41:14 localhost systemd: Starting User Slice of vagrant.
 Nov 27 10:41:14 localhost systemd: Started Session 15 of user vagrant.
 Nov 27 10:41:14 localhost systemd-logind: New session 15 of user vagrant.
 Nov 27 10:41:14 localhost systemd: Starting Session 15 of user vagrant.
 Nov 27 10:41:14 localhost ansible-command: Invoked with warn=True executable=None _uses_shell=False _raw_params=uptime removes=None creates=None chdir=None stdin=None
 Nov 27 10:41:46 localhost ansible-command: Invoked with warn=True executable=None _uses_shell=False _raw_params=tail /var/log/dmesg removes=None creates=None chdir=None stdin=None
 Nov 27 10:41:55 localhost ansible-command: Invoked with warn=True executable=None _uses_shell=False _raw_params=tail /var/log/dmesg removes=None creates=None chdir=None stdin=None
 Nov 27 10:42:13 localhost ansible-command: Invoked with warn=True executable=None _uses_shell=False _raw_params=tail /var/log/messages removes=None creates=None chdir=None stdin=None

```
If this works, now we can scale up to running a playbook. How would you deploy an Apache playbook on a Vagrant machine? :-)
