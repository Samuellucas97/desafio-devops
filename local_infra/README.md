# Ambiente local

Este diretório possui `Linux Ubuntu 20.04 LTS`, onde configura um `MicroK8s`. A imagem abaixo mostra a arquitetura proposta, onde é instalado o Kong e a aplicação Flask de exemplo.

![Loca infrastructure design](../assets/local-environment_version_3.png)


## Requisitos

- Vagrant (_versão 2.2.19_)
  - Como instalar? Execute `sudo apt install vagrant`
- VirtualBox (_versão 6.1.50\_Ubuntu r16103_)
  - Como instalar? Execute `sudo apt-get install virtualbox-6.1`
- Ansible
  - Como instalar? Execute `sudo apt-get install ansible`

Execute o script abaixo para instalar todos os requisitos:

```bash
$ make requirements 

******************** INSTALLING SOFTWARE REQUIREMENTS **********************************
if [ -x /usr/bin/apt-get ]; then  xargs -a requirements.txt sudo apt-get install -y; fi
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
ansible is already the newest version (2.10.7+merged+base+2.10.8+dfsg-1).
vagrant is already the newest version (2.2.19+dfsg-1ubuntu1).
virtualbox is already the newest version (6.1.50-dfsg-1~ubuntu1.22.04.1).
The following packages were automatically installed and are no longer required:
  chromium-codecs-ffmpeg-extra gstreamer1.0-vaapi guile-2.2-libs libflashrom1 libftdi1-2 libgc1
  libgnome-games-support-1-3 libgnome-games-support-common libgstreamer-plugins-bad1.0-0 libllvm13
  libminizip1 libqqwing2v5 libva-wayland2
Use 'sudo apt autoremove' to remove them.
0 to upgrade, 0 to newly install, 0 to remove and 59 not to upgrade.

```

## Instalando e usando a VM

Para criação da VM e obtenção de acesso, use o comando abaixo:

