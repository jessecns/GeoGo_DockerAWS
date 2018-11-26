# COMP6905 AWS/Docker Project

The following instructions describe how to successfully deploy an extended user authentication Django web application using CloudFormation stack and docker-compose. 

Alternatively, you can follow along to this youtube tutorial https://www.youtube.com/watch?v=rILgSGPpHC0&t=1643s

## Overview
- Create cloudformation stack
- Edit .env values
- Build and push docker image to DockerHub
- Launch docker-compose to run container on AWS 


## Instructions
### CloudFormation Stack
1. Clone github repository to a new directory on local machine
2. Create EC2 key pair in AWS management console and save to project folder directory
3. Open ```GGEO_fullstack.yml``` and replace the ```MyKeyName``` parameter with your KeyPair (line 26)
4. Run aws cloudformation command in ```proj_commands.sh```
5. Once completed, open the ```Outputs``` tab on the CloudFormation page in AWS console. Save the access key id and secret access key in a text editor.
6. Open RDS instance on console, save RDS endpoint address to text file.
7. Open EC2 instance next, and save Public IP address and Public DNS address to text.

### Edit .env values
1. Open ```.env.example``` file in text editor and rename file to ```.env```
2. Replace ```aws_s3_access_key_id``` and ```aws_s3_secret_access_key``` with the values from CloudFormation Outputs
3. Replace ```RDS Host``` with RDS endpoint obtained from previous step.
4. (optional) Replace ```django_key``` with a random secret key that can be generated from https://www.miniwebtool.com/django-secret-key-generator/
5. Save changes and exit ```.env```

### Docker Image and Docker Hub
1. Open ```proj_commands.sh``` and replace all instances of ```jessecns/ggeo-django``` with ```yourdockerhubname/ggeo-django```
2. Also, replace DOCKER_HOST ip address with your EC2 ip address obtained from AWS console
3. Open ```docker-compose.yml``` and replace ```jessecns/ggeo-django``` with ```yourdockerhubname/ggeo-django```
3. Run docker build, docker image tag and docker image push commands

### Docker-Compose
1. Run the remainder of docker-compose commands in ```proj_commands.sh```(enter yes when prompted during collectstatic)
2. After ```docker-compose up -d``` is executed, go to EC2 public DNS address and GeoGo website will be up and running.
3. Explore site: register new users, subscribe to plans, change passwords, edit user profiles, view home page and pricing plans
4. To stop and remove containers, networks, volumes, and images created by up: ```docker-compose down -v --rmi all```

### (Optional) Run additional docker command
1. Create a django superuser to access Django's admin interface:  ```docker exec -it <container id> bash```
2. Once inside the running container type: ```python manage.py createsuperuser```
3. Fill out usrname, email, password
4. Access admin page and login as new superuser: "PublicDNSaddress"/admin 
