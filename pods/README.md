# Kubernetes Commands and Files

### This repository contains various commands to work with kubernetes

### Pods

- Check number of pods present in system

```sh
    kubectl get pods
```
- Delete Pod

```sh
    kubectl delete pod <pod-name>
```
- Information about the pod
```sh
    kubectl describe pods 
```
- No of containers in pod
```sh
    kubectl get pods -o json "{.spec.containers[*].name}
```

