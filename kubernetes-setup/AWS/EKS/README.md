# EKS

## Installation

- Install following clis
    * awscli
    * kubectl 
    * ekscli

## COMMANDS

### CREATE CLUSTER
-  Create cluster with no worker nodes
 ```sh
    eksctl create cluster --name={CLUSTER NAME} \
                        --region=ap-south-1 \
                        --zones=ap-south-1a,ap-south-1b \
                        --without-nodegroup 
```

- check current context 
 ```sh
    kubectl config view | grep current 
```

- Get clusters
 ```sh
    eksctl get clusters
```

### Create IAM Policy And Ec2 Node Key Pair
 ```sh
- eksctl utils associate-iam-oidc-provider \
    --region ap-south-1 \
    --cluster {CLUSTER NAME}
    --approve
```

### Node groupds
- Create Node Group with autoscaling alb ingress and dns access
 ```sh
eksctl create nodegroup --cluster={CLUSTER NAME} --region=ap-south-1 --name={CLUSTER NODEGROUP NAME} --node-type=t2.medium --nodes=2 --nodes-min=2 --nodes-max=5  --node-volume-size=10 --ssh-access --ssh-public-key=eks --managed --asg-access --external-dns-access --full-ecr-access --appmesh-access --alb-ingress-access 
```

- Get nodes
 ```sh
  kubectl get nodes
  kubectl get nodes -o wide
```

- Get nodegroup of cluster
 ```sh
  eksctl get nodegroup --cluster=ekscluster
```

### Delete Cluster
 - eksctl delete cluster {CLUSTER NAME}

 - eksctl delete nodegroup --cluster={CLUSTER NAME} --name={NODE GROUP NAME}