# Hello World - Flask application

Aplicação Flask Hello World usando AWS Elastic Beanstalk com Continuous Delivery through AWS CodeBuild

- [Hello World - Flask application](#hello-world---flask-application)
  - [Pré-requisitos](#pré-requisitos)
  - [Steps](#steps)
  - [References](#references)


## Pré-requisitos

- [Configurar aws cli](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html), 
- [Configurar Git](https://git-scm.com/book/en/v2/Getting-Started-First-Time-Git-Setup#Your-Identity), 
- [Configurar ssh-key no Github](https://docs.github.com/pt/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent)
- [Instalar Elastic Beanstalk CLI](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/eb-cli3-install.html)
- [Configurar Elastic Beanstalk CLI](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/eb-cli3-configuration.html)

## Steps

1. Create a folder with files:
   
   `Makefile`: with make instructions

   `requirements.txt`: with python packages

   `buildspec.yml`: with build specifications for CodeBuild

2. Write a Flask application
    
    `application.py`

3. Optionally, write tests
    
    `test_application.py`

4. Create application and enviroment with Elastic Beanstalk CLI
    ```
    eb init -p python-3.7 flaskhelloworld --region sa-east-1
    eb init
    eb create flaskhelloworld-env
    eb open
    eb terminate flaskhelloworld-env
    ```
5. Create CodeBuild project and link to github repository
6. Commit changes and check CodeBuild project build status.


## References

- [Youtube - Noah Gift - Flask Elastic Beanstalk](https://www.youtube.com/watch?v=iSv-i1tWpQc)
- [Github noahgift - Flask-Elastic-Beanstalk](https://github.com/noahgift/Flask-Elastic-Beanstalk)
- [Github noahgift - Hugo AWS Continuous Delivery](https://github.com/noahgift/hugo-duke-jan23)
- [AWS - Deploying a Flask application to Elastic Beanstalk](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create-deploy-python-flask.html)
- [AWS Elastic BeanstalkExemplo de CodeBuild](https://docs.aws.amazon.com/pt_br/codebuild/latest/userguide/sample-elastic-beanstalk.html)