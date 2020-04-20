# Kubernetes Commands and Files

### This repository contains various commands to work with kubernetes

### Taints and Tolerations

- Taint Effects

```sh
    1) NoSchedule : Pod not scheduled on nodes
    2) PreferNoSchedule : try to avoid placing pods
    3) NoExecute : new pods not scheduled and existing pods evicted if do not tolerate taint
```
 - Taint Nodes

 ```sh
    kubectl taint nodes <node name>  key=value: taint-effect
```

- Check Taint on master node

```sh
    kubectl describe node kubemaster | grep Taint
```

- Get taints in all nodes

```sh
    kubectl get nodes -o json | jq '.items[].spec.taints'

    kubectl describe nodes node1
```

- Remove taint from master node

```sh
    kubectl taint nodes master node-role.kubernetes.io/master : NoSchedule
```

