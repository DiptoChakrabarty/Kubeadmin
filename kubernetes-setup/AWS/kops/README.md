# Kops Cluster Setup

### These are the steps to setup kubernetes cluster in aws

- Launch Instance and install kops in it 

```sh
curl -Lo kops https://github.com/kubernetes/kops/releases/download/$(curl -s https://api.github.com/repos/kubernetes/kops/releases/latest | grep tag_name | cut -d '"' -f 4)/kops-darwin-amd64

chmod +x ./kops

sudo mv ./kops /usr/local/bin/
```

- Install kubectl in the instance

```sh
curl -Lo kubectl https://storage.googleapis.com/kubernetes-release/release/$(curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt)/bin/linux/amd64/kubectl

sudo chmod +x ./kubectl

sudo mv ./kubectl /usr/local/bin/kubectl
```

- Create group and add user with permissions
```sh
AmazonEC2FullAccess
AmazonRoute53FullAccess
AmazonS3FullAccess
IAMFullAccess
AmazonVPCFullAccess

In instance terminal

aws configure           
aws iam list-users      


export AWS_ACCESS_KEY_ID=$(aws configure get aws_access_key_id)
export AWS_SECRET_ACCESS_KEY=$(aws configure get aws_secret_access_key)

```

- Create S3 bucket and add env vars to instance
```sh

export NAME=kopsdemo.k8s.local
export KOPS_STATE_STORE=s3://kops-dipto

```

- Create cluster config files using kops 
```sh
kops create cluster --zones=ap-south-1a,ap-south-1b,ap-south-1c ${NAME} 

Generate public key for kops to use 

ssh-keygen -b 2048 -t rsa -f  ~/.ssh/id_rsa

Add public key to kops secret and cluster name

kops create secret --name ${NAME} sshpublickey admin -i ~/.ssh/id_rsa.pub


```

- Edit cluster configs
```sh
 * Edit main cluster configuration
  kops edit cluster ${NAME}

  * Edit types of instance used
    kops edit ig nodes --name ${NAME}

  * Get all nodes type
   kops get ig --name ${NAME}

  * Edit master node 
   kops edit ig {{ master name }}  --name ${NAME}

```

- Create the cluster 
```sh
    kops update cluster ${NAME} --yes
```

- Check cluster status
```sh
   kops export kubecfg --admin
   
   kops validate cluster 

   kubectl get nodes
```

- Delete cluster
```sh
  kops delete cluster --name ${NAME}  --yes
```

- Include Ingress
```sh
  kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/controller-v0.35.0/deploy/static/provider/aws/deploy.yaml
```





