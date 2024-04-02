# Kong API Gateway

Este diretório contém informações relacionadas ao Kong API Gateway.

## Como instalar?

```bash
$ microk8s enable dns storage rbac metallb
$ microk8s.kubectl apply -f https://github.com/kubernetes-sigs/gateway-api/releases/download/v1.0.0/standard-install.yaml
$ microk8s.kubectl apply -f /home/vagrant/kong/gateway-api-crd.yaml
$ helm repo add kong https://charts.konghq.com
$ helm repo update
$ helm install kong kong/ingress -n kong --create-namespace 
$ export PROXY_IP=$(microk8s.kubectl get svc --namespace kong kong-gateway-proxy -o jsonpath='{.status.loadBalancer.ingress[0].ip}')
$ echo $PROXY_IP
$ curl -i $PROXY_IP
HTTP/1.1 404 Not Found
Content-Type: application/json; charset=utf-8
Connection: keep-alive
Content-Length: 48
X-Kong-Response-Latency: 0
Server: kong/3.0.0

{"message":"no Route matched with those values"}
```

## Como configurar?

Execute o seguinte comando para descobrir as portas dos serviços relacionados:

```bash
$ microk8s.kubectl get service -n kong-api-gateway 
NAME                           TYPE           CLUSTER-IP       EXTERNAL-IP   PORT(S)                         AGE
kong-kong-validation-webhook   ClusterIP      10.152.183.159   <none>        443/TCP                         6h39m
kong-kong-manager              NodePort       10.152.183.94    <none>        8002:31553/TCP,8445:31273/TCP   6h39m
kong-kong-proxy                LoadBalancer   10.152.183.235   192.168.56.13     80:32435/TCP,443:32380/TCP      6h39m
```

Abra o navegador e acesse o serviço `kong-kong-manager` via [http://192.168.56.10:31553](http://192.168.56.10:31553/), onde `192.168.56.10` é o IP setado no VagrantFile.
