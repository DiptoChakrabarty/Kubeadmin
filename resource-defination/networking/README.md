# Kubernetes Commands and Files

### This repository contains various commands to work with kubernetes

### NetWorking

- Determine Ip Address
```sh
    ifconfig

    ip addr
```

- Find mac address of another node in network
```sh
    arp node
```

- No of Requests in a port
```sh

    netstat -tnlp | grep < port > | wc -l

```

- Network plugin for kubernetes and directory
```sh
    ps -aux | grep kubernetes

    /etc/cni/net.d
```

- Check gateway and destination
```sh
    route -n
```