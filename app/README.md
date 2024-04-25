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
flask_app

docker ps
CONTAINER ID   IMAGE                              COMMAND                  CREATED        STATUS        PORTS     NAMES


******************** REMOVING DOCKER IMAGE **********************************
docker image rm -f app:1.0
Untagged: app:1.0
Deleted: sha256:8d8e2f40b280037b55395c746fe184f01d2149cae6009d878fd26ee16a9bdaa7

docker image ls
REPOSITORY                                      TAG       IMAGE ID       CREATED       SIZE


******************** BUILDING & TAGGING DOCKER IMAGE **********************************
docker build -t app:1.0 .
[+] Building 1.3s (18/18) FINISHED                                                        docker:default
 => [internal] load build definition from Dockerfile                                                0.0s
 => => transferring dockerfile: 815B                                                                0.0s
 => [internal] load metadata for docker.io/library/python:3.9-alpine                                1.2s
 => [auth] library/python:pull token for registry-1.docker.io                                       0.0s
 => [internal] load .dockerignore                                                                   0.0s
 => => transferring context: 82B                                                                    0.0s
 => [builder 1/6] FROM docker.io/library/python:3.9-alpine@sha256:99161d2323b4130fed2d849dc8ba3527  0.0s
 => [internal] load build context                                                                   0.0s
 => => transferring context: 4.37kB                                                                 0.0s
 => CACHED [builder 2/6] WORKDIR /opt/app                                                           0.0s
 => CACHED [builder 3/6] RUN  pip install --upgrade pip && apk add -u build-base gcc musl-dev libf  0.0s
 => CACHED [builder 4/6] COPY pyproject.toml ./                                                     0.0s
 => CACHED [builder 5/6] RUN pip install poetry==1.1.12                                             0.0s
 => CACHED [builder 6/6] RUN poetry config virtualenvs.create false     && poetry install --no-dev  0.0s
 => CACHED [production 2/7] COPY --from=builder /opt/app/.venv /opt/app/.venv                       0.0s
 => CACHED [production 3/7] RUN apk --no-cache add musl-dev libgcc                                  0.0s
 => CACHED [production 4/7] WORKDIR /opt/app                                                        0.0s
 => CACHED [production 5/7] COPY api ./api                                                          0.0s
 => [production 6/7] COPY main.py .                                                                 0.0s
 => [production 7/7] COPY config.py .                                                               0.0s
 => exporting to image                                                                              0.0s
 => => exporting layers                                                                             0.0s
 => => writing image sha256:010a65eaa2f0a65cead73142b30a4d69e6d0e6f75f5e99fb93f0a7c7c1c266e0        0.0s
 => => naming to docker.io/library/app:1.0                                                          0.0s


docker image ls
REPOSITORY                                      TAG       IMAGE ID       CREATED                  SIZE
app                                             1.0       010a65eaa2f0   Less than a second ago   89MB


******************** RUNNING DOCKER INSTANCE **********************************
docker build -t app:1.0 .
[+] Building 0.3s (17/17) FINISHED                                                        docker:default
 => [internal] load build definition from Dockerfile                                                0.0s
 => => transferring dockerfile: 815B                                                                0.0s
 => [internal] load metadata for docker.io/library/python:3.9-alpine                                0.2s
 => [internal] load .dockerignore                                                                   0.0s
 => => transferring context: 82B                                                                    0.0s
 => [builder 1/6] FROM docker.io/library/python:3.9-alpine@sha256:99161d2323b4130fed2d849dc8ba3527  0.0s
 => [internal] load build context                                                                   0.0s
 => => transferring context: 179B                                                                   0.0s
 => CACHED [builder 2/6] WORKDIR /opt/app                                                           0.0s
 => CACHED [builder 3/6] RUN  pip install --upgrade pip && apk add -u build-base gcc musl-dev libf  0.0s
 => CACHED [builder 4/6] COPY pyproject.toml ./                                                     0.0s
 => CACHED [builder 5/6] RUN pip install poetry==1.1.12                                             0.0s
 => CACHED [builder 6/6] RUN poetry config virtualenvs.create false     && poetry install --no-dev  0.0s
 => CACHED [production 2/7] COPY --from=builder /opt/app/.venv /opt/app/.venv                       0.0s
 => CACHED [production 3/7] RUN apk --no-cache add musl-dev libgcc                                  0.0s
 => CACHED [production 4/7] WORKDIR /opt/app                                                        0.0s
 => CACHED [production 5/7] COPY api ./api                                                          0.0s
 => CACHED [production 6/7] COPY main.py .                                                          0.0s
 => CACHED [production 7/7] COPY config.py .                                                        0.0s
 => exporting to image                                                                              0.0s
 => => exporting layers                                                                             0.0s
 => => writing image sha256:010a65eaa2f0a65cead73142b30a4d69e6d0e6f75f5e99fb93f0a7c7c1c266e0        0.0s
 => => naming to docker.io/library/app:1.0                                                          0.0s
docker run --net=host --detach --rm -p 8000:8000 --name flask_app app:1.0
WARNING: Published ports are discarded when using host network mode
fe68f002cdeaf6415b439952c122b5b2bd26a97aca2fc83c146d46cb931dda66


docker ps
CONTAINER ID   IMAGE                              COMMAND                  CREATED        STATUS                  PORTS     NAMES
fe68f002cdea   app:1.0                            "gunicorn -b 0.0.0.0…"   1 second ago   Up Less than a second             flask_app
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

