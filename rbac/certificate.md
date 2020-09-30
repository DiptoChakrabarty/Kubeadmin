# Commands to generate a X.509 Certificate for cluster users


## Generate Certificate

```sh

- openssl genrsa -out developer.key 2048  # create pvt key for user

- openssl req -new -key developer.key -out req.csr -subj "/CN=developer/O=developer"

- get kubernetes pvt key and certificate

- openssl x509 -req -in req.csr -CA kube.crt -CAkey kube.key  -CAcreateserial -out developer.crt -days 365


```

## Add cluster context 
```sh
- kubectl config set-cluster {{ cluster name }} --server= {{ loadbalancer/master url }}

-  kubectl config set-context mycontext --user developer --cluster {{ cluster name }} 

- kubectl config use-context mycontext

- kubectl config set-credentials developer --client-certificate= {{ users certificate}} --client-key= {{ users key }} 

- kubectl config set-cluster kopsdemo.k8s.local --certificate-authority= {{kubernetes certificate  }}

```

## Add tls certificates
```sh
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