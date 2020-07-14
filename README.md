# Themisto Reports Authentication

`python version 3.7`

## install dependencies using pipenv
`pipenv install`

## Configuration
In the file `/config.py` change the `SQLALCHEMY_DATABASE_URI` connection string and its SECRET_KEY 
In the `/ main.py` file set the desired environment
changing the do_ create_app parameter.
Example: `create_app ('dev')`

## Run
`
pipenv shell
`

`
python main.py
`
select u.id, u.username,p.id as personID ,p."name" , p.surname , p."type" , ad.street       
from   users as u 
join person as p
	on u.person_id = p.id
join address as ad 
	on ad.person_id = p.id
where u.id  = 19
