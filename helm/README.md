# Helm Commands 


- Update helm Version
  curl -L https://git.io/get_helm.sh | bash -s -- --version {VERSION}

- Add a repository to helm
  helm repo add stable https://charts.helm.sh/stable

- List the repository
  helm repo list 

- Search for a repository
  helm search repo stable/mysql

- Update a repository
  helm repo update
