# Introdução aos Microserviços

## O que são Microserviços?

Microserviços são um estilo arquitetônico de desenvolvimento de software que estrutura aplicações como uma coleção de serviços pequenos, independentes e modulares. Cada serviço executa um processo de negócio específico, funciona de maneira autônoma, e se comunica com outros serviços através de interfaces bem definidas, normalmente APIs.

### Características Principais

- **Independência**: Serviços podem ser desenvolvidos, implantados, e escalados independentemente.
- **Especialização**: Cada serviço é especializado em uma função ou recurso específico.
- **Descentralização**: Gestão descentralizada de dados e processos.
- **Flexibilidade Tecnológica**: Possibilidade de usar diferentes tecnologias e linguagens em serviços distintos.

## Diferença entre Microserviços e APIs Comuns

Enquanto microserviços e APIs são frequentemente discutidos juntos, eles representam conceitos distintos:

- **Microserviços**: Referem-se a uma abordagem arquitetônica para construir uma aplicação como um conjunto de serviços menores e independentes. Cada microserviço é focado em realizar uma função específica e se comunica com outros serviços.

- **APIs (Interface de Programação de Aplicações)**: São interfaces que permitem a comunicação entre diferentes peças de software. Em uma arquitetura de microserviços, os serviços frequentemente se comunicam entre si através de APIs, mas as APIs podem existir em muitos outros contextos e arquiteturas de software.

Em suma, microserviços utilizam APIs para interagir, mas a ideia de API é muito mais ampla e não se limita à arquitetura de microserviços.

## Como Iniciar com Microserviços

### Passo 1: Compreensão dos Fundamentos

Antes de mergulhar na criação de microserviços, é crucial entender os princípios fundamentais e as motivações por trás dessa abordagem arquitetônica. Livros como "Building Microservices" de Sam Newman podem ser uma excelente introdução.

### Passo 2: Definição do Domínio e Design

- Identifique os limites de domínio da sua aplicação. Isso ajudará a definir os serviços.
- Projete cada microserviço para ser autônomo e responsável por uma parte específica da funcionalidade de negócios.

### Passo 3: Escolha das Tecnologias

Decida as tecnologias e linguagens de programação adequadas para cada serviço. Microserviços oferecem a flexibilidade de combinar várias tecnologias em uma única aplicação.

### Passo 4: Desenvolvimento e Teste

Comece desenvolvendo serviços individualmente. Adote práticas de desenvolvimento que facilitam a independência e a escalabilidade, como containers. Não se esqueça da importância dos testes automatizados.

### Passo 5: Implementação de Comunicação entre Serviços

Defina como os serviços se comunicarão (REST, gRPC, mensageria etc.). Implemente APIs claras e bem documentadas para facilitar essa comunicação.

### Passo 6: Implantação e Monitoramento

Utilize ferramentas de CI/CD para automatizar a implantação dos serviços. Implemente monitoramento e logging para garantir a visibilidade e a saúde da aplicação.



# Projeto: Sistema de Notificações

**Descrição**: Um sistema de notificações simples composto por dois microserviços:
1. **Microserviço de Usuários** - Responsável por gerenciar usuários.
2. **Microserviço de Notificações** - Responsável por enviar notificações aos usuários.

### Tecnologias Utilizadas

- **Linguagem de Programação**: Python
- **Framework Web**: Flask, para criar as APIs dos microserviços.
- **Comunicação entre Serviços**: HTTP RESTful API
- **Banco de Dados**: SQLite, para simplicidade.

### Estrutura do Projeto

- **Microserviço de Usuários**:
  - **Funcionalidades**: Adicionar um novo usuário, listar usuários.
  - **Endpoints**:
    - POST `/users` - Adiciona um novo usuário.
    - GET `/users` - Lista todos os usuários.

- **Microserviço de Notificações**:
  - **Funcionalidades**: Enviar uma notificação para um usuário específico.
  - **Endpoints**:
    - POST `/notify/{userId}` - Envia uma notificação para o usuário especificado.

### Como Executar o Projeto

#### Passo 1: Preparação do Ambiente

Certifique-se de que Python e pip estejam instalados. Instale as dependências (Flask) para ambos os serviços.

#### Passo 2: Implementação dos Microserviços

**Microserviço de Usuários (`users_service.py`)**:
- Implemente os endpoints usando Flask.
- Utilize SQLite para armazenar os dados dos usuários.

**Microserviço de Notificações (`notifications_service.py`)**:
- Implemente o endpoint de notificação.
- Faça uma chamada HTTP para o microserviço de usuários para obter as informações do usuário antes de enviar a notificação.

#### Passo 3: Execução dos Serviços

- Execute cada microserviço em seu próprio terminal:
  - `python users_service.py`
  - `python notifications_service.py`

#### Passo 4: Testando a Comunicação

- Utilize uma ferramenta como Postman ou curl para testar os endpoints. Adicione um novo usuário através do microserviço de usuários e, em seguida, envie uma notificação para esse usuário utilizando o microserviço de notificações.

### Funcionamento

1. **Adição e Listagem de Usuários**: O microserviço de usuários permite adicionar novos usuários ao sistema e listar todos os usuários registrados.
2. **Envio de Notificações**: Para enviar uma notificação, o microserviço de notificações consulta o microserviço de usuários para obter as informações necessárias do usuário destinatário. Em seguida, ele procede com o envio da notificação.

### Conclusão

Este projeto simples demonstra a interação entre microserviços em um cenário prático. A comunicação entre os microserviços é essencial para o funcionamento do sistema como um todo, destacando a importância de APIs bem definidas e a autonomia de cada serviço. Este exemplo serve como base para explorar conceitos mais avançados, como autenticação entre serviços, balanceamento de carga, e implementação de um gateway de API para sistemas mais complexos.