# CERT MAANAGER

This tells how to add ssl/tls support in your kubernetes cluster

## Minikube

```sh
- All the resources are present in yamls folder

- Add minikube ip in your /etc/hosts with host

```

## Self Signed Certificates
```sh
- openssl req -x509 -newkey rsa:4096 -sha256 -nodes -keyout tls.key -out tls.crt -subj "/CN=example.com" -days 365

- Two files tls.crt and tls.key will be created

- Create secret of the tls keys 
  kubectl create secret tls example-com-tls --cert=tls.crt --key=tls.key

- Add secret in ingress 

```
