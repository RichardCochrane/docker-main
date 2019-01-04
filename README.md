# Docker Main

Main project for docker testing.

This project has two components:
- interaction with a mail service
- interaction with a reporting service

## Installation (local development)

1. `virtualenv venv`
2. `source venv/bin/activate`
3. `pip install -r requirements.txt`
4. `pip install -e .`
5. `pserve development.ini`

## Installation (docker)

1. Ensure that docker server is installed
2. Build image: `docker image build -t d_main .`
3. Setup network for docker containers: `docker network create d_test`
4. Run container as part of network: `docker container run -it -p 6543:6543 --rm --name docker_main -e MAIL_API_URL=http://docker_mail:5657 -e REPORTS_API_URL=http://docker_reports:5656 --network d_test d_main`
