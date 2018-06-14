
# Ansible Introduction Hands-on Workshop

## What knowledge and skills do we aim to develop?
* Basics of Ansible concepts.
* Write own basic playbooks for common tasks (e.g. deploy a web server, automate simple sysadmin tasks, etc. ).
* Use git to check out and commit Ansible playbooks.
* Confidence to continue using Ansible by oneself and look into further resources (Ansible Galaxy, etc), and interest in further hands-on workshops


## How to achieve that?

* With a friendly workshop for all sysadmins and developers who are interested in  Ansible and would like some guided exercises to get started.

    * Absolute maximum duration: 2 hours
    * A few slides to introduce Ansible basic concepts
    * Exercises of progressive difficulty level on:
        * Apache Hello World (or Nginx Hello World as alternative)
        * Sys Admin Tasks (e.g chrony)
        * Infra Admin Tasks
    * And a reference to Ansible use in Taito. See [servers/taito in Kielipankki-palvelut](https://github.com/CSCfi/Kielipankki-palvelut/tree/master/servers/taito "The Taito software stack of the Language Bank")

And why not continuing the Apache thread by a ops_playbook to for example update apache on all the nodes or why not how to add the oh-so important [ http://www.gnuterrypratchett.com/#apache | http://www.gnuterrypratchett.com/#apache ]

## Pre-requisite Skills
1. Connect to a remote machine with SSH
2. Interact with BASH and use `sudo`
3. Install software packages
4. Check and set file permissions
5. Start and stop services
6. Set environment variables
7. Experience in writing scripts (any language) is a plus

## Reading materials

http://docs.ansible.com/

## Getting Started with the Exercises
0. Installing ansible after sshing in to the bastion host

1. apache2: this is the simplest exercise, the inventory is in one playbook (`apache2.yml.`). Give a value to `hosts` (replace `<your_remote_host>` with the remote host's IP) and get it running with `ansible-playbook apache2.yml`.

2. `sysadmin`: several sysadmin playbooks under `/sysadmin/playbooks`:

  2.1 Configure User accounts on the host

     1 Add another user
     2 Add your user's ssh public key to the authorized_keys file for a new user

  2.2 Configure Chrony for NTP on the host

     1 Prevent ntpd and chrony from running at the same time
     2 Add the rest of the FUNET NTP servers ntp2.funet.fi ntp3.funet.fi and ntp4.funet.fi

  2.3 Configure SSH on the host

     1 Make PrintMotd a variable. Keep it False by default and change it to True in the playbook
     2 Move this task into a role

  2.4 Configure Logrotate on the host

     1 Fix a bug :)
     2 Is it possible to use the validate parameter to the template module when templating in the logrotate config file?

  2.5 Use the debug ansible module

     1 What is the ansible-playbook command needed to output the variable to your terminal?
     2 How can you make the playbook output the variable also when running in --check mode?
