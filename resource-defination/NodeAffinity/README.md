# Kubernetes Commands and Files

### This repository contains various commands to work with kubernetes

### NodeAffinity

- Types of NodeAffinity

```sh
    - requiredDuringSchedulingIgnoredDuringExecution

    - preferredDuringSchedulingIgnoredDuringExecution
```

- Label a node
```sh
  kubectl label node node01 <key>=<value>
```

- Check which pods are running on which nodes
```sh
    kubectl get pods -o wide
```

- Get node labels
```sh
 kubectl get nodes --show-labels
```