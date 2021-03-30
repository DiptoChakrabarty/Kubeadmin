# KIND


### Installation
```sh
- curl -Lo ./kind https://kind.sigs.k8s.io/dl/v0.10.0/kind-linux-amd64

- chmod +x ./kind

- sudo mv ./kind /usr/local/bin

- kind version , kind help

```

### Getting started
```sh
-  Create a cluster with one master node only
   kind create cluster

- Get kubeconfig path
  kind get kubeconfig-path

- Get information about clusters
   kind get clusters
```

### Kind multiple worker nodes
```sh
- Create cluster from config file
  kind create cluster --name kindcluster --config kind-config.yaml

- Get nodes information
   kind get nodes 

- Create cluster with multiple master nodes which creates a  haproxyloadbalancer
kind create cluster --name kindcluster --config kind-multimaster.yaml

```