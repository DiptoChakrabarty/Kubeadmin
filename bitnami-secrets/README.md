### INSTALLATION

1) Install kubeseal cli
- wget https://github.com/bitnami-labs/sealed-secrets/releases/download/v0.15.0/kubeseal-linux-amd64 -O kubeseal

- sudo install -m 755 kubeseal /usr/local/bin/kubeseal

- Install controller from controller.yaml [Taken from](https://github.com/bitnami-labs/sealed-secrets/releases/download/v0.15.0/controller.yaml)