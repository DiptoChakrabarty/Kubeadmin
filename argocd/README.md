# ARGO CD

## ARGOCD
- kubectl create namespace argocd

- kubectl apply -n argocd -f config/install.yaml 

- eval $(minikube docker-env)

- Create docker image

- Use config/app.yml to generate own application for a repository CD

## ARGO EVENTS
- Install argo-events.yaml,event-bus.yaml from install directories

- Use config/event-source.yml to setup webhook eventsource

- Port Forward : kubectl -n argo-events port-forward  svc/webshook-eventsource-svc 8085:8085 &

- curl -X POST -H "Content-Type: application/json" -d '{"message": "simple webhook"}' http://localhost:8085/trigger