```bash
$ make

******************** DESTROYING THE VIRTUAL MACHINE **********************************
vagrant destroy -f
==> default: Destroying VM and associated drives...

vagrant status
Current machine states:

default                   not created (virtualbox)

The environment has not yet been created. Run `vagrant up` to
create the environment. If a machine is not created, only the
default provider will be shown. So if a provider is not listed,
then the machine is not created for that environment.


******************** BUILDING THE VIRTUAL MACHINE **********************************
vagrant provision
==> default: VM not created. Moving on...

vagrant status
Current machine states:

default                   not created (virtualbox)

The environment has not yet been created. Run `vagrant up` to
create the environment. If a machine is not created, only the
default provider will be shown. So if a provider is not listed,
then the machine is not created for that environment.


******************** RUNNING THE VIRTUAL MACHINE **********************************
vagrant up
Bringing machine 'default' up with 'virtualbox' provider...
==> default: Importing base box 'ubuntu/focal64'...
==> default: Matching MAC address for NAT networking...
==> default: Checking if box 'ubuntu/focal64' version '20240306.0.0' is up to date...
==> default: A newer version of the box 'ubuntu/focal64' for provider 'virtualbox' is
==> default: available! You currently have version '20240306.0.0'. The latest is version
==> default: '20240306.0.1'. Run `vagrant box update` to update.
==> default: Setting the name of the VM: local_infra_default_1711935269628_61595
==> default: Clearing any previously set network interfaces...
==> default: Preparing network interfaces based on configuration...
    default: Adapter 1: nat
    default: Adapter 2: hostonly
==> default: Forwarding ports...
    default: 22 (guest) => 2222 (host) (adapter 1)
==> default: Running 'pre-boot' VM customizations...
==> default: Booting VM...
==> default: Waiting for machine to boot. This may take a few minutes...
    default: SSH address: 127.0.0.1:2222
    default: SSH username: vagrant
    default: SSH auth method: private key
    default: 
    default: Vagrant insecure key detected. Vagrant will automatically replace
    default: this with a newly generated keypair for better security.
    default: 
    default: Inserting generated public key within guest...
    default: Removing insecure key from the guest if it's present...
    default: Key inserted! Disconnecting and reconnecting using new SSH key...
==> default: Machine booted and ready!
==> default: Checking for guest additions in VM...
==> default: Configuring and enabling network interfaces...
==> default: Mounting shared folders...
    default: /vagrant => /home/samuel/Music/desafio-devops/local_infra
==> default: Running provisioner: file...
    default: ./k8s => /home/vagrant/k8s
==> default: Running provisioner: file...
    default: ./kong => /home/vagrant/kong
==> default: Running provisioner: file...
    default: ./ansible => /home/vagrant/ansible
==> default: Running provisioner: ansible...
    default: Running ansible-playbook...

PLAY [localhost] ***************************************************************

TASK [Gathering Facts] *********************************************************
ok: [localhost]

TASK [Update package cache] ****************************************************
changed: [localhost]

TASK [Upgrade all packages] ****************************************************
changed: [localhost]

TASK [Install prerequisites for MicroK8s] **************************************
ok: [localhost] => (item=curl)
ok: [localhost] => (item=iptables)
ok: [localhost] => (item=snapd)

TASK [Install MicroK8s] ********************************************************
changed: [localhost]

TASK [Check MicroK8s status] ***************************************************
changed: [localhost]

TASK [Create .kube directory] **************************************************
changed: [localhost]

TASK [Checking if the group exists] ********************************************
ok: [localhost]

TASK [Add Ansible user to microk8s group] **************************************
changed: [localhost]

TASK [Change ownership to Ansible user (and group)] ****************************
ok: [localhost]

TASK [Add kubectl and helm aliases] ********************************************
changed: [localhost] => (item={'alias': 'kubectl', 'command': 'microk8s kubectl'})
changed: [localhost] => (item={'alias': 'helm', 'command': 'microk8s helm'})

TASK [Enable add-ons] **********************************************************
changed: [localhost]

TASK [Instal Metallb] **********************************************************
changed: [localhost]

TASK [Install Kubernetes Gateway API] ******************************************
changed: [localhost]

TASK [Install Kubernetes Gateway CRD] ******************************************
changed: [localhost]

TASK [Add Kong helm repo] ******************************************************
changed: [localhost]

TASK [Update Helm repo] ********************************************************
changed: [localhost]

TASK [Check if the Kong namespace exists] **************************************
fatal: [localhost]: FAILED! => {"changed": true, "cmd": ["microk8s.kubectl", "get", "namespace", "kong"], "delta": "0:00:00.164182", "end": "2024-04-01 01:40:04.254308", "msg": "non-zero return code", "rc": 1, "start": "2024-04-01 01:40:04.090126", "stderr": "Error from server (NotFound): namespaces \"kong\" not found", "stderr_lines": ["Error from server (NotFound): namespaces \"kong\" not found"], "stdout": "", "stdout_lines": []}
...ignoring

TASK [Install KIC Helm] ********************************************************
changed: [localhost]

PLAY RECAP *********************************************************************
localhost                  : ok=19   changed=15   unreachable=0    failed=0    skipped=0    rescued=0    ignored=1   


vagrant status
Current machine states:

default                   running (virtualbox)

The VM is running. To stop this VM, you can run `vagrant halt` to
shut it down forcefully, or you can run `vagrant suspend` to simply
suspend the virtual machine. In either case, to restart it again,
simply run `vagrant up`.

vagrant ssh
Welcome to Ubuntu 20.04.6 LTS (GNU/Linux 5.4.0-173-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/pro

 System information disabled due to load higher than 2.0


Expanded Security Maintenance for Applications is not enabled.

0 updates can be applied immediately.

Enable ESM Apps to receive additional future security updates.
See https://ubuntu.com/esm or run: sudo pro status

New release '22.04.3 LTS' available.
Run 'do-release-upgrade' to upgrade to it.


*** System restart required ***
Last login: Mon Apr  1 01:40:04 2024 from 192.168.56.1
```

Para parar a VM, execute:

```bash
$  vagrant halt
==> default: Attempting graceful shutdown of VM...
```

Por fim, deve-se executar o seguinte comando para destruir a VM:

```bash
$ vagrant destroy -f
==> default: Destroying VM and associated drives...
```
