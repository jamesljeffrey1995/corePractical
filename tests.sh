#! /bin/bash
docker-compose build
docker-compose push
scp -i ~/.ssh/ansible_id_rsa .env corepractical:/home/jamesljeffrey1995/corePractical/.env
scp -i ~/.ssh/ansible_id_rsa docker-compose.yaml corepractical:/home/jamesljeffrey1995/corePractical/docker-compose.yaml
ssh -i ~/.ssh/ansible_id_rsa corepractical << EOF



. /home/jenkins/corePractical/venv/bin/activate

cd /home/jenkins/corePractical/1_server/Testing
pytest --cov ~/corePractical/1_server/application

cd /home/jenkins/corePractical/2_stance/Testing
pytest --cov ~/corePractical/2_stance/application

cd /home/jenkins/corePractical/3_trick/Testing
pytest --cov ~/corePractical/3_trick/application

cd /home/jenkins/corePractical//4_SKATE/Testing
pytest --cov ~/corePractical/4_SKATE/application 
EOF
