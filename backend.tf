terraform {
  backend "s3" {
    bucket = "terra-backend235"
    key = "terraform/backend"
    region = "us-east-1"
  }
}
