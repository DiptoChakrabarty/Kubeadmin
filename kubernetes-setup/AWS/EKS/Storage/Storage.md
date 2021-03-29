## EBS CSI DRIVER

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