# Kubernetes Commands and Files

### This repository contains various commands to work with kubernetes

### Pods

- Check number of deployments present in system

```sh
    kubectl get deployment
```
- Delete Pod

```sh
    kubectl delete deployment <deployment-name>
```
- Information about the pod
```sh
    kubectl describe deployments 
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


