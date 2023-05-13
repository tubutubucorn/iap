NETWORK_NAME = DMZ
NETWORK_NAME2 = private_nw
NETWORK_NAME3 = control_plane

up:
	@if [ -z "`docker network ls | grep $(NETWORK_NAME)`" ]; then docker network create $(NETWORK_NAME) --subnet=172.30.0.0/24; fi
	@if [ -z "`docker network ls | grep $(NETWORK_NAME2)`" ]; then docker network create $(NETWORK_NAME2) --internal; fi
	@if [ -z "`docker network ls | grep $(NETWORK_NAME3)`" ]; then docker network create $(NETWORK_NAME3) --internal; fi
	docker-compose up -d

down:
	docker-compose down
	@if [ -n "`docker network inspect $(NETWORK_NAME) | grep \"\\"Containers\\": {}\"`" ]; then docker network rm $(NETWORK_NAME); fi
	@if [ -n "`docker network inspect $(NETWORK_NAME2) | grep \"\\"Containers\\": {}\"`" ]; then docker network rm $(NETWORK_NAME2); fi
	@if [ -n "`docker network inspect $(NETWORK_NAME3) | grep \"\\"Containers\\": {}\"`" ]; then docker network rm $(NETWORK_NAME3); fi

