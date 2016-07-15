# Luiza labs

##Procedimentos para rodar o projeto

Instalar os pacotes necessários
```
pip install -r requirements.txt
```

##Criar o banco de dados
```
./manage.py migrate
```
## Criar o superuser
```
./manage.py createsuperuser
```

##Rodar o servidor
```
./manage.py runserver
```

## Acessar o Admin para a população da base
```
http://localhost:8000/admin
```

##Acessar os dados dos Funcionários
```
curl -H "Content-Type: application/javascript" http://localhost:8000/employee/
```
