# VPC Public Network Setup (Boto3)

Creates a basic public VPC network architecture in AWS using Python + boto3.

This project demonstrates programmatic infrastructure provisioning using the AWS SDK rather than infrastructure-as-code tools.

## What it creates

- **VPC**: `10.0.0.0/16`
- **Internet Gateway (IGW)** attached to the VPC
- **Public route table** with `0.0.0.0/0 -> IGW`
- **3 public subnets** across the first 3 available Availability Zones
- **Route table association** for each subnet
- **Consistent tagging** applied to all major resources

## Why this exists

Hands-on automation lab focused on AWS networking fundamentals and infrastructure scripting using boto3.

It reinforces:

- VPC architecture basics
- Public routing configuration
- Subnet segmentation
- Infrastructure automation patterns

## Prerequisites

- Python 3.10+ recommended
- boto3 installed
- AWS credentials configured via one of:
  - `aws configure`
  - Environment variables
  - IAM role (if running from AWS infrastructure)

### Minimum Required Permissions

- `ec2:CreateVpc`
- `ec2:CreateSubnet`
- `ec2:CreateInternetGateway`
- `ec2:AttachInternetGateway`
- `ec2:CreateRouteTable`
- `ec2:CreateRoute`
- `ec2:AssociateRouteTable`
- `ec2:CreateTags`
- `ec2:Describe*`

## How to run

From the `aws-python` repo root:

\`\`\`bash
cd 07_vpc
python3 vpc_public_network.py
\`\`\`