resource "aws_key_pair" "web-key" {
  key_name   = "web-key"
  public_key = "your_public_ssh_key_here"
}