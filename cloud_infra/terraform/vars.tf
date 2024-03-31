variable "region" {
    default = "us-east-2"
    type = string
}

variable "vpc_cidr" {
    default = "10.0.0.0/16"
    description = "CIDR for the VPC (2**16 = 65536 ips)"
 }


variable "subnet_cidr" {
    default = "10.0.0.0/24"
    description = "CIDR fo the Subnet (2**8 = 256 ips)"
}

variable "route_table_cidr" {
    default = "0.0.0.0/0"
    description = "Mapping request to the this"
}

variable "security_group_name" {
    default = "desafio_devops_security_group"
    description = "Name of my security group"
}

variable "ami_id" {
    default = "ami-0b4750268a88e78e0"
    description = "Ubuntu Server 20.04 LTS (HVM), SSD Volume Type"
}

variable "instance_type" {
    default = "t2.micro"
    description = "EC2 instance type"
}

variable "key_pair_name" {
    default = "desafio_devops_key_pair"
    description = "Public SSH to be put inside EC2"
}
