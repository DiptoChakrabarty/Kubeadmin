# Logging and Monitoring

- Install and configure helm
```sh
 * helm init

 * helm repo update
```

- Fix tiller account priviledges
```sh

kubectl create serviceaccount --namespace kube-system tiller

kubectl create clusterrolebinding tiller-cluster-rule --clusterrole=cluster-admin --serviceaccount=kube-system:tiller

kubectl patch deploy --namespace kube-system tiller-deploy -p '{"spec":{"template":{"spec":{"serviceAccount":"tiller"}}}}' 

```

- helm usage
```sh
 * helm install stable/mysql --name {{ NAME }} --set mysqlPassword=password

 * helm delete --purge {{ NAME }}

```

- Prometheus Operator
```sh
 * helm install --name monitoring --namespace monitoring stable/prometheus-operator

    Edit service monitoring-grafana  to LoadBalancer type
```