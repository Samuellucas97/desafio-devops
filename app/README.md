# API de Comentários

Trata-se de uma aplicação Flask - API REST.  Através dela os internautas enviam comentários em texto de uma máteria e acompanham o que outras pessoas estão falando sobre o assunto em destaque. O funcionamento básico da API consiste em uma rota para inserção dos comentários e uma rota para listagem.

É utilizado o Poetry para gerenciamento de ambiente virtual (virtualenv) e gerenciamento de pacotes. A lista de pacotes está disponível em `pyproject`. Caso deseje adicionar um novo pacotes execute `poetry add <nome do pacote>`.

## Requisitos

- Docker (_versão 25.0.4_)
- GNU Make (_versão 4.3_) - Opcional!

## Como executa a aplicação?

### Execução via Docker

Para criação da imagem Docker e instanciação de seu respectivo container, execute o comando abaixo:

```bash
$ make

******************** KILLING CONTAINER **********************************
docker rm -f flask_app
Error response from daemon: No such container: flask_app

docker ps
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES


******************** REMOVING DOCKER IMAGE **********************************
docker image rm -f app:1.0
Untagged: app:1.0
Deleted: sha256:b9b683671dda7241f6de452dc526653cdfae0d4c1d1cdc58afea0d32443b6146

docker image ls
REPOSITORY   TAG       IMAGE ID   CREATED   SIZE


******************** BUILDING & TAGGING DOCKER IMAGE **********************************
docker build -t app:1.0 .
[+] Building 1.3s (10/10) FINISHED                                                                                    docker:default
 => [internal] load build definition from Dockerfile                                                                            0.0s
 => => transferring dockerfile: 274B                                                                                            0.0s
 => [internal] load metadata for docker.io/library/python:3.7.4-alpine                                                          1.3s
 => [internal] load .dockerignore                                                                                               0.0s
 => => transferring context: 68B                                                                                                0.0s
 => [1/5] FROM docker.io/library/python:3.7.4-alpine@sha256:6673d8ce9610d166b6d7d6abda21537ddcf30e6bc8c20ca86f17f1085e20ac95    0.0s
 => [internal] load build context                                                                                               0.0s
 => => transferring context: 63B                                                                                                0.0s
 => CACHED [2/5] WORKDIR /opt/app                                                                                               0.0s
 => CACHED [3/5] COPY requirements.txt .                                                                                        0.0s
 => CACHED [4/5] RUN pip install --no-cache-dir -r requirements.txt                                                             0.0s
 => CACHED [5/5] COPY ./api.py .                                                                                                0.0s
 => exporting to image                                                                                                          0.0s
 => => exporting layers                                                                                                         0.0s
 => => writing image sha256:e593f2bb2d51d07894e58bb35f1188ef17ea6769e615ba010ac701f2101f4c2b                                    0.0s
 => => naming to docker.io/library/app:1.0                                                                                      0.0s


docker image ls
REPOSITORY   TAG       IMAGE ID       CREATED          SIZE
app          1.0       e593f2bb2d51   13 minutes ago   109MB


******************** RUNNING DOCKER INSTANCE **********************************
docker build -t app:1.0 .
[+] Building 0.3s (10/10) FINISHED                                                                                    docker:default
 => [internal] load build definition from Dockerfile                                                                            0.0s
 => => transferring dockerfile: 274B                                                                                            0.0s
 => [internal] load metadata for docker.io/library/python:3.7.4-alpine                                                          0.3s
 => [internal] load .dockerignore                                                                                               0.0s
 => => transferring context: 68B                                                                                                0.0s
 => [1/5] FROM docker.io/library/python:3.7.4-alpine@sha256:6673d8ce9610d166b6d7d6abda21537ddcf30e6bc8c20ca86f17f1085e20ac95    0.0s
 => [internal] load build context                                                                                               0.0s
 => => transferring context: 63B                                                                                                0.0s
 => CACHED [2/5] WORKDIR /opt/app                                                                                               0.0s
 => CACHED [3/5] COPY requirements.txt .                                                                                        0.0s
 => CACHED [4/5] RUN pip install --no-cache-dir -r requirements.txt                                                             0.0s
 => CACHED [5/5] COPY ./api.py .                                                                                                0.0s
 => exporting to image                                                                                                          0.0s
 => => exporting layers                                                                                                         0.0s
 => => writing image sha256:e593f2bb2d51d07894e58bb35f1188ef17ea6769e615ba010ac701f2101f4c2b                                    0.0s
 => => naming to docker.io/library/app:1.0                                                                                      0.0s
docker run --detach --rm -p 8000:8000 --name flask_app app:1.0
b7b2b5177439806c472a7eed33175f100ca4045cc1dd44aeb7977b3e5a7c6640


docker ps
CONTAINER ID   IMAGE     COMMAND                  CREATED        STATUS                  PORTS                                       NAMES
b7b2b5177439   app:1.0   "gunicorn -b 0.0.0.0…"   1 second ago   Up Less than a second   0.0.0.0:8000->8000/tcp, :::8000->8000/tcp   flask_app
```

A aplicação por meio do container `flask_ap` estará disponível em [http://localhost:8000](http://localhost:8000). Voce pode verificar se está tudo ok fazendo a seguinte requisição:

```bash
$ curl -sv localhost:8000/api/comment/list/1
*   Trying 127.0.0.1:8000...
* Connected to localhost (127.0.0.1) port 8000 (#0)
> GET /api/comment/list/1 HTTP/1.1
> Host: localhost:8000
> User-Agent: curl/7.81.0
> Accept: */*
> 
* Mark bundle as not supporting multiuse
< HTTP/1.1 404 NOT FOUND
< Server: gunicorn/20.0.4
< Date: Tue, 26 Mar 2024 01:09:42 GMT
< Connection: close
< Content-Type: application/json
< Content-Length: 68
< 
{
  "message": "content_id 1 not found", 
  "status": "NOT-FOUND"
}
* Closing connection 0
```

Para limpeza do ambiente execute o comando abaixo:

```bash
$ make clean

******************** KILLING CONTAINER **********************************
docker rm -f flask_app
flask_app

docker ps
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES


******************** REMOVING DOCKER IMAGE **********************************
docker image rm -f app:1.0
Untagged: app:1.0
Deleted: sha256:e593f2bb2d51d07894e58bb35f1188ef17ea6769e615ba010ac701f2101f4c2b

docker image ls
REPOSITORY   TAG       IMAGE ID   CREATED   SIZE

```

Existem outros comandos disponíveis no arquivo `Makefile`: `make buid`, `make run`, e `make publish`. Uma breve descrição segue abaixo:

| Comando      | Descrição |
|--------------|-------------|
| `make build`   | Build da imagem Docker             |
| `make run`     | Instanciação do container Docker            |
| `make publish` | Publicação da imagem Docker no DockerHub            |

### Execução Local

Caso deseje executar localmente, execute os seguintes comandos em máquina Linux:

```bash
$ pip install poetry==1.1.12
$ poetry install --no-dev --no-interaction --no-ansi
$ sudo apt install gunicorn
$ gunicorn --log-level debug api:app
```

A aplicação estará disponível em [http://localhost:8000](http://localhost:8000).

