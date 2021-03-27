# EKS

## Installation

- Install following clis
    * awscli
    * kubectl 
    * ekscli

## COMMANDS

### CREATE CLUSTER
-  Create cluster with no worker nodes
    eksctl create cluster --name=ekscluster \
                        --region=ap-south-1 \
                        --zones=ap-south-1a,ap-south-1b \
                        --without-nodegroup 

- check current context 
    kubectl config view | grep current 

- Get clusters
    eksctl get clusters

### Create IAM Policy And Ec2 Node Key Pair
- eksctl utils associate-iam-oidc-provider \
    --region ap-south-1 \
    --cluster ekscluster
    --approve

### Node groupds
- Create Node Group with autoscaling alb ingress and dns access

eksctl create nodegroup --cluster=ekscluster --region=ap-south-1 --name=ekscluster-nodes --node-type=t2.medium --nodes=2 --nodes-min=2 --nodes-max=5  --node-volume-size=10 --ssh-access --ssh-public-key=eks --managed --asg-access --external-dns-access --full-ecr-access --appmesh-access --alb-ingress-access 

- Get nodes
  kubectl get nodes
  kubectl get nodes -o wide

- Get nodegroup of cluster
  eksctl get nodegroup --cluster=ekscluster