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
- Scale a deployment
```sh
    kubectl scale deployments/<deployment-name>  --replicas=4
```
- Information about deployment
```sh
    kubectl describe deployments/<name>
```
- Update a deployment image
```sh
    kubectl set image deployments/<deployment-name>   <deployment-name>=<new image name>
```


