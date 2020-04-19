# Kubernetes Commands and Files

### This repository contains various commands to work with kubernetes

### Deployments

- Find all pods of all namespaces

```sh
    kubectl get pods --all-namespace
```

- Access pod of another namespace
```sh
    db-service.dev.svc.cluster.local

   - We are trying to access db-service pod of namespace dev from namespace default 
   - cluster local is domain name of cluster
   - svc is subdomain name
```


