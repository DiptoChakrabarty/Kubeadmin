## INSTALLATION
- kubectl create ns flux
- export GHUSER="DiptoChakrabarty"
- fluxctl install \
    --git-user=${GHUSER} \
    --git-email=${GHUSER}@users.noreply.github.com \
    --git-url=git@github.com:${GHUSER}/Kubeadmin \
    --git-path=flux/yamls/* \
    --git-branch=master \
    --namespace=flux | kubectl apply -f -