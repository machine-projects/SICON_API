# SICON

`python version 3.7`

## instalando dependencias utilizando o pipenv
`pipenv install`

## Configuração
No arquivo `/config.py` alterar a conection string `SQLALCHEMY_DATABASE_URI` e a `SECRET_KEY `
No arquivo `/ main.py` alterar environment
Examplo: `create_app ('dev')`

## Migrate de banco de dados
Com o arquivo `/config.py` configurado a devidamente a string de conexão `SQLALCHEMY_DATABASE_URI`  e já instalou as dependencias, execute os comandos a baixo.
```
pipenv shell
flask db upgrade
```

## criando o primeiro usuario admin (REMOVER/COMENTAR ROTA APÓS PROCEDIMENTO)
Enviar requisição json POST para `/completeuser/firstadmin` com o seguinte corpo
```
   {
		 
"person":{
 	
    "birth_date": null,
    "cnpj": null,
    "company_name": null,
    "cpf": null,
    "gender": null,
    "name": null,
    "surname": null,
    "type": "Pessoa Fisica"
    },
		 
"address":{
				
"neighborhood": null,
"street": null,
"number":null,
"complement": null ,
"city": null
		 },
		 
"user": {
	"username": "admin",
	"password": "123",
	"is_admin": true
}
		
	 }
```
## executar dev
```
pipenv shell
python main.py
```

