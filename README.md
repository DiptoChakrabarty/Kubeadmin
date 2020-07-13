# Kubernetes Commands and Files

<img src="images/kube.png">




## This repository contains the most useful commands to work with kubernetes


* [Official Docs](https://kubernetes.io/docs/home/)
* [Tutorials](https://kubernetes.io/docs/tutorials/)
* Videos 
   - [Kubernetes in 5 Minutes](https://www.youtube.com/watch?v=PH-2FfFD2PU)
   - [Kubernetes for beginners](https://www.youtube.com/watch?v=l_lWfipUimk&list=PLhW3qG5bs-L8EU_Oocu6RkNPpYpaamtXX)
   - [Kubernetes made Easy](https://www.youtube.com/watch?v=jgmdY73RF6w&list=PLMPZQTftRCS8Pp4wiiUruly5ODScvAwcQ)


ETCDCTL_API=3 etcdctl --endpoints=https://127.0.0.1:2379 --cacert=/etc/kubernetes/pki/etcd/ca.crt --cert=/etc/kubernetes/pki/etcd/server.crt --key=/etc/ku
bernetes/pki/etcd/server.key snapshot save  /tmp/snapshot-pre-boot.db


ETCDCTL_API=3 etcdctl --endpoints=https://[127.0.0.1]:2379 --cacert=/etc/kubernetes/pki/etcd/ca.crt \
     --name=master \
     --cert=/etc/kubernetes/pki/etcd/server.crt --key=/etc/kubernetes/pki/etcd/server.key \
     --data-dir /var/lib/etcd-from-backup \
     --initial-cluster=master=https://127.0.0.1:2380 \
     --initial-cluster-token etcd-cluster-1 \
     --initial-advertise-peer-urls=https://127.0.0.1:2380 \
     snapshot restore /tmp/snapshot-pre-boot.db



