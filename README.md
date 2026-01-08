## Provision web app on AWS EC2 instance

### Project Overview

This project demonstrates how to provision a web application on an AWS EC2 instance using Terraform. The web application will be a simple HTML, CSS and JavaScript page served by an Apache2 web server. Additionally, the project includes Python scripts to create and delete an S3 bucket.

### Prerequisite

- AWS free tier Account

### Must have the following install and configured on your machine

- aws cli
- Python
- boto3
  
### Create the following on your local machine

- Create IAM User and assign access and secret access key to it.
- Create ssh keys in your project directory

 ```bash
 ssh-keygen
 ```

- Copy the content of ssh key with `.pub` file extension to the `keypair.tf` file
- Add your laptop ipv4 public to security group SSH rule like this your_public_ip/32.
- **You can find your laptop/PC public ipv4 by visiting [Whatismyipaddress](https://whatismyipaddress.com/) site**.


### Run terraform commands to create the infra

```bash
terraform init
terraform fmt
terraform validate
terraform plan
terraform apply
```

### Create s3 bucket for backend 

- First create `backend.tf` after `terraform apply` is successful and add the lines of code below **NB:** *This is for collaboration purpose*

```bash
terraform {
  backend "s3" {
    bucket = "terra-backend235"
    key = "terraform/backend"
    region = "us-east-1"
  }
}
```

```bash
python create_s3.py
```

### Clean up

```bash
terraform destory
```

### Command to delete the s3 bucket

```bash
python delete_s3.py
```
