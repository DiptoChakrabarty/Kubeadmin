# Kubernetes Commands and Files

### This repository contains various commands to work with kubernetes


- kubectl exec -it ubuntu-sleeper  /bin/bash


apiVersion: v1
kind: Pod
metadata:
  name: hello-world
spec:  # specification of the pod’s contents
  restartPolicy: Never
  containers:
  - name: hello
    image: "ubuntu:14.04"
    env:
    - name: MESSAGE
      value: "hello world"
    command: ["/bin/sh","-c"]
    args: ["/bin/echo \"${MESSAGE}\""]
    
    
command: ["/bin/sh","-c"]
args: ["command one; command two && command three"]

