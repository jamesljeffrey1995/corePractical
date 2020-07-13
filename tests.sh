#! /bin/bash
docker-compose build
docker-compose push
scp -i ~/.ssh/ansible_id_rsa .env corepractical:/home/jamesljeffrey1995/corePractical/.env
scp -i ~/.ssh/ansible_id_rsa docker-compose.yaml corepractical:/home/jamesljeffrey1995/corePractical/docker-compose.yaml
ssh -i ~/.ssh/ansible_id_rsa corepractical << EOF



. /home/jamesljeffrey1995/venv/bin/activate

cd /home/jamesljeffrey1995/corePractical/1_server/Testing
pytest --cov ~/corePractical/1_server/application

cd /home/jamesljeffrey1995/corePractical/corePractical/2_stance/Testing
pytest --cov ~/corePractical/1_server/application

cd /home/jamesljeffrey1995/corePractical/corePractical/3_trick/Testing
pytest --cov ~/corePractical/1_server/application

cd /home/jamesljeffrey1995/corePractical/corePractical/4_SKATE/Testing
pytest --cov ~/corePractical/1_server/application 
EOF
