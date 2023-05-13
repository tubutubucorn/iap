NETWORK_NAME = private_nw

up:
	@if [ -z "`docker network ls | grep $(NETWORK_NAME)`" ]; then docker network create $(NETWORK_NAME) --subnet=172.28.0.0/24; fi
	docker-compose up -d

down:
	docker-compose down
	@if [ -n "`docker network inspect $(NETWORK_NAME) | grep \"\\"Containers\\": {}\"`" ]; then docker network rm $(NETWORK_NAME); fi

