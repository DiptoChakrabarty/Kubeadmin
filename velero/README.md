# Velero BackUps

### Configure Storage

```sh

- Download minio docker image for storage
  sudo docker pull minio/minio

- Start container 
  sudo docker run --name minio -p 9000:9000 -v data:/data minio/minio server /data

- Get Access and Secret Key
  sudo docker exec -it minio cat /data/.minio.sys/config/config.json | egrep "(access|secret)_key"

```

### Setup Velero

```sh

- Install Velero and create credentials file with minio access and secret keys

- velero install --provider aws --plugins velero/velero-plugin-for-aws:v1.0.0 --bucket velerodemo --secret-file ./minio.keys --backup-location-config region=minio,s3ForcePathStyle=true,s3Url=http://192.168.0.104:9000

- Check backup location 
  veleor backup-location get

- Check backups 
  veleor backup get

```


### BackUp Resources

```sh
- BackUp Entire Cluster
   velero backup create clusterbackup

- BackUp Single NameSpace
  velero backup create argonsbackup --include-namespaces argo

- Restor from backup 
  velero restore create argonsrestore --from-backup argonsbackup

- Check restores
  velero restore  get

- Create schedules
 velero schedule create argonschedule --schedule="@every 1m" --include-namespace argo
```


### UnInstall Velero

```sh
 - kubectl delete namespace/velero clusterrolebinding/velero
 - kubectl delete crds -l component=velero
```

