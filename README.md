# CRUD de clientes envolvendo Flask, Docker, Mysql:

Baseado nas demandas do exercício, foi criado um cadastro de clientes (nome, email, senha). Podendo
consultar a lista, inserir um novo cliente, atualizar informações (nome, email), e mudar a senha.

### Observações:

* A lista de clientes é retornada em uma string jwt, pode usar esse site para visualizar o conteudo: https://jwt.io/
* No cadastro de um novo cliente ou alteração de senha, a mesma é "criptografada" antes de ser salva no banco, para não deixar exposto. 
* Em momento algum ela retorna como um campo na lista de cliente.  

### Como executar

* Configurei de forma que a api e o banco ficam em containers. Basta abrir um terminal no diretório onde esta o arquivo
docker-compose.yml e digitar o comando: docker-compose up 

### Endpoints

* https://documenter.getpostman.com/view/8508677/TVejgpyN
* Basta acessar o link acima, os endpoints e os modelos de payload estão disponíveis

### Testes Unitários

* Desenvolvi testes unitários para verificar o fluxo de cada função. 

### Como executar os testes

* Basta abrir um terminal na pasta app, e executar no terminal o comando pytest test_enpoints.py
* No caso de utilizar Pycharm, só criar um Unnitest profile no edit configurations do canto superior direito
* Após subir o docker-compose, digitar docker ps para copiar o id do container que possui o banco. Usar o comando docker inspect <id_do_container> para pegar o ip do mesmo, e inserir como valor na chave host da função conexao_db antes de rodar os testes.

