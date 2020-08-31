# Kubernetes Commands and Files

### This repository contains various commands to work with kubernetes

### Ingress


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
