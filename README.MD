# Api Logs

## Run
    Na raiz do projeto
        $ sudo docker-compose up 

## Swagger
    localhost:8000/api/swagger/

### Infos
    - Api foi desenvolvida em ambiente linux - Ubuntu 20.04
    - Api foi testada utilizando Postman


### Endpoints
    - localhost:8000/api/v1 ... : faz algo
    
### Tests and Coverage
    Na raiz do projeto
        $ coverage run manage.py test
        $ coverage report
