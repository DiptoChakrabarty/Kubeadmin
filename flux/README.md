## Setup 
```sh
    * Installation 
    - kubectl create ns flux

    - export GHUSER="DiptoChakrabarty"

    - fluxctl install \
        --git-user=${GHUSER} \
        --git-email=${GHUSER}@users.noreply.github.com \
        --git-url=git@github.com:${GHUSER}/Kubeadmin \
        --git-path=flux/kustomize/ \
        --git-branch=master \
        --namespace=flux | kubectl apply -f -

    - kubectl -n flux rollout status deployment/flux


* UnInstall 
    - fluxctl install \
        --git-user=${GHUSER} \
        --git-email=${GHUSER}@users.noreply.github.com \
        --git-url=git@github.com:${GHUSER}/Kubeadmin \
        --git-path=flux/kustomize/ \
        --git-branch=master \
        --namespace=flux | kubectl delete -f -
```
## AUTHETICATION 
```sh
- In github Settings->deploy key

- get key using fluxctl identity --k8s-fwd-ns flux

- give write access
```

## Flux and Kustomize
```sh
 - Download toolkit cli : curl -s https://toolkit.fluxcd.io/install.sh | sudo bash 

 - Install in flux namespace : flux install --namespace=flux

 - all files are present in kustomize-controller folder

 - apply gitinfo.yml to specify git repo and kustomize.yml to specify which gitrepo to reference and other details

 - ensure kustomization.yaml file is present in your working repo which kustomize will build

```

