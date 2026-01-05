## Provision web app on AWS EC2 instance

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

### Run terraform commands to create the infra

```bash
terraform init
terraform fmt
terraform validate
terraform plan
terraform apply
```

### Clean up

```bash
terraform destory
```

### Run the following commands to create and/or delete bucket s3

```bash
python create_s3.py
```



```bash
python delete_s3.py
```

