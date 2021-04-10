# CERT MANAGER

This tells how to add ssl/tls support in your kubernetes cluster

## Minikube

```sh
- All the resources are present in yamls folder

- Add minikube ip in your /etc/hosts with host

```

## Self Signed Certificates

### Manual Provisioning 
```sh
- openssl req -x509 -newkey rsa:4096 -sha256 -nodes -keyout tls.key -out tls.crt -subj "/CN=example.com" -days 365

- Two files tls.crt and tls.key will be created

- Create secret of the tls keys 
  kubectl create secret tls example-com-tls --cert=tls.crt --key=tls.key

- Add secret in ingress 

```

### Automatic Provisioning using cert manager
```sh
- kubectl create namespace cert-manager
- helm repo add jetstack https://charts.jetstack.io
- helm repo update
- helm install \
  cert-manager jetstack/cert-manager \
  --namespace cert-manager \
  --create-namespace \
  --version v1.3.0 \
   --set installCRDs=true

- openssl genrsa -out ca.key 2048
- openssl req -x509 -new -nodes -key ca.key -sha256 -subj "/CN=sampleissuer.local" -days 1024 -out ca.crt -extensions v3_ca
- kubectl create secret tls ca-key-pair --key=ca.key --cert=ca.crt

- Create Issuer using issuer.yaml in crds which will create a certificate issuer referencing the above created secret
- Create certificate using certyaml in crds which will create secret needed by ingress
```
