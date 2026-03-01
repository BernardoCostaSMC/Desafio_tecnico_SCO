# Desafio Técnico Seu Cliente Oculto 

## Índice
- [Desafio Técnico do Processo Seletivo Seu Cliente Oculto](#desafio-técnico-seu-cliente-oculto)
  - [Índice](#índice)
  - [Descrição do Desafio](#descrição-do-desafio)
  - [Como executar o arquivo](#como-executar-o-arquivo)
    - [Requisitos](#requisitos)
    - [Passo a Passo](#passo-a-passo)
  - [Telas Desenvolvidas](#telas-desenvolvidas)
    - [Base.html](#basehtml)
    - [Tela de LogIn (login.html)](#tela-de-login-loginhtml)
    - [Tela de Cadastro (cadastro.html)](#tela-de-cadastro-cadastrohtml)
    - [Tela Home (home.html)](#tela-home-homehtml)
    - [Tela de Detalhes (detalhes.html)](#tela-de-detalhes-detalheshtml)
  - [Diagrama de Entidade-Relacionamento](#diagrama-de-entidade-relacionamento)
  - [Contato](#contato)

## Descrição do Desafio
O teste consiste no desenvolviento de um To Do List com autenticação de usuario. O único requisito obrigatório é o uso do Framework Django.<br> 
O projeto deve conter as seguintes telas:
- Tela de SignUp de usuário;
- Tela de LogIn de usuários cadastrados;
- Tela com uma Listagem das tarefas cadastradas por usuário;
- Tela para edição/criação de tarefas, exibindo os campos de titulo, descrição e status das tarefas.

## Como executar o arquivo
  ### Requisitos

- Python 3.12.6
- pip 26.0.1
- virtualenv 20.36.1 (opcional, mas recomendado)
- Git 2.47.0
- Django 6.0.2
  
### Passo a Passo
  1. Clone o repositório:
     1. Abra o 'git bash' na pasta escolhida para clonar o repositorio;
     2. No 'git bash' digite `git clone https://github.com/BernardoCostaSMC/Desafio_tecnico_SCO.git` e pressione  enter.
   
  2. Iniciando o ambiente virtual:
     1. Abra o 'CMD' na pasta do projeto e digite `venv\Scripts\activate` e pressione  enter no windows;
     2. ou `source venv/Scripts/activate` para Linux e Mac.
   
  3. Instalando as dependências adicionais:
     1. No 'CMD' execute o comando `pip install -r requirements.txt` para que as dependências adicionais sejam instaladas.
  
  4. Criação de Superusuario e Grupo de autorização:
     1.  Ainda no 'CMD' execute o comando `python manage.py createsuperuser`, ele vai solicitar uma nome de usuario(obrigatorio), email(opcional) e uma senha(obrigatorio)
     2.  Apos criar o Superusuario podemos no Django admin pelo link <a href="http://127.0.0.1:8000/admin/" target="_blank">127.0.0.1:8000/admin/</a>
     3.  Logando com o Superusuario podemos entrar na aba de Grupos, e criar um grupo chamado "Usuários" atribuindo a ele as autorizações desejadas na sessão de permissões.
   
  5. Executando o servidor do projeto:
     1. Ainda no 'CMD' execute o comando `python manage.py runserver` 
     2. Agora o prejeto está sendo executado e pode ser acessado pelo link <a href="http://127.0.0.1:8000" target="_blank">127.0.0.1:8000</a>



## Telas Desenvolvidas

### Base.html
A tela base é composta pelo cabeçalho da pagina e um include do rodapé. Ela serve como contêiner para as demais páginas.

### _footer.html
Partial responsavel por serpara o footer da tela base.html para que facilite a manutenção 

### Tela de LogIn (login.html)
Uma tela simples com campos de 'Nome de usuário' e 'Senha', além de botões como 'Entrar', que efetua o login caso os dados estejam corretos, e o botão 'Cadastre-se', que leva para a tela de cadastro onde é possível criar um usuário.
Essa tela chamada automaticamente quando a URL estiver sem parâmetro

![Tela de LogIn](./fotos_README/tela_Login.png)

### Tela de SignUp (signup.html)
Tela responsável pela criação de usuários para que possam acessar a aplicação por meio da tela de login. Esta tela conta com campos como 'Usuário', 'Senha' e 'Confirmação de Senha', além do botão 'Cadastrar' para salvar os dados inseridos caso estejam de acordo com a verificação standard do Django.

![Tela de Sigup](./fotos_README/tela_Sigup.png)

### Tela Lista de Tarefas (task_list.html)
Esta é a tela principal da aplicação, onde são mostradas cards que apresentam as tarefas para cada usuario, contendo o titulo, descrição, seu status, um botão para criar uma tarefa que leva para uma tela(task_create_form.html), um botão para editar a tarefa que leva para uma tela(task_edit_form.html) e um botão para deletar a tarefa que leva para uma tela(task_confirm_delete.html).

![Tela Lista de Tarefas](./fotos_README/tela_Lista.png)

### Tela de Criação de Tarefas (task_create_form.html)
A tela de Criação oferece uma visão mais detalhada para criação de tarefas, onde podemos criar uma tarefa nova colocando seu titulo, sua descrição e seu status. 

![Tela de Criação de Tarefas](./fotos_README/tela_Criação.png)

### Tela de Edição de Tarefas (task_edit_form.html)
A tela de Edição oferece uma visão mais detalhada para edição de tarefas, onde podemos editar o titulo, descrição e status de uma tarefa. 

![Tela de Edição de Tarefas](./fotos_README/tela_Edição.png)

### Tela de Confirmação de Exclusão de Tarefas (task_confirm_delete.html)
A tela de Confirmação de Exclusão é dedicada a uma confirmação do usuario para eclusão de tarefas.

![Tela de Confirmação de Exclusão de Tarefas](./fotos_README/tela_Exclusão.png)


---
