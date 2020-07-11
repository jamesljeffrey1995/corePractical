#! /bin/bash
docker-compose build
docker-compose push
scp -i ~/.ssh/ansible_id_rsa .env corepractical:/home/jamesljeffrey1995/corePractical/.env
scp -i ~/.ssh/ansible_id_rsa docker-compose.yaml corepractical:/home/jamesljeffrey1995/corePractical/docker-compose.yaml
ssh -i ~/.ssh/ansible_id_rsa corepractical << EOF
cd /home/jamesljeffrey1995/corePractical
docker login -u "jamesljeffrey1995" -p "890111e5!" docker.io
docker-compose build
sudo docker-compose push
env MY_SECRET_KEY=${MY_SECRET_KEY} env USERNAME=${USERNAME} env PASSWORD=${PASSWORD} env IP=${IP} env DATABASE=${DATABASE}  docker stack deploy --compose-file docker-compose.yaml corePractical
EOF
