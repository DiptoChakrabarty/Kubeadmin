# ARGO CD

## Directory Structure
```sh
- install : installation of argocd in cluster taken from official argocd documentation
- config : custom resources to define in argocd
- yamls : resources we want argocd to deploy
```

## ARGOCD

```sh
- kubectl create namespace argocd

- kubectl apply -n argocd -f config/install.yaml 

- eval $(minikube docker-env) this step is only for minikube

- Create docker image

- Use config/project.yml to generate development project 

- Use config/app.yml to generate own application for a repository CD

- Resources should be deployed now
```

## ARGO EVENTS

```sh
- Install argo-events.yaml,event-bus.yaml from install directories

- Use config/event-source.yml to setup webhook eventsource

- Port Forward : kubectl -n argo-events port-forward  svc/webshook-eventsource-svc 8085:8085 &

- curl -X POST -H "Content-Type: application/json" -d '{"message": "simple webhook"}' http://localhost:8085/trigger
```






