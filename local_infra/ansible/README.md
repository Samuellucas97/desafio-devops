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
$ ansible-playbook  -i ./inventory/localhost/hosts.yaml ./playbooks/main.yaml 

PLAY [localhost] ***********************************************************************************

TASK [Gathering Facts] *****************************************************************************
ok: [localhost]

TASK [Update package cache] ************************************************************************
changed: [localhost]

TASK [Upgrade all packages] ************************************************************************
ok: [localhost]

TASK [Install MicroK8s] ****************************************************************************
changed: [localhost]

PLAY RECAP *****************************************************************************************
localhost                  : ok=4    changed=2    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   

```
