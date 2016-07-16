# Luizalabs Employee Manager

##Procedimentos para rodar o projeto

###Instalar os pacotes necessários
```
pip install -r requirements.txt
```

###Criar o banco de dados
```
./manage.py migrate
```
### Criar o superuser
```
./manage.py createsuperuser
```
### Testando o projeto
```
./manage.py test employee
```

###Rodar o servidor
```
./manage.py runserver
```

### Popular a base

#### Através do Admin
```
http://localhost:8000/admin
```
#### Através da fixture
```
./manage.py loaddata initial_data
```

###Acessar os dados dos Funcionários
```
curl -H "Content-Type: application/javascript" http://localhost:8000/employee/
```
