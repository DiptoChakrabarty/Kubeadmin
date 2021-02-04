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

- History about the objects deployed
  helm history {DEPLOYEDCHART}


### Custom Charts

- Create a chart
  helm create ziggy

- Install a chart
  helm install ziggy-demo ./ziggy

- See template output after install
  helm get manifest ziggy

- Check output of template
  helm template {DIRECTORY}
  helm install --debug --dry-run dryrun ziggy/

- Change template value
  helm install --dry-run --debug --set name=zygote valuestest ziggy/


### Charts and Repository

- Package chart 
  helm package ziggy/

- Send chart to chartmuseum
  curl --data-binary "@ziggy-0.1.0.tgz" http://localhost:8085/api/charts

- Push using plugin
  helm push {DIRECTORY} {REPONAME}
  helm repo update
  helm search repo {REPONAME}

- Remove a repository
  helm repo remove {REPONAME}

- Check previous versions
  helm search repo -l {REPONAME}

- Install chart from repository
   helm install {INSTALLNAME} {REPOSITORYNAME}/{CHARTNAME}
  
- Upgrade using helm
  helm upgrade {INSTALLNAME} {REPOSITORYNAME}/{CHARTNAME}

- Rollback a install
  helm rollback (INSTALLNAME) {REVISION NO}



### Chartmuseum

- Set chartmuseum storage 
  chartmuseum --debug --port=8085 \
    --storage="local" \
    --storage-local-rootdir="./chartstorage"

- Add chartmuseum repo
  helm repo add mychartrepo http://localhost:8085

- Push using the push plugin
  helm push ziggy/ mychartrepo


