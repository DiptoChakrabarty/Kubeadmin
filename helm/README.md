# Helm Commands 



### Basic Commands

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

- Install a repository
  helm install stable/mysql --generate-name
  helm install myairflow stable/airflow

- Uninstall a repository
  helm uninstall myairflow


### Custom Charts

- Create a chart
  helm create ziggy

- Install a chart
  helm install ziggy-demo ./ziggy

