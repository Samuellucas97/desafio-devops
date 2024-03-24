# Registro de reflexões

Dia 23/Março (madrugada)

- Avaliando os requisitos e ferramentas open source necesárias. 

    -  Para Cloud, eu decidi usar o GPC já que a vaga faz menção a ela (espero que não esteja cara kkk).

    - Para o requisito de IaaC - criação da VMS, estou pensando em usar ou Terraform, ferramentas famosas por configurar infra de forma declarativa. 

    -  Para pipeline de CD, tenho duas opções gratuitas famosas: github actions e gitlab ci. Pessoalmente não vejo muita diferença entre uma e outra

        - Verifiquei que não tem testes automatizados. Acho que no final vale a pena adicionar. 

    - Acredito que o uso de API Gateway é bastante fundamental. O Kong é bastante famoso como uma solução open-source.

    - Para aumentar a resiliência, pretendo instalar um cluster kubernetes, Pretendo usar o Ansible para instalação de um cluster kubernetes microk8s. A instalação dele é mais simples que a do kubeadmin.

    - configura o pacote de observabilidade do microk8s. Dessa forma, já habilito o monitoramento do cluster


- Scripts a serem criados

    - Dockerfile

    -  Makefile

    - pasta .github (Github Actions)

    - Deployment/Service (Kubernetes)

    - pasta terraform

    - pasta ansible

Acho que vou trabalhar só com a branch main, já que sou só eu. Do contrário, eu criaria a develop e bloquearia a main e develop para commit direto, apenas pull request com revisão obrigatória. Isso principalmente porque não há testes automatizados implementados

(Vou dormir)

Dia 23/Março (tarde)

- Resolvi criar primeiramente uma infraestrutura local usando vagrant para provisionamento da VM com o cluster e o API Gateway e só depois mover para a nuvem.
   - Assim posso evitar gastos desnecessários com a GPC e usá-la só na instanciação final. 

- Estou pensando no pipeline as seguinte etapas: test

- Também pretendo mudar o README.md atual para ser CHALLENGE.md, e criar um novo README.md contendo informações sobre o projeto em si: requisitos, como instalar e executar, por exemplo. Também vou criar um README.md para o app em si, explicando também informações sobre o app em si. Como todos os documentos encontrados estão em portugues, vou escrever em portugues mesmo. 

- Primeiro passo é executar a aplicação flask - e documentar para como foi feita - para aí então pensarmos em containerização.

- Mas antes disso, voi fazer o desenho da arquitetura de implantação que estou pensando

- Fazendo o desenho, fiz uma versão da infra local usando VMs via Vagrant e estava fazendo outro desenho supondo como seria na nuvem. Fiquei em dúvida se era necessário (ou permitido) uso de cloud já que a descrição fala  que as ferramentas precisam ser open-source, porém quando vi iaas, ficou claro para mim que sim a principio. Porém vi que parecia especificamente relacionado a provisionamento de hosts. Mandei a pergunta por desencargo de consciẽncia

  - O ambiente local tem suas vantagens de me permitir testar os arquivos de configuração Docker (i.e., Dockerfile) e Kubernetes (i.e., Deployment e Service) de forma gratuita, basta subir um cluster microk8s com o Vagrant. Como minha máquina tem 16gb de ram, não há tanta preocupação de falta de recurso.

- Vi que a descrição da vaga fala sobre domínio em AWS e Google Cloud Platform (GPC). Resolvi usar GPC pela comunidade ser maior.

- Resolvi colocar o api gateway kong dentro do cluster também para aumentar a resiliencia e a escalabilidade

- Percebi que posso testar o script ansible no ambiente local. Basta que eu crie uma vm usando uma imagem base linux ubuntu que eu tenha instalado o python. Já o ambiente na cloud serve para testar o script de implantação contínua. E também o script terraform que sobe a vm na aws, o EC2 

- Instalei os pacotes e executei a aplicação flask. Fiz algumas requisições de post e get.
- Estou criando o dockerfile, vou criar usando dockerfile multi-stage.
	- É uma solução mais segura e enxuta porque na versão final do container só haverá o código e biblitecas necessárias em runtime. Isso é importante para aqueles casos que fazem varios apt installs, por exemplo compilador c. Apesar do código atual não usar nada do tipo, acho que a longo prazo evitar que a build cresca anormalmente porque alguém precisou de algo.
	- Também é possível economizar em execuções fazendo cache de passos intermediarios.
	- aproveitei para colocar um dockerignore para impedir que sejam colocadas coisas que não se devem na imagem docker

- Agora que eu lembrei, esqueci de criar um .gitignore. 
- Finalizei o dockerfile, testei apenas o build, não a execução. Mas aproveitei para fazer um script make para facilitar o build (com tag). Agora basta digitar make que é executado o build

Dia 24/Março (tarde)

- No teste do container verifiquei que precisava corrigir certos pontos do dockerfile. Tinha esquecido de colocar o host sendo 0.0.0.0. Não consegui executar via multi-stage, ficava dando problema no gunicorn, como se ele não estive ok. Decidi prosseguir, depois vejo essa otimização. De qualquer modo, já estou usando imagem alpine para reduzir o tamanho. Porém deixei como backup.
- Aproveitei para melhorar o makefile. Eu gosto muito do uso de script make porque para mim é mais fácil lembrar: make, make build, make clean.
- Vou trabalhar agora na parte de kubernetes, mas não vou esquecer de publicar a minha imagem docker no Dockerhub. Antes disso, não me esqueci de atualizar a documentação do README da pasta `app`.