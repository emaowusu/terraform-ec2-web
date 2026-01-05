output "instance-public-ip" {
  description = "EC2 public ip"
  value       = aws_instance.web.public_ip
}
