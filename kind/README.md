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