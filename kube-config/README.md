# Kubernetes Commands and Files

### This repository contains various commands to work with kubernetes

### Kube Config

- Check current context
```sh
 kubectl config view
```
- Set current context
```sh
  kubectl config --kubeconfig=config-demo use-context dev-frontend
```

- Add context details
```sh
kubectl config --kubeconfig=config-demo set-context dev-frontend --cluster=development --namespace=frontend --user=developer
kubectl config --kubeconfig=config-demo set-context dev-storage --cluster=development --namespace=storage --user=developer
kubectl config --kubeconfig=config-demo set-context exp-scratch --cluster=scratch --namespace=default --user=experimenter

```

- Specify kube config file
```sh
 kubectl config view --kubeconfig=<filename>
```



