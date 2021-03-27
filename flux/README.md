## INSTALLATION
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

- $env:FLUX_FORWARD_NAMESPACE = "flux"

## UNINSTALL
fluxctl install \
    --git-user=${GHUSER} \
    --git-email=${GHUSER}@users.noreply.github.com \
    --git-url=git@github.com:${GHUSER}/Kubeadmin \
    --git-path=flux/kustomize/ \
    --git-branch=master \
    --namespace=flux | kubectl delete -f -

## AUTHETICATION 

- In github Settings->deploy key

- get key using fluxctl identity --k8s-fwd-ns flux

- give write access


## GIT SOURCE
- Download using curl -s https://toolkit.fluxcd.io/install.sh | sudo bash

- Install toolkit using flux install --namespace=flux
flux create source git gitinfo \
    --url=https://github.com/DiptoChakrabarty/Kubeadmin \
    --branch=master --namespace=flux
