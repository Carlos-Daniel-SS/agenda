# Django Site Agenda

## Descrição

Este é um projeto Django que implementa uma agenda com diversas funcionalidades, incluindo criação, edição e remoção de eventos.

## Instalação

1. *Clone o repositório:*

    bash
    git clone [https://Carlos-Daniel-SS/agenda.git]
    cd agenda
    

2. *Crie e ative um ambiente virtual (recomendado):*

    bash
    python -m venv venv
    source venv/bin/activate  # Para Linux/Mac
    venv\Scripts\activate  # Para Windows
    

3. *Instale as dependências:*

    bash
    pip install -r requirements.txt
    

4. *Aplique as migrações:*

    bash
    python manage.py migrate
    

5. *Inicie o servidor de desenvolvimento:*

    bash
    python manage.py runserver
    

### Login
Para utilizar o login o usuário deve ser previamente cadastrado utilizando os comandos

## Projeto

### Home
A tela inicial apresenta os agendamentos mais recentes do dia.
![home](https://github.com/Carlos-Daniel-SS/agenda/assets/69223907/4ce17337-d357-4205-bd25-f2c451585b5a)


### Criação

O projeto permite a criação de novos eventos de forma intuitiva. O usuário pode definir o título do seu evento, a data e uma descrição.

![criar](https://github.com/Carlos-Daniel-SS/agenda/assets/69223907/5af8a961-3840-414b-abff-f9ad0cfc983b)

### Edição

No projeto é possível realizar a edição dos eventos cadastrados.

![editar](https://github.com/Carlos-Daniel-SS/agenda/assets/69223907/358d79c4-70bb-49db-b80b-f443a066c816)

### Remoção

E por fim é possível realizar a remoção do evento de acordo o usuário logado.
Até o momento o projeto está apenas com básico, procuro realizar vários upgrades... Conto com susgestões.
