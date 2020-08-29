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
