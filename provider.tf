provider "aws" {
    region = "us-east-1"
}

# S3 bucket for Terraform state
resource "aws_s3_bucket" "terraform_state" {
    bucket = "pipeline-101-tf-state"
    acl    = "private"

    versioning {
        enabled = true
    }

    server_side_encryption_configuration {
        rule {
            apply_server_side_encryption_by_default {
                sse_algorithm = "AES256"
            }
        }
    }

    lifecycle {
        prevent_destroy = true
    }

    tags = {
        Name = "terraform-state-bucket"
    }
}

# DynamoDB table for Terraform state locking
resource "aws_dynamodb_table" "terraform_locks" {
    name         = "terraform-locks"
    billing_mode = "PAY_PER_REQUEST"
    hash_key     = "LockID"

    attribute {
        name = "LockID"
        type = "S"
    }

    tags = {
        Name = "terraform-locks"
    }
}

# Terraform backend configuration
terraform {
    backend "s3" {
        bucket         = "pipeline-101-tf-state"  # Matches the S3 bucket created above
        key            = "terraform.tfstate"
        region         = "us-east-1"
        dynamodb_table = "terraform-locks"
        encrypt        = true
    }
}
