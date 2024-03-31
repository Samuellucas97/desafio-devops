output "instance_id" {
  value = aws_instance.desafio_devops_ec2_instance.id
  description = "The ID of the EC2 instance"
}

output "public_ip" {
  value = aws_instance.desafio_devops_ec2_instance.public_ip
  description = "The PUBLIC IP of the EC2 instance"
}