terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.16"
    }
  }

  required_version = ">= 1.2.0"
}

provider "aws" {
  region = "us-east-1"
}

resource "aws_ec2_host" "mac_dedicated_host" {
  availability_zone = "us-east-1a" 
  instance_type     = "mac1.metal"
  auto_placement    = "on"

  tags = {
    Name = "Mac-Dedicated-Host"
  }
}

resource "aws_instance" "sonoma_victim" {
  ami           = "ami-031ef535c8ee703b6"
  instance_type = "mac1.metal"
  host_id       = aws_ec2_host.mac_dedicated_host.id
  key_name      = "your-key-pair-name"

  tags = {
    Name = "Victim-Sonoma"
  }
}

resource "aws_instance" "kali_attacker" {
  ami           = "ami-061b17d332829ab1c"
  instance_type = "t2.micro"
  key_name      = "your-key-pair-name"

  tags = {
    Name = "Attacker-KaliLinux"
  }
}