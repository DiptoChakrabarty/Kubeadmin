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

    kubectl get pods -o wide
```
- No of containers in pod
```sh
    kubectl get pods -o json "{.spec.containers[*].name}
```
- Launch Pods imperative commands
```sh
    kubectl run --generator=run-pod/v1 redis-pod --image=redis:alpine
```
- Get pods of all namespace
```sh
    kubectl get pods --namespace=<namespace name>
```
- Label pods
```sh
    kubectl run --generator=run-pod/v1 redis-pod --image=redis:alpine  -l tier=db
```

- Edit pods

```sh
    kubectl edit pod <pod name>
```

