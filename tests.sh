#! /bin/bash
docker-compose build
docker-compose push
scp -i ~/.ssh/ansible_id_rsa .env corepractical:/home/jamesljeffrey1995/corePractical/.env
scp -i ~/.ssh/ansible_id_rsa docker-compose.yaml corepractical:/home/jamesljeffrey1995/corePractical/docker-compose.yaml
ssh -i ~/.ssh/ansible_id_rsa corepractical << EOF



. /home/jamesljeffrey1995/venv/bin/activate

cd /home/jenkins/.jenkins/workspace/corePractical/1_server
pytest --cov ./application

cd /home/jenkins/.jenkins/workspace/corePractical/2_stance
pytest --cov ./application

cd /home/jenkins/.jenkins/workspace/corePractical/3_trick
pytest --cov ./application

cd /home/jenkins/.jenkins/workspace/corePractical/4_SKATE
pytest --cov ./application 
