# Commands to generate a X.509 Certificate for cluster users


## Kops

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


## MiniKube

## Generate Certificates

```sh

- Create a certificate and key pair for user pinku

- openssl genrsa -out pinku.key 2048  (private key)

- openssl req -new -key pinku.key -out pinku.csr -subj "/CN=pinku/O=argo" (certificate signing request)

- Sign pinkus certificatew with the cluster crt and key which is in /etc/kubernetes/pki or .minikube folder

- openssl x509 -req -in pinku.csr -CA ${HOME}/.minikube/ca.crt -CAkey ${HOME}/.minikube/ca.key -CAcreateserial -out pinku.crt -days 45  

- If Pinku creates own certificate
    - kubectl --kubeconfig {kubeconfig filename} config set-cluster {cluster name} --server {server url} --certificate-authority=${HOME}/.minikube/ca.crt (create kubeconfig)

    kubectl --kubeconfig pinku.kubeconfig config set-cluster minikube --server https://192.168.99.100:8443 --certificate-authority=${HOME}/.minikube/ca.crt

    - kubectl --kubeconfig {kubeconfig filename} config set-credentials {username } --client-certificate {user crt} --client-key {user key}
    
    kubectl --kubeconfig pinku.kubeconfig config set-credentials pinku --client-certificate pinku.crt --client-key pinku.key   (attach user)

    - kubectl --kubeconfig {kubeconfig filename}  config set-context {context name} --cluster  {cluster name} --namespace {namespace} --user {username}
    
      kubectl --kubeconfig pinku.kubeconfig  config set-context pinku-kube --cluster  minikube --namespace argo --user pinku  (attach context and namespace)

```
