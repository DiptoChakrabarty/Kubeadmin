# Kubernetes Commands and Files

### This repository contains various commands to work with kubernetes

### Labels and Services

- Get labels of Pods

```sh
    kubectl get pods --show-labels
```
- Label a  Pod

```sh
    kubectl run --generator= run-pod/v1  redis-pod --image=redis:alpine  -l tier=db
```
- Get pods with env=dev

```sh
    kubectl get pods --selector env=dev
```

- Get pods with label bu

```sh
    kubectl get pods -l bu
```

- Get everything in env pod

```sh
    kubectl get all --selector env=pod
```