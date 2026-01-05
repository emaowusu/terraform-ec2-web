resource "aws_instance" "web" {
  ami                    = var.amiID
  instance_type          = var.instance_type
  key_name               = "web-key"
  vpc_security_group_ids = [aws_security_group.web-sg.id]
  availability_zone      = var.zone

  tags = {
    Name = "web-server"
  }

  provisioner "file" {
    source      = "web.sh"
    destination = "/tmp/web.sh"
  }

  connection {
    type        = "ssh"
    user        = var.webuser
    private_key = file("webKey")
    host        = self.public_ip
  }

  provisioner "remote-exec" {

    inline = [
      "chmod +x /tmp/web.sh",
      "sudo /tmp/web.sh"
    ]
  }

  provisioner "local-exec" {
    command = "echo ${self.private_ip} >> private_ips.txt"
  }

}

resource "aws_ec2_instance_state" "web-state" {
  instance_id = aws_instance.web.id
  state       = "running"
}

