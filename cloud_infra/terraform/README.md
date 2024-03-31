# Terraform scripts

Este diretório contem os scripts para criação de infraestrutura na AWS.

## Requisitos

- Terraform
  - Como instalar? `sudo apt install terraform`. Para mais informações: [documentação oficial](https://developer.hashicorp.com/terraform/tutorials/aws-get-started/install-cli)
- AWS CLI
  - Como instalar? 

```bash
$ curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
$ unzip awscliv2.zip
$ sudo ./aws/install
You can now run: /usr/local/bin/aws --version
```

## Como executar?

Execute os seguintes comandos para criação da infraestrutura:

```bash
$ terraform init
Initializing the backend...

Initializing provider plugins...
- Reusing previous version of hashicorp/aws from the dependency lock file
- Using previously-installed hashicorp/aws v5.43.0

Terraform has been successfully initialized!

You may now begin working with Terraform. Try running "terraform plan" to see
any changes that are required for your infrastructure. All Terraform commands
should now work.

If you ever set or change modules or backend configuration for Terraform,
rerun this command to reinitialize your working directory. If you forget, other
commands will detect it and remind you to do so if necessary.

$ terraform validate
Success! The configuration is valid.

$ terraform plan -out=tfplan

Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the
following symbols:
  + create

Terraform will perform the following actions:

  # aws_instance.desafio_devops_ec2_instance will be created
  + resource "aws_instance" "desafio_devops_ec2_instance" {
      + ami                                  = "ami-0b4750268a88e78e0"
      + arn                                  = (known after apply)
      + associate_public_ip_address          = (known after apply)
      + availability_zone                    = (known after apply)
      + cpu_core_count                       = (known after apply)
      + cpu_threads_per_core                 = (known after apply)
      + disable_api_stop                     = (known after apply)
      + disable_api_termination              = (known after apply)
      + ebs_optimized                        = (known after apply)
      + get_password_data                    = false
      + host_id                              = (known after apply)
      + host_resource_group_arn              = (known after apply)
      + iam_instance_profile                 = (known after apply)
      + id                                   = (known after apply)
      + instance_initiated_shutdown_behavior = (known after apply)
      + instance_lifecycle                   = (known after apply)
      + instance_state                       = (known after apply)
      + instance_type                        = "t2.micro"
      + ipv6_address_count                   = (known after apply)
      + ipv6_addresses                       = (known after apply)
      + key_name                             = "desafio_devops_key_pair"
      + monitoring                           = (known after apply)
      + outpost_arn                          = (known after apply)
      + password_data                        = (known after apply)
      + placement_group                      = (known after apply)
      + placement_partition_number           = (known after apply)
      + primary_network_interface_id         = (known after apply)
      + private_dns                          = (known after apply)
      + private_ip                           = (known after apply)
      + public_dns                           = (known after apply)
      + public_ip                            = (known after apply)
      + secondary_private_ips                = (known after apply)
      + security_groups                      = [
          + "desafio_devops_security_group",
        ]
      + source_dest_check                    = true
      + spot_instance_request_id             = (known after apply)
      + subnet_id                            = (known after apply)
      + tags                                 = {
          + "Name" = "DesafioDevOpsEC2Instance"
        }
      + tags_all                             = {
          + "Name" = "DesafioDevOpsEC2Instance"
        }
      + tenancy                              = (known after apply)
      + user_data                            = (known after apply)
      + user_data_base64                     = (known after apply)
      + user_data_replace_on_change          = false
      + vpc_security_group_ids               = (known after apply)
    }

  # aws_internet_gateway.desafio_devops_igw will be created
  + resource "aws_internet_gateway" "desafio_devops_igw" {
      + arn      = (known after apply)
      + id       = (known after apply)
      + owner_id = (known after apply)
      + tags_all = (known after apply)
      + vpc_id   = (known after apply)
    }

  # aws_key_pair.devops_cha will be created
  + resource "aws_key_pair" "devops_cha" {
      + arn             = (known after apply)
      + fingerprint     = (known after apply)
      + id              = (known after apply)
      + key_name        = "desafio_devops_key_pair"
      + key_name_prefix = (known after apply)
      + key_pair_id     = (known after apply)
      + key_type        = (known after apply)
      + public_key      = "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDJiZyzyfZ7s/2evxuFrbAG8HsOGUAMXYcXOASMxy3zqtZ/qEvkLEUGEZ0WH2Gh0kTLUbbJeZLHv/BABiBEw2Wf+kGuoOq814F7jB59lpm3yJ6CGxBh8ngu3QbEWTZ165kP5xIKL/D3AQ6TXWw8v5gOrjPGSmutNK/erweUcmdUpQ7OQEz8V9+SzfetbotkNRloZlZsCE1HF+SN7WN7SROSy9xmwVT8rtOwGcu9xzCNycnZmjFwe0eec+um8/eAqsjPgaZYNbprJ7r8Tb6C1pP7ei1f2yhAEuZWy1SGwyIEm9CA0+t++wFa64YRhl4//se6S14PfAHrwWGnYgHdItYJnxNwVSNPerN0fvWL6EpW6aSOWj9t7TcCzldq4+rybJYJCNs0l43sxsTIkopDys7cRxRZL3Xjl08tmUUk1YkDUPu0KBnIXYK6YeLRxvu/xOPxeUrEyLH1oesspoSukDlhGHZQGGk9xM7bgJGqWoSmvY2QGS1olEGtGIR8zbIHHlM= samuel@samuellucas97-hp-250-g8-notebook-pc"
      + tags_all        = (known after apply)
    }

  # aws_route_table.desafio_devops_route_table will be created
  + resource "aws_route_table" "desafio_devops_route_table" {
      + arn              = (known after apply)
      + id               = (known after apply)
      + owner_id         = (known after apply)
      + propagating_vgws = (known after apply)
      + route            = [
          + {
              + carrier_gateway_id         = ""
              + cidr_block                 = "0.0.0.0/0"
              + core_network_arn           = ""
              + destination_prefix_list_id = ""
              + egress_only_gateway_id     = ""
              + gateway_id                 = (known after apply)
              + ipv6_cidr_block            = ""
              + local_gateway_id           = ""
              + nat_gateway_id             = ""
              + network_interface_id       = ""
              + transit_gateway_id         = ""
              + vpc_endpoint_id            = ""
              + vpc_peering_connection_id  = ""
            },
        ]
      + tags_all         = (known after apply)
      + vpc_id           = (known after apply)
    }

  # aws_route_table_association.desafio_devops_route_table_association will be created
  + resource "aws_route_table_association" "desafio_devops_route_table_association" {
      + id             = (known after apply)
      + route_table_id = (known after apply)
      + subnet_id      = (known after apply)
    }

  # aws_security_group.desafio_devops_security_group will be created
  + resource "aws_security_group" "desafio_devops_security_group" {
      + arn                    = (known after apply)
      + description            = "Allow SSH and HTTP requests - inboud traffic"
      + egress                 = [
          + {
              + cidr_blocks      = [
                  + "0.0.0.0/0",
                ]
              + description      = ""
              + from_port        = 0
              + ipv6_cidr_blocks = []
              + prefix_list_ids  = []
              + protocol         = "-1"
              + security_groups  = []
              + self             = false
              + to_port          = 0
            },
        ]
      + id                     = (known after apply)
      + ingress                = [
          + {
              + cidr_blocks      = [
                  + "0.0.0.0/0",
                ]
              + description      = ""
              + from_port        = 2222
              + ipv6_cidr_blocks = []
              + prefix_list_ids  = []
              + protocol         = "tcp"
              + security_groups  = []
              + self             = false
              + to_port          = 22
            },
          + {
              + cidr_blocks      = [
                  + "0.0.0.0/0",
                ]
              + description      = ""
              + from_port        = 80
              + ipv6_cidr_blocks = []
              + prefix_list_ids  = []
              + protocol         = "tcp"
              + security_groups  = []
              + self             = false
              + to_port          = 80
            },
        ]
      + name                   = "desafio_devops_security_group"
      + name_prefix            = (known after apply)
      + owner_id               = (known after apply)
      + revoke_rules_on_delete = false
      + tags_all               = (known after apply)
      + vpc_id                 = (known after apply)
    }

  # aws_subnet.desafio_devops_public_subnet will be created
  + resource "aws_subnet" "desafio_devops_public_subnet" {
      + arn                                            = (known after apply)
      + assign_ipv6_address_on_creation                = false
      + availability_zone                              = (known after apply)
      + availability_zone_id                           = (known after apply)
      + cidr_block                                     = "10.0.0.0/16"
      + enable_dns64                                   = false
      + enable_resource_name_dns_a_record_on_launch    = false
      + enable_resource_name_dns_aaaa_record_on_launch = false
      + id                                             = (known after apply)
      + ipv6_cidr_block_association_id                 = (known after apply)
      + ipv6_native                                    = false
      + map_public_ip_on_launch                        = true
      + owner_id                                       = (known after apply)
      + private_dns_hostname_type_on_launch            = (known after apply)
      + tags_all                                       = (known after apply)
      + vpc_id                                         = (known after apply)
    }

  # aws_vpc.desafio_devops_vpc will be created
  + resource "aws_vpc" "desafio_devops_vpc" {
      + arn                                  = (known after apply)
      + cidr_block                           = "10.0.0.0/16"
      + default_network_acl_id               = (known after apply)
      + default_route_table_id               = (known after apply)
      + default_security_group_id            = (known after apply)
      + dhcp_options_id                      = (known after apply)
      + enable_dns_hostnames                 = (known after apply)
      + enable_dns_support                   = true
      + enable_network_address_usage_metrics = (known after apply)
      + id                                   = (known after apply)
      + instance_tenancy                     = "default"
      + ipv6_association_id                  = (known after apply)
      + ipv6_cidr_block                      = (known after apply)
      + ipv6_cidr_block_network_border_group = (known after apply)
      + main_route_table_id                  = (known after apply)
      + owner_id                             = (known after apply)
      + tags_all                             = (known after apply)
    }

Plan: 8 to add, 0 to change, 0 to destroy.

Changes to Outputs:
  + instance_id = (known after apply)
  + public_ip   = (known after apply)

──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────

Saved the plan to: tfplan

To perform exactly these actions, run the following command to apply:
    terraform apply "tfplan"
$ terraform apply "tfplan"
aws_vpc.desafio_devops_vpc: Creating...
aws_vpc.desafio_devops_vpc: Creation complete after 3s [id=vpc-019aa49b4a7e284a0]
aws_internet_gateway.desafio_devops_igw: Creating...
aws_subnet.desafio_devops_public_subnet: Creating...
aws_security_group.desafio_devops_security_group: Creating...
aws_internet_gateway.desafio_devops_igw: Creation complete after 1s [id=igw-0789c6eb86438c218]
aws_route_table.desafio_devops_route_table: Creating...
aws_route_table.desafio_devops_route_table: Creation complete after 1s [id=rtb-02af8b09f1c92a7a3]
aws_security_group.desafio_devops_security_group: Creation complete after 3s [id=sg-0ce0ba32f7f4170fb]
aws_subnet.desafio_devops_public_subnet: Still creating... [10s elapsed]
aws_subnet.desafio_devops_public_subnet: Creation complete after 12s [id=subnet-0552400a0fc6c7bbf]
aws_route_table_association.desafio_devops_route_table_association: Creating...
aws_instance.desafio_devops_ec2_instance: Creating...
aws_route_table_association.desafio_devops_route_table_association: Creation complete after 1s [id=rtbassoc-0744e75230e52372b]
aws_instance.desafio_devops_ec2_instance: Still creating... [10s elapsed]
aws_instance.desafio_devops_ec2_instance: Still creating... [20s elapsed]
aws_instance.desafio_devops_ec2_instance: Still creating... [30s elapsed]
aws_instance.desafio_devops_ec2_instance: Still creating... [40s elapsed]
aws_instance.desafio_devops_ec2_instance: Creation complete after 45s [id=i-09702e15aedb96421]

Apply complete! Resources: 7 added, 0 changed, 0 destroyed.

Outputs:

instance_id = "i-09702e15aedb96421"
public_ip = "18.117.96.107"
```

Para acessar a máquina, use o seguinte commando SSH, atentando para o public_ip:

```bash
$ ssh -i ~/.ssh/id_rsa ubuntu@18.117.96.107
The authenticity of host '18.117.96.107 (18.117.96.107)' can't be established.
ED25519 key fingerprint is SHA256:4MaZje1NSZXWe/4LBizgpPi/eg5Wjmxz+6c9Wxr1kwI.
This key is not known by any other names
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '18.117.96.107' (ED25519) to the list of known hosts.
Welcome to Ubuntu 20.04.6 LTS (GNU/Linux 5.15.0-1055-aws x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/pro

  System information as of Sun Mar 31 07:40:59 UTC 2024

  System load:  0.24              Processes:             99
  Usage of /:   21.2% of 7.57GB   Users logged in:       0
  Memory usage: 22%               IPv4 address for eth0: 10.0.250.5
  Swap usage:   0%

Expanded Security Maintenance for Applications is not enabled.

0 updates can be applied immediately.

Enable ESM Apps to receive additional future security updates.
See https://ubuntu.com/esm or run: sudo pro status


The list of available updates is more than a week old.
To check for new updates run: sudo apt update


The programs included with the Ubuntu system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Ubuntu comes with ABSOLUTELY NO WARRANTY, to the extent permitted by
applicable law.

To run a command as administrator (user "root"), use "sudo <command>".
See "man sudo_root" for details.
```

Para remover a infraestrutura, execute:

```bash
$ terraform destroy -auto-approve
aws_key_pair.devops_cha: Refreshing state... [id=desafio_devops_key_pair]
aws_vpc.desafio_devops_vpc: Refreshing state... [id=vpc-019aa49b4a7e284a0]
aws_internet_gateway.desafio_devops_igw: Refreshing state... [id=igw-0789c6eb86438c218]
aws_subnet.desafio_devops_public_subnet: Refreshing state... [id=subnet-0552400a0fc6c7bbf]
aws_security_group.desafio_devops_security_group: Refreshing state... [id=sg-0ce0ba32f7f4170fb]
aws_route_table.desafio_devops_route_table: Refreshing state... [id=rtb-02af8b09f1c92a7a3]
aws_instance.desafio_devops_ec2_instance: Refreshing state... [id=i-09702e15aedb96421]
aws_route_table_association.desafio_devops_route_table_association: Refreshing state... [id=rtbassoc-0744e75230e52372b]

Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the
following symbols:
  - destroy

Terraform will perform the following actions:

  # aws_instance.desafio_devops_ec2_instance will be destroyed
  - resource "aws_instance" "desafio_devops_ec2_instance" {
      - ami                                  = "ami-0b4750268a88e78e0" -> null
      - arn                                  = "arn:aws:ec2:us-east-2:851725465376:instance/i-09702e15aedb96421" -> null
      - associate_public_ip_address          = true -> null
      - availability_zone                    = "us-east-2b" -> null
      - cpu_core_count                       = 1 -> null
      - cpu_threads_per_core                 = 1 -> null
      - disable_api_stop                     = false -> null
      - disable_api_termination              = false -> null
      - ebs_optimized                        = false -> null
      - get_password_data                    = false -> null
      - hibernation                          = false -> null
      - id                                   = "i-09702e15aedb96421" -> null
      - instance_initiated_shutdown_behavior = "stop" -> null
      - instance_state                       = "running" -> null
      - instance_type                        = "t2.micro" -> null
      - ipv6_address_count                   = 0 -> null
      - ipv6_addresses                       = [] -> null
      - key_name                             = "desafio_devops_key_pair" -> null
      - monitoring                           = false -> null
      - placement_partition_number           = 0 -> null
      - primary_network_interface_id         = "eni-0ceb9435d17f0047f" -> null
      - private_dns                          = "ip-10-0-250-5.us-east-2.compute.internal" -> null
      - private_ip                           = "10.0.250.5" -> null
      - public_ip                            = "18.117.96.107" -> null
      - secondary_private_ips                = [] -> null
      - security_groups                      = [] -> null
      - source_dest_check                    = true -> null
      - subnet_id                            = "subnet-0552400a0fc6c7bbf" -> null
      - tags                                 = {
          - "Name" = "DesafioDevOpsEC2Instance"
        } -> null
      - tags_all                             = {
          - "Name" = "DesafioDevOpsEC2Instance"
        } -> null
      - tenancy                              = "default" -> null
      - user_data_replace_on_change          = false -> null
      - vpc_security_group_ids               = [
          - "sg-0ce0ba32f7f4170fb",
        ] -> null

      - capacity_reservation_specification {
          - capacity_reservation_preference = "open" -> null
        }

      - cpu_options {
          - core_count       = 1 -> null
          - threads_per_core = 1 -> null
        }

      - credit_specification {
          - cpu_credits = "standard" -> null
        }

      - enclave_options {
          - enabled = false -> null
        }

      - maintenance_options {
          - auto_recovery = "default" -> null
        }

      - metadata_options {
          - http_endpoint               = "enabled" -> null
          - http_protocol_ipv6          = "disabled" -> null
          - http_put_response_hop_limit = 1 -> null
          - http_tokens                 = "optional" -> null
          - instance_metadata_tags      = "disabled" -> null
        }

      - private_dns_name_options {
          - enable_resource_name_dns_a_record    = false -> null
          - enable_resource_name_dns_aaaa_record = false -> null
          - hostname_type                        = "ip-name" -> null
        }

      - root_block_device {
          - delete_on_termination = true -> null
          - device_name           = "/dev/sda1" -> null
          - encrypted             = false -> null
          - iops                  = 100 -> null
          - tags                  = {} -> null
          - tags_all              = {} -> null
          - throughput            = 0 -> null
          - volume_id             = "vol-05373119acf52ffdc" -> null
          - volume_size           = 8 -> null
          - volume_type           = "gp2" -> null
        }
    }

  # aws_internet_gateway.desafio_devops_igw will be destroyed
  - resource "aws_internet_gateway" "desafio_devops_igw" {
      - arn      = "arn:aws:ec2:us-east-2:851725465376:internet-gateway/igw-0789c6eb86438c218" -> null
      - id       = "igw-0789c6eb86438c218" -> null
      - owner_id = "851725465376" -> null
      - tags     = {} -> null
      - tags_all = {} -> null
      - vpc_id   = "vpc-019aa49b4a7e284a0" -> null
    }

  # aws_key_pair.devops_cha will be destroyed
  - resource "aws_key_pair" "devops_cha" {
      - arn         = "arn:aws:ec2:us-east-2:851725465376:key-pair/desafio_devops_key_pair" -> null
      - fingerprint = "60:52:27:47:ba:ef:31:5a:a6:5c:20:47:41:c8:ae:98" -> null
      - id          = "desafio_devops_key_pair" -> null
      - key_name    = "desafio_devops_key_pair" -> null
      - key_pair_id = "key-0fa597032ff78ff01" -> null
      - key_type    = "rsa" -> null
      - public_key  = "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDJiZyzyfZ7s/2evxuFrbAG8HsOGUAMXYcXOASMxy3zqtZ/qEvkLEUGEZ0WH2Gh0kTLUbbJeZLHv/BABiBEw2Wf+kGuoOq814F7jB59lpm3yJ6CGxBh8ngu3QbEWTZ165kP5xIKL/D3AQ6TXWw8v5gOrjPGSmutNK/erweUcmdUpQ7OQEz8V9+SzfetbotkNRloZlZsCE1HF+SN7WN7SROSy9xmwVT8rtOwGcu9xzCNycnZmjFwe0eec+um8/eAqsjPgaZYNbprJ7r8Tb6C1pP7ei1f2yhAEuZWy1SGwyIEm9CA0+t++wFa64YRhl4//se6S14PfAHrwWGnYgHdItYJnxNwVSNPerN0fvWL6EpW6aSOWj9t7TcCzldq4+rybJYJCNs0l43sxsTIkopDys7cRxRZL3Xjl08tmUUk1YkDUPu0KBnIXYK6YeLRxvu/xOPxeUrEyLH1oesspoSukDlhGHZQGGk9xM7bgJGqWoSmvY2QGS1olEGtGIR8zbIHHlM= samuel@samuellucas97-hp-250-g8-notebook-pc" -> null
      - tags        = {} -> null
      - tags_all    = {} -> null
    }

  # aws_route_table.desafio_devops_route_table will be destroyed
  - resource "aws_route_table" "desafio_devops_route_table" {
      - arn              = "arn:aws:ec2:us-east-2:851725465376:route-table/rtb-02af8b09f1c92a7a3" -> null
      - id               = "rtb-02af8b09f1c92a7a3" -> null
      - owner_id         = "851725465376" -> null
      - propagating_vgws = [] -> null
      - route            = [
          - {
              - carrier_gateway_id         = ""
              - cidr_block                 = "0.0.0.0/0"
              - core_network_arn           = ""
              - destination_prefix_list_id = ""
              - egress_only_gateway_id     = ""
              - gateway_id                 = "igw-0789c6eb86438c218"
              - ipv6_cidr_block            = ""
              - local_gateway_id           = ""
              - nat_gateway_id             = ""
              - network_interface_id       = ""
              - transit_gateway_id         = ""
              - vpc_endpoint_id            = ""
              - vpc_peering_connection_id  = ""
            },
        ] -> null
      - tags             = {} -> null
      - tags_all         = {} -> null
      - vpc_id           = "vpc-019aa49b4a7e284a0" -> null
    }

  # aws_route_table_association.desafio_devops_route_table_association will be destroyed
  - resource "aws_route_table_association" "desafio_devops_route_table_association" {
      - id             = "rtbassoc-0744e75230e52372b" -> null
      - route_table_id = "rtb-02af8b09f1c92a7a3" -> null
      - subnet_id      = "subnet-0552400a0fc6c7bbf" -> null
    }

  # aws_security_group.desafio_devops_security_group will be destroyed
  - resource "aws_security_group" "desafio_devops_security_group" {
      - arn                    = "arn:aws:ec2:us-east-2:851725465376:security-group/sg-0ce0ba32f7f4170fb" -> null
      - description            = "Allow SSH and HTTP requests - inboud traffic" -> null
      - egress                 = [
          - {
              - cidr_blocks      = [
                  - "0.0.0.0/0",
                ]
              - description      = ""
              - from_port        = 0
              - ipv6_cidr_blocks = []
              - prefix_list_ids  = []
              - protocol         = "-1"
              - security_groups  = []
              - self             = false
              - to_port          = 0
            },
        ] -> null
      - id                     = "sg-0ce0ba32f7f4170fb" -> null
      - ingress                = [
          - {
              - cidr_blocks      = [
                  - "0.0.0.0/0",
                ]
              - description      = ""
              - from_port        = 22
              - ipv6_cidr_blocks = []
              - prefix_list_ids  = []
              - protocol         = "tcp"
              - security_groups  = []
              - self             = false
              - to_port          = 22
            },
          - {
              - cidr_blocks      = [
                  - "0.0.0.0/0",
                ]
              - description      = ""
              - from_port        = 80
              - ipv6_cidr_blocks = []
              - prefix_list_ids  = []
              - protocol         = "tcp"
              - security_groups  = []
              - self             = false
              - to_port          = 80
            },
        ] -> null
      - name                   = "desafio_devops_security_group" -> null
      - owner_id               = "851725465376" -> null
      - revoke_rules_on_delete = false -> null
      - tags                   = {} -> null
      - tags_all               = {} -> null
      - vpc_id                 = "vpc-019aa49b4a7e284a0" -> null
    }

  # aws_subnet.desafio_devops_public_subnet will be destroyed
  - resource "aws_subnet" "desafio_devops_public_subnet" {
      - arn                                            = "arn:aws:ec2:us-east-2:851725465376:subnet/subnet-0552400a0fc6c7bbf" -> null
      - assign_ipv6_address_on_creation                = false -> null
      - availability_zone                              = "us-east-2b" -> null
      - availability_zone_id                           = "use2-az2" -> null
      - cidr_block                                     = "10.0.0.0/16" -> null
      - enable_dns64                                   = false -> null
      - enable_lni_at_device_index                     = 0 -> null
      - enable_resource_name_dns_a_record_on_launch    = false -> null
      - enable_resource_name_dns_aaaa_record_on_launch = false -> null
      - id                                             = "subnet-0552400a0fc6c7bbf" -> null
      - ipv6_native                                    = false -> null
      - map_customer_owned_ip_on_launch                = false -> null
      - map_public_ip_on_launch                        = true -> null
      - owner_id                                       = "851725465376" -> null
      - private_dns_hostname_type_on_launch            = "ip-name" -> null
      - tags                                           = {} -> null
      - tags_all                                       = {} -> null
      - vpc_id                                         = "vpc-019aa49b4a7e284a0" -> null
    }

  # aws_vpc.desafio_devops_vpc will be destroyed
  - resource "aws_vpc" "desafio_devops_vpc" {
      - arn                                  = "arn:aws:ec2:us-east-2:851725465376:vpc/vpc-019aa49b4a7e284a0" -> null
      - assign_generated_ipv6_cidr_block     = false -> null
      - cidr_block                           = "10.0.0.0/16" -> null
      - default_network_acl_id               = "acl-0667d4818530d42f4" -> null
      - default_route_table_id               = "rtb-0f159789e20be8129" -> null
      - default_security_group_id            = "sg-0a00388f6f3ec83bf" -> null
      - dhcp_options_id                      = "dopt-03bc4c4062226700d" -> null
      - enable_dns_hostnames                 = false -> null
      - enable_dns_support                   = true -> null
      - enable_network_address_usage_metrics = false -> null
      - id                                   = "vpc-019aa49b4a7e284a0" -> null
      - instance_tenancy                     = "default" -> null
      - ipv6_netmask_length                  = 0 -> null
      - main_route_table_id                  = "rtb-0f159789e20be8129" -> null
      - owner_id                             = "851725465376" -> null
      - tags                                 = {} -> null
      - tags_all                             = {} -> null
    }

Plan: 0 to add, 0 to change, 8 to destroy.

Changes to Outputs:
  - instance_id = "i-09702e15aedb96421" -> null
  - public_ip   = "18.117.96.107" -> null

Do you really want to destroy all resources?
  Terraform will destroy all your managed infrastructure, as shown above.
  There is no undo. Only 'yes' will be accepted to confirm.

  Enter a value: yes

aws_route_table_association.desafio_devops_route_table_association: Destroying... [id=rtbassoc-0744e75230e52372b]
aws_key_pair.devops_cha: Destroying... [id=desafio_devops_key_pair]
aws_instance.desafio_devops_ec2_instance: Destroying... [id=i-09702e15aedb96421]
aws_key_pair.devops_cha: Destruction complete after 2s
aws_route_table_association.desafio_devops_route_table_association: Destruction complete after 2s
aws_route_table.desafio_devops_route_table: Destroying... [id=rtb-02af8b09f1c92a7a3]
aws_route_table.desafio_devops_route_table: Destruction complete after 1s
aws_internet_gateway.desafio_devops_igw: Destroying... [id=igw-0789c6eb86438c218]
aws_instance.desafio_devops_ec2_instance: Still destroying... [id=i-09702e15aedb96421, 10s elapsed]
aws_internet_gateway.desafio_devops_igw: Still destroying... [id=igw-0789c6eb86438c218, 10s elapsed]
aws_instance.desafio_devops_ec2_instance: Still destroying... [id=i-09702e15aedb96421, 20s elapsed]
aws_internet_gateway.desafio_devops_igw: Still destroying... [id=igw-0789c6eb86438c218, 20s elapsed]
aws_instance.desafio_devops_ec2_instance: Still destroying... [id=i-09702e15aedb96421, 30s elapsed]
aws_internet_gateway.desafio_devops_igw: Still destroying... [id=igw-0789c6eb86438c218, 30s elapsed]
aws_instance.desafio_devops_ec2_instance: Still destroying... [id=i-09702e15aedb96421, 40s elapsed]
aws_internet_gateway.desafio_devops_igw: Still destroying... [id=igw-0789c6eb86438c218, 40s elapsed]
aws_instance.desafio_devops_ec2_instance: Destruction complete after 49s
aws_subnet.desafio_devops_public_subnet: Destroying... [id=subnet-0552400a0fc6c7bbf]
aws_security_group.desafio_devops_security_group: Destroying... [id=sg-0ce0ba32f7f4170fb]
aws_internet_gateway.desafio_devops_igw: Destruction complete after 48s
aws_subnet.desafio_devops_public_subnet: Destruction complete after 2s
aws_security_group.desafio_devops_security_group: Destruction complete after 2s
aws_vpc.desafio_devops_vpc: Destroying... [id=vpc-019aa49b4a7e284a0]
aws_vpc.desafio_devops_vpc: Destruction complete after 2s

Destroy complete! Resources: 8 destroyed.
```
