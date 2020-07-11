#! /bin/bash
docker-compose build
docker-compose push
scp docker-compose.yaml corepractical:/home/jamesljeffrey1995/corePractical/docker-compose.yaml
ssh corepractical << EOF
cd /home/jamesljeffrey1995/corePractical
env MY_SECRET_KEY=${MY_SECRET_KEY} env USERNAME=${USERNAME} env PASSWORD=${PASSWORD} env IP=${IP} env DATABASE=${DATABASE}  docker stack deploy --compose-file docker-compose.yaml corePractical
EOF
