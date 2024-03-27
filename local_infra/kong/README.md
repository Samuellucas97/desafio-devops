# Kong API Gateway

Este diretório contain informações relacionadas ao Kong API Gateway.

## Como instalar?

```bash
$ microk8s helm repo add kong https://charts.konghq.com
$ microk8s helm repo update
$ microk8s helm install kong kong/kong --create-namespace kong-api-gateway -f values.yaml
$ microk8s kubectl port-forward svc/kong-proxy 8001:8001 -n default
```

## Como configurar?


