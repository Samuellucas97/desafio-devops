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

Para destruir a VM, basta executar o comando abaixo:

```bash
$ make clean

******************** DESTROYING THE VIRTUAL MACHINE **********************************
vagrant destroy -f
==> default: Forcing shutdown of VM...
==> default: Destroying VM and associated drives...

vagrant status
Current machine states:

default                   not created (virtualbox)

The environment has not yet been created. Run `vagrant up` to
create the environment. If a machine is not created, only the
default provider will be shown. So if a provider is not listed,
then the machine is not created for that environment.

```

## Usando comandos Vagrant

Para subir a VM, use o seguinte comando:

```bash
$ vagrant up
Bringing machine 'default' up with 'virtualbox' provider...
==> default: Importing base box 'ubuntu/focal64'...
==> default: Matching MAC address for NAT networking...
==> default: Checking if box 'ubuntu/focal64' version '20240306.0.0' is up to date...
==> default: Setting the name of the VM: local_infra_default_1711413417008_84675
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
    default: Warning: Remote connection disconnect. Retrying...
    default: Warning: Connection reset. Retrying...
    default: 
    default: Vagrant insecure key detected. Vagrant will automatically replace
    default: this with a newly generated keypair for better security.
    default: 
    default: Inserting generated public key within guest...
    default: Removing insecure key from the guest if it is present...
    default: Key inserted! Disconnecting and reconnecting using new SSH key...
==> default: Machine booted and ready!
==> default: Checking for guest additions in VM...
==> default: Configuring and enabling network interfaces...
==> default: Mounting shared folders...
    default: /vagrant => /home/samuel/Music/desafio-devops/local_infra
==> default: Running provisioner: shell...
    default: Running: inline script
    default: Hit:1 http://archive.ubuntu.com/ubuntu focal InRelease
    default: Get:2 http://security.ubuntu.com/ubuntu focal-security InRelease [114 kB]
    default: Get:3 http://archive.ubuntu.com/ubuntu focal-updates InRelease [114 kB]
    default: Get:4 http://security.ubuntu.com/ubuntu focal-security/main amd64 Packages [2815 kB]
    default: Get:5 http://archive.ubuntu.com/ubuntu focal-backports InRelease [108 kB]
    default: Get:6 http://archive.ubuntu.com/ubuntu focal/universe amd64 Packages [8628 kB]
    default: Get:7 http://security.ubuntu.com/ubuntu focal-security/main Translation-en [427 kB]
    default: Get:8 http://security.ubuntu.com/ubuntu focal-security/restricted amd64 Packages [2690 kB]
    default: Get:9 http://security.ubuntu.com/ubuntu focal-security/restricted Translation-en [376 kB]
    default: Get:10 http://security.ubuntu.com/ubuntu focal-security/universe amd64 Packages [952 kB]
    default: Get:11 http://security.ubuntu.com/ubuntu focal-security/universe Translation-en [200 kB]
    default: Get:12 http://security.ubuntu.com/ubuntu focal-security/universe amd64 c-n-f Metadata [19.2 kB]
    default: Get:13 http://security.ubuntu.com/ubuntu focal-security/multiverse amd64 Packages [23.9 kB]
    default: Get:14 http://security.ubuntu.com/ubuntu focal-security/multiverse Translation-en [5796 B]
    default: Get:15 http://security.ubuntu.com/ubuntu focal-security/multiverse amd64 c-n-f Metadata [548 B]
    default: Get:16 http://archive.ubuntu.com/ubuntu focal/universe Translation-en [5124 kB]
    default: Get:17 http://archive.ubuntu.com/ubuntu focal/universe amd64 c-n-f Metadata [265 kB]
    default: Get:18 http://archive.ubuntu.com/ubuntu focal/multiverse amd64 Packages [144 kB]
    default: Get:19 http://archive.ubuntu.com/ubuntu focal/multiverse Translation-en [104 kB]
    default: Get:20 http://archive.ubuntu.com/ubuntu focal/multiverse amd64 c-n-f Metadata [9136 B]
    default: Get:21 http://archive.ubuntu.com/ubuntu focal-updates/main amd64 Packages [3192 kB]
    default: Get:22 http://archive.ubuntu.com/ubuntu focal-updates/main Translation-en [509 kB]
    default: Get:23 http://archive.ubuntu.com/ubuntu focal-updates/restricted amd64 Packages [2807 kB]
    default: Get:24 http://archive.ubuntu.com/ubuntu focal-updates/restricted Translation-en [391 kB]
    default: Get:25 http://archive.ubuntu.com/ubuntu focal-updates/universe amd64 Packages [1177 kB]
    default: Get:26 http://archive.ubuntu.com/ubuntu focal-updates/universe Translation-en [282 kB]
    default: Get:27 http://archive.ubuntu.com/ubuntu focal-updates/universe amd64 c-n-f Metadata [25.7 kB]
    default: Get:28 http://archive.ubuntu.com/ubuntu focal-updates/multiverse amd64 Packages [26.1 kB]
    default: Get:29 http://archive.ubuntu.com/ubuntu focal-updates/multiverse Translation-en [7768 B]
    default: Get:30 http://archive.ubuntu.com/ubuntu focal-updates/multiverse amd64 c-n-f Metadata [620 B]
    default: Get:31 http://archive.ubuntu.com/ubuntu focal-backports/main amd64 Packages [45.7 kB]
    default: Get:32 http://archive.ubuntu.com/ubuntu focal-backports/main Translation-en [16.3 kB]
    default: Get:33 http://archive.ubuntu.com/ubuntu focal-backports/main amd64 c-n-f Metadata [1420 B]
    default: Get:34 http://archive.ubuntu.com/ubuntu focal-backports/restricted amd64 c-n-f Metadata [116 B]
    default: Get:35 http://archive.ubuntu.com/ubuntu focal-backports/universe amd64 Packages [25.0 kB]
    default: Get:36 http://archive.ubuntu.com/ubuntu focal-backports/universe Translation-en [16.3 kB]
    default: Get:37 http://archive.ubuntu.com/ubuntu focal-backports/universe amd64 c-n-f Metadata [880 B]
    default: Get:38 http://archive.ubuntu.com/ubuntu focal-backports/multiverse amd64 c-n-f Metadata [116 B]
    default: Fetched 30.6 MB in 8s (4010 kB/s)
    default: Reading package lists...
    default: Reading package lists...
    default: Building dependency tree...
    default: Reading state information...
    default: Calculating upgrade...
    default: The following packages have been kept back:
    default:   linux-headers-generic linux-headers-virtual linux-image-virtual
    default:   linux-virtual ubuntu-advantage-tools ubuntu-pro-client-l10n
    default: The following packages will be upgraded:
    default:   accountsservice libaccountsservice0 python3-update-manager
    default:   update-manager-core vim vim-common vim-runtime vim-tiny xxd
    default: 9 upgraded, 0 newly installed, 0 to remove and 6 not upgraded.
    default: Need to get 8027 kB of archives.
    default: After this operation, 4096 B of additional disk space will be used.
    default: Get:1 http://archive.ubuntu.com/ubuntu focal-updates/main amd64 vim amd64 2:8.1.2269-1ubuntu5.22 [1243 kB]
    default: Get:2 http://archive.ubuntu.com/ubuntu focal-updates/main amd64 vim-tiny amd64 2:8.1.2269-1ubuntu5.22 [582 kB]
    default: Get:3 http://archive.ubuntu.com/ubuntu focal-updates/main amd64 vim-runtime all 2:8.1.2269-1ubuntu5.22 [5877 kB]
    default: Get:4 http://archive.ubuntu.com/ubuntu focal-updates/main amd64 xxd amd64 2:8.1.2269-1ubuntu5.22 [53.2 kB]
    default: Get:5 http://archive.ubuntu.com/ubuntu focal-updates/main amd64 vim-common all 2:8.1.2269-1ubuntu5.22 [88.2 kB]
    default: Get:6 http://archive.ubuntu.com/ubuntu focal-updates/main amd64 accountsservice amd64 0.6.55-0ubuntu12~20.04.7 [61.3 kB]
    default: Get:7 http://archive.ubuntu.com/ubuntu focal-updates/main amd64 libaccountsservice0 amd64 0.6.55-0ubuntu12~20.04.7 [72.4 kB]
    default: Get:8 http://archive.ubuntu.com/ubuntu focal-updates/main amd64 python3-update-manager all 1:20.04.10.20 [38.4 kB]
    default: Get:9 http://archive.ubuntu.com/ubuntu focal-updates/main amd64 update-manager-core all 1:20.04.10.20 [11.6 kB]
    default: dpkg-preconfigure: unable to re-open stdin: No such file or directory
    default: Fetched 8027 kB in 1s (5501 kB/s)
(Reading database ... 63758 files and directories currently installed.)
    default: Preparing to unpack .../0-vim_2%3a8.1.2269-1ubuntu5.22_amd64.deb ...
    default: Unpacking vim (2:8.1.2269-1ubuntu5.22) over (2:8.1.2269-1ubuntu5.21) ...
    default: Preparing to unpack .../1-vim-tiny_2%3a8.1.2269-1ubuntu5.22_amd64.deb ...
    default: Unpacking vim-tiny (2:8.1.2269-1ubuntu5.22) over (2:8.1.2269-1ubuntu5.21) ...
    default: Preparing to unpack .../2-vim-runtime_2%3a8.1.2269-1ubuntu5.22_all.deb ...
    default: Unpacking vim-runtime (2:8.1.2269-1ubuntu5.22) over (2:8.1.2269-1ubuntu5.21) ...
    default: Preparing to unpack .../3-xxd_2%3a8.1.2269-1ubuntu5.22_amd64.deb ...
    default: Unpacking xxd (2:8.1.2269-1ubuntu5.22) over (2:8.1.2269-1ubuntu5.21) ...
    default: Preparing to unpack .../4-vim-common_2%3a8.1.2269-1ubuntu5.22_all.deb ...
    default: Unpacking vim-common (2:8.1.2269-1ubuntu5.22) over (2:8.1.2269-1ubuntu5.21) ...
    default: Preparing to unpack .../5-accountsservice_0.6.55-0ubuntu12~20.04.7_amd64.deb ...
    default: Unpacking accountsservice (0.6.55-0ubuntu12~20.04.7) over (0.6.55-0ubuntu12~20.04.6) ...
    default: Preparing to unpack .../6-libaccountsservice0_0.6.55-0ubuntu12~20.04.7_amd64.deb ...
    default: Unpacking libaccountsservice0:amd64 (0.6.55-0ubuntu12~20.04.7) over (0.6.55-0ubuntu12~20.04.6) ...
    default: Preparing to unpack .../7-python3-update-manager_1%3a20.04.10.20_all.deb ...
    default: Unpacking python3-update-manager (1:20.04.10.20) over (1:20.04.10.18) ...
    default: Preparing to unpack .../8-update-manager-core_1%3a20.04.10.20_all.deb ...
    default: Unpacking update-manager-core (1:20.04.10.20) over (1:20.04.10.18) ...
    default: Setting up xxd (2:8.1.2269-1ubuntu5.22) ...
    default: Setting up vim-common (2:8.1.2269-1ubuntu5.22) ...
    default: Setting up python3-update-manager (1:20.04.10.20) ...
    default: Setting up libaccountsservice0:amd64 (0.6.55-0ubuntu12~20.04.7) ...
    default: Setting up vim-runtime (2:8.1.2269-1ubuntu5.22) ...
    default: Setting up accountsservice (0.6.55-0ubuntu12~20.04.7) ...
    default: Setting up vim (2:8.1.2269-1ubuntu5.22) ...
    default: Setting up vim-tiny (2:8.1.2269-1ubuntu5.22) ...
    default: Setting up update-manager-core (1:20.04.10.20) ...
    default: Processing triggers for libc-bin (2.31-0ubuntu9.14) ...
    default: Processing triggers for man-db (2.9.1-1) ...
    default: Processing triggers for dbus (1.12.16-2ubuntu2.3) ...
    default: Processing triggers for mime-support (3.64ubuntu1) ...
    default: microk8s (1.27/stable) v1.27.11 from Canonical** installed
    default: microk8s is running
    default: high-availability: no
    default:   datastore master nodes: 127.0.0.1:19001
    default:   datastore standby nodes: none
    default: addons:
    default:   enabled:
    default:     dns                  # (core) CoreDNS
    default:     ha-cluster           # (core) Configure high availability on the current node
    default:     helm                 # (core) Helm - the package manager for Kubernetes
    default:     helm3                # (core) Helm 3 - the package manager for Kubernetes
    default:   disabled:
    default:     cert-manager         # (core) Cloud native certificate management
    default:     community            # (core) The community addons repository
    default:     dashboard            # (core) The Kubernetes dashboard
    default:     gpu                  # (core) Automatic enablement of Nvidia CUDA
    default:     host-access          # (core) Allow Pods connecting to Host services smoothly
    default:     hostpath-storage     # (core) Storage class; allocates storage from host directory
    default:     ingress              # (core) Ingress controller for external access
    default:     kube-ovn             # (core) An advanced network fabric for Kubernetes
    default:     mayastor             # (core) OpenEBS MayaStor
    default:     metallb              # (core) Loadbalancer for your Kubernetes cluster
    default:     metrics-server       # (core) K8s Metrics Server for API access to service metrics
    default:     minio                # (core) MinIO object storage
    default:     observability        # (core) A lightweight observability stack for logs, traces and metrics
    default:     prometheus           # (core) Prometheus operator for monitoring and logging
    default:     rbac                 # (core) Role-Based Access Control for authorisation
    default:     registry             # (core) Private image registry exposed on localhost:32000
    default:     storage              # (core) Alias to hostpath-storage add-on, deprecated

$ vagrant ssh
Welcome to Ubuntu 20.04.6 LTS (GNU/Linux 5.4.0-173-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/pro

  System information as of Tue Mar 26 00:42:10 UTC 2024

  System load:  0.15              Processes:               163
  Usage of /:   7.5% of 38.70GB   Users logged in:         0
  Memory usage: 20%               IPv4 address for enp0s3: 10.0.2.15
  Swap usage:   0%                IPv4 address for enp0s8: 192.168.56.10


Expanded Security Maintenance for Applications is not enabled.

11 updates can be applied immediately.
8 of these updates are standard security updates.
To see these additional updates run: apt list --upgradable

Enable ESM Apps to receive additional future security updates.
See https://ubuntu.com/esm or run: sudo pro status

New release '22.04.3 LTS' available.
Run 'do-release-upgrade' to upgrade to it.
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
