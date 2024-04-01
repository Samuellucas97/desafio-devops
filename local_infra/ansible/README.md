# Script Ansible

Este diretórios contém os scripts Ansible relacionado a configuração da  Virtual Machine.

## Requisitos

- Python (version >= 3.8.10)
  - Execute no terminal: `sudo apt install python3.8`.
  - Abra o arquivo `~/.bashrc` e insira `alias python=python3`. Então execute: `source ~/.bashrc`
  - Para checar execute:

```bash
$ python --version
Python 3.8.10
```

- Install Ansible (version >= 2.12.4)

  - Execute no terminal: `sudo apt install ansible`.  
  - Para checar, executeTo check if it was installed: `ansible --version`.

```bash
$ ansible --version
ansible [core 2.13.13]
  config file = /etc/ansible/ansible.cfg
  configured module search path = ['/home/vagrant/.ansible/plugins/modules', '/usr/share/ansible/plugins/modules']
  ansible python module location = /home/vagrant/.local/lib/python3.8/site-packages/ansible
  ansible collection location = /home/vagrant/.ansible/collections:/usr/share/ansible/collections
  executable location = /home/vagrant/.local/bin/ansible
  python version = 3.8.10 (default, Nov 22 2023, 10:22:35) [GCC 9.4.0]
  jinja version = 3.1.3
  libyaml = True
```

## Como executar?

Execute o seguinte comando:

```bash
$ ansible-playbook  -i ./inventory/localhost/hosts.yaml ./playbooks.yaml 

PLAY [localhost] ***************************************************************

TASK [Gathering Facts] *********************************************************
ok: [localhost]

TASK [INSTALL THE COMMON REQUIREMENTS] *****************************************

TASK [common : Update package cache] *******************************************
changed: [localhost]

TASK [common : Upgrade all packages] *******************************************
ok: [localhost]

TASK [common : Install prerequisites for MicroK8s installation] ****************
ok: [localhost] => (item=curl)
ok: [localhost] => (item=iptables)
ok: [localhost] => (item=snapd)

TASK [CREATE AND CONFIGURE A MICROK8S CLUSTER] *********************************

TASK [microk8s : Install MicroK8s using snap] **********************************
changed: [localhost]

TASK [microk8s : Check MicroK8s status] ****************************************
changed: [localhost]

TASK [microk8s : Create .kube directory] ***************************************
ok: [localhost]

TASK [microk8s : Checking if the group exists] *********************************
ok: [localhost]

TASK [microk8s : Add Ansible user to microk8s group] ***************************
ok: [localhost]

TASK [microk8s : Change ownership to Ansible user (and group)] *****************
ok: [localhost]

TASK [microk8s : Add kubectl and helm aliases] *********************************
ok: [localhost] => (item={'alias': 'kubectl', 'command': 'microk8s kubectl'})
ok: [localhost] => (item={'alias': 'helm', 'command': 'microk8s helm'})

TASK [microk8s : Enable add-ons] ***********************************************
changed: [localhost]

TASK [microk8s : Instal Metallb] ***********************************************
changed: [localhost]

TASK [ENABLE KUBERNETES CLUSTER MONITORING] ************************************

TASK [monitoring : Enable MicroK8s monitoring add-ons (metrics-server, observability, and dashboard)] ***
changed: [localhost]

TASK [INSTALL THE KONG INTO THE MICROK8S] **************************************

TASK [kong : Creates a directory for the Gateway CRD configuration file] *******
ok: [localhost]

TASK [kong : Copy the Gateway CRD configuration file] **************************
ok: [localhost]

TASK [kong : Install Kubernetes Gateway API] ***********************************
changed: [localhost]

TASK [kong : Install Kubernetes Gateway CRD] ***********************************
changed: [localhost]

TASK [kong : Add Kong helm repo] ***********************************************
changed: [localhost]

TASK [kong : Update Helm repo] *************************************************
changed: [localhost]

TASK [kong : Check if the Kong namespace exists] *******************************
changed: [localhost]

TASK [kong : Install KIC Helm] *************************************************
skipping: [localhost]

TASK [INSTALL ARGO CD INTO THE MICROK8S] ***************************************

TASK [argocd : Creates a directory for the Apllication.yaml Kubernetes configuration file] ***
ok: [localhost]

TASK [argocd : Copy the Gateway CRD configuration file] ************************
ok: [localhost]

TASK [argocd : Create namespace argocd] ****************************************
fatal: [localhost]: FAILED! => {"changed": true, "cmd": ["microk8s.kubectl", "create", "namespace", "argocd"], "delta": "0:00:02.898286", "end": "2024-04-01 08:38:06.886221", "msg": "non-zero return code", "rc": 1, "start": "2024-04-01 08:38:03.987935", "stderr": "Error from server (AlreadyExists): namespaces \"argocd\" already exists", "stderr_lines": ["Error from server (AlreadyExists): namespaces \"argocd\" already exists"], "stdout": "", "stdout_lines": []}
...ignoring

TASK [argocd : Deploy Argo CD into MicroK8s] ***********************************
changed: [localhost]

TASK [argocd : Deploy Argo CD Flask Application into the MicroK8s] *************
changed: [localhost]

PLAY RECAP *********************************************************************
localhost                  : ok=26   changed=14   unreachable=0    failed=0    skipped=1    rescued=0    ignored=1 

```
