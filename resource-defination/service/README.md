# Kubernetes Commands and Files

### This repository contains various commands to work with kubernetes

### Services

- Types of Services

```sh
 1) NodePort : makes internal port accessible
 2) ClusterIp : creates virtual ip inside cluster
 3) LoadBalancer: provides loadbalancer to app
 ```
 
 - Port Forward
 ```sh
 kubectl port-forward svc/nginx-demo 8000:80
 ```

