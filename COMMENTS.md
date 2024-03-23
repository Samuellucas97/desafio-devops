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