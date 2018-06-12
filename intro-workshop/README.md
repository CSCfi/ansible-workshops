
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

## Getting Started with the Exercises
1. apache2: this is the simplest exercise, the inventory is in one playbook (`apache2.yml.`). Give a value to `hosts` (replace `<your_remote_host>` with the remote host's IP) and get it running with `ansible-playbook apache2.yml`.

2. `sysadmin`: several sysadmin playbooks under `/sysadmin/playbooks`:

  2.1 Configure User accounts on the host

  2.2 Configure Chrony for NTP on the host

  2.3. Configure Logrotate on the host

  2.4 Configure SSH on the host
