#! /bin/bash
docker-compose build
docker-compose push
scp -i ~/.ssh/ansible_id_rsa .env corepractical:/home/jamesljeffrey1995/corePractical/.env
scp -i ~/.ssh/ansible_id_rsa docker-compose.yaml corepractical:/home/jamesljeffrey1995/corePractical/docker-compose.yaml
ssh -i ~/.ssh/ansible_id_rsa corepractical << EOF



. /home/jamesljeffrey1995/venv/bin/activate

cd /home/jamesljeffrey1995/corePractical/1_server/Testing
sudo pytest --cov ~/corePractical/1_server/application

cd /home/jamesljeffrey1995/corePractical/2_stance/Testing
sudo pytest --cov ~/corePractical/2_stance/application

cd /home/jamesljeffrey1995/corePractical/3_trick/Testing
sudo pytest --cov ~/corePractical/3_trick/application

cd /home/jamesljeffrey1995/corePractical//4_SKATE/Testing
sudo pytest --cov ~/corePractical/4_SKATE/application 
EOF
