# Kubernetes Commands and Files

### This repository contains various commands to work with kubernetes

### Deployments

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
- Rollout status
```sh
    kubectl rollout status deployments/<deployment-name>   
```
- Rollback deployment
```sh
    kubectl rollout undo deployment/<deployment-name>
```
- Edit Deployment
```sh
    kubectl edit deployment.v1.apps/nginx-deployment
```
- Run deployment with replicas
```sh
    kubectl run <pod-name> --image=<image name> --replicas=<no of replicas>
```



