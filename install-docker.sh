#! /bin/bash
echo "installing docker"
curl https://get.docker.com | sudo bash
echo "create docker group"
sudo groupadd docker
echo "add user to docker group"
sudo usermod -aG docker $(whoami)
echo "log out and back in"
newgrp docker
echo "check docker works"
docker run hello-world
echo "install docker-compose"
sudo curl -L "https://github.com/docker/compose/releases/download/1.24.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
echo "making docker-compose executable"
sudo chmod +x /usr/local/bin/docker-compose
