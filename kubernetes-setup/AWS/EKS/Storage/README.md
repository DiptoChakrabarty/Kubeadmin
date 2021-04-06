# Storage Methods

## EBS CSI DRIVERS

### Installation
```sh
- Create IAM policy with the following roles 
   {
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "ec2:AttachVolume",
        "ec2:CreateSnapshot",
        "ec2:CreateTags",
        "ec2:CreateVolume",
        "ec2:DeleteSnapshot",
        "ec2:DeleteTags",
        "ec2:DeleteVolume",
        "ec2:DescribeInstances",
        "ec2:DescribeSnapshots",
        "ec2:DescribeTags",
        "ec2:DescribeVolumes",
        "ec2:DetachVolume"
      ],
      "Resource": "*"
    }
  ]
}

- Generate IAM policy

```

```sh
- Attach IAM role to cluster
  
- Get worker nodes IAM Role ARN
 kubectl -n kube-system describe configmap aws-auth

- Attach policy created in previous step to IAM Role

- Deploy CSI Driver
  kubectl apply -k "github.com/kubernetes-sigs/aws-ebs-csi-driver/deploy/kubernetes/overlays/stable/?ref=master"
```


## RDS DATABASE 

### INITIAL SETUP

#### SECURITY GROUP
```sh
- There should be 2 VPCs present , one default and one of EKS

- Create security group for mysql in eks vpc

```

#### SUBNET GROUP
```sh
 - Provide RDS DB name and description

 - Select VPC as EKS provisoned one

 - Select Avalability zones

 - Select private subnets of EKS VPC for rds subnets and create

```

#### CREATE DATABASE
```sh

```