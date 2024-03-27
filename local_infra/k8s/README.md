# Arquivos Kubernetes

Este diretórios contém o arquivo Kubernetes relacionado a configuração da aplicação Flas 

## Como instalar dentro de um cluster Kubernetes?

Execute os seguintes comandos:

```bash
$ kubectl create namespace app
$ kubectl apply -f /home/vagrant/k8s/flask-app-k8s.yaml --namespace app
$ kubectl wait --for=condition=available deployment/flask-app-deployment --namespace app
$ kubectl wait --for=condition=Ready pod -l app=flask-app -n app
$ kubectl get service --namespace app
$ kubectl get deployment --namespace app
```

Para testar, execute:

```bash
$ export NODE_PORT="$(kubectl get services/flask-app-service --namespace app -o go-template='{{(index .spec.ports 0).nodePort}}')"
$ echo "NODE_PORT=${NODE_PORT}"
$ curl -sv localhost:${NODE_PORT}/api/comment/list/1
```
