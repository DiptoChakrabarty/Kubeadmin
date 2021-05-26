# Kubernetes Commands and Files

### This repository contains various commands to work with kubernetes

### Ingress

- [RBAC AND DEPLOY](https://raw.githubusercontent.com/kubernetes/ingress-nginx/nginx-0.27.0/deploy/static/mandatory.yaml)
- [SERVICE](https://raw.githubusercontent.com/kubernetes/ingress-nginx/nginx-0.27.0/deploy/static/provider/cloud-generic.yaml)


## Add tls certificates
```sh
   Use the file nginx-ingress-tls.yml for this example

 - Create self signed certificates and key
 openssl req -x509 -newkey rsa:4096 -sha256 -nodes  -keyout tls.key -out tls.crt -subj "/CN=nginx-ingress.com" -days 365
    x509: type of certificate
    newkey: specifies requirement of newkey
    rsa:4096: algorithm used and key length
    nodes: No DES
    CN: Common Name

 - Create secret to hold the tls certificate and key
   kubectl create secret tls nginx-ingress-tls --cert=tls.crt --key=tls.key

```

## Automatic provisoning of certificates
```sh

  Add cert manager helm repo 
   - helm init 

  - helm repo add jetstack https://charts.jetstack.io
 
  - helm repo update
  
  - helm install \
  --name cert-manager \
  --namespace cert-manager \
  --version v0.16.1 \
  --set installCRDs=true \
  jetstack/cert-manager  

```
- Create Certificates

```sh
 - openssl genrsa -out ca.key 2048

 - openssl req -x509 -new -nodes -key ca.key -sha256 -subj "/CN=nginx-ingress.com" -days 1024 -out ca.crt -extensions v3_ca  -config openssl-ca.cnf
```
