# COMP6905 AWS/Docker Project

The following instructions describe how to successfully deploy an extended user authentication Django web application using CloudFormation stack and docker-compose script. 

Alternatively, you can follow along to this youtube tutorial http://........

## Overview
- Create cloudformation stack
- Edit .env values
- Build and push docker image to DockerHub
- Launch docker-compose to run container on AWS 


<h2>Instructions</h2>
<h3>CloudFormation Stack</h3>
1. Clone github repository to a new directory on local machine
2. Create EC2 key pair in AWS management console and save to project folder dir
3. Open GGEO_fullstack.yml and replace the MyKeyName parameter with your KeyName (line 26)
4. Run create_stack.sh
5. Once completed, open the Outputs tab on the CloudFormation page in AWS console. Save the access key and secret access in a text editor.
6. Open RDS instance on console, save RDS endpoint address to text file.
7. Open EC2 instance next, and save Public IP address and Public DNS address.

<h3>Edit .env values</h3>
1. Open .env.example file in text editor and rename file to .env
2. Replace aws_s3_access_key_id and aws_s3_secret_access_key with the values from CloudFormation Outputs
3. Replace RDS Host with RDS endpoint obtained from previous step.
4. (optional) Replace django_key with a random secret key that can be generated from https://www.miniwebtool.com/django-secret-key-generator/
5. Save changes and exit .env

<h3> Docker Image and Docker Hub </h3>
