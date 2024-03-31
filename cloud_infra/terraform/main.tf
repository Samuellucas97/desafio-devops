terraform {
    required_providers {
      aws = {
        source = "hashicorp/aws"
        version = "~> 5.0"
      }
    }
    backend "s3" {
      bucket = "desafiodevopsterraforms3backendbucket"
      key = "terraform.tfstate"
      dynamodb_table = "desafio-devops-terraform-lock"
    }

    required_version = ">= 1.7.5"
}

provider "aws" {
    region = "${var.region}"
}

resource "aws_key_pair" "devops_cha" {
  key_name = "${var.key_pair_name}"
  public_key = file("~/.ssh/id_rsa.pub")
}

resource "aws_vpc" "desafio_devops_vpc" {
  cidr_block =  "${var.vpc_cidr}"
}

resource "aws_subnet" "desafio_devops_public_subnet" {
    vpc_id = aws_vpc.desafio_devops_vpc.id
    cidr_block = "${var.vpc_cidr}"
    map_public_ip_on_launch = true
}

resource "aws_internet_gateway" "desafio_devops_igw" {
    vpc_id = aws_vpc.desafio_devops_vpc.id
}

resource "aws_route_table" "desafio_devops_route_table" {
    vpc_id = aws_vpc.desafio_devops_vpc.id

    route {
        cidr_block = "${var.route_table_cidr}"
        gateway_id = aws_internet_gateway.desafio_devops_igw.id
    }
}

resource "aws_route_table_association" "desafio_devops_route_table_association" {
    subnet_id = aws_subnet.desafio_devops_public_subnet.id
    route_table_id = aws_route_table.desafio_devops_route_table.id
}

resource "aws_security_group" "desafio_devops_security_group" {
    name = "${var.security_group_name}"
    description = "Allow SSH and HTTP requests - inboud traffic"
    vpc_id = aws_vpc.desafio_devops_vpc.id

    ingress {
        from_port = 22
        to_port = 22
        protocol = "tcp"
        cidr_blocks = ["0.0.0.0/0"]
    }

    ingress {
        from_port = 80
        to_port = 80
        protocol = "tcp"
        cidr_blocks = ["0.0.0.0/0"]
    }

    egress {
        from_port = 0
        to_port = 0
        protocol = "-1"
        cidr_blocks = ["0.0.0.0/0"]
    }
}

resource "aws_instance" "desafio_devops_ec2_instance" {
    ami = "${var.ami_id}"
    instance_type = "${var.instance_type}"
    
    subnet_id = aws_subnet.desafio_devops_public_subnet.id
    vpc_security_group_ids = [ aws_security_group.desafio_devops_security_group.id ]
    key_name = "${var.key_pair_name}"

    tags = {
        Name = "DesafioDevOpsEC2Instance"
    }
}


