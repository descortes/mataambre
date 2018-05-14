## cheatsheet de docker
Es posible que necesiten ejecutar los comandos con `sudo`, según el sistema que usen y cómo lo hayan instalado.

```sh
# Run a command in a new container
docker run -ti IMAGEN /bin/sh

# Run container in background and print container ID
docker run -d IMAGEN 

# Ver qué containers existen
docker ps [-a]

# Ver qué imagenes hay en mi máquina
docker images

# Ver uso de recursos de containers (como "top" en linux)
# Ejemplo con formato específico: docker stats --format '{{.Name}}\t{{.ID}}\t{{.CPUPerc}}\t{{.MemUsage}}'
docker stats [--format <format_string>]

# Descargar una imagen
docker pull <image>[:<tag>]

# Eliminar un container
docker rm <container_id> [-f]

# Eliminar una imagen
docker rmi <image_id> [-f]

# Versión instalada
docker version

# Docker build image
docker build -t py/app .

### Docker compose

# Build and run your app with Compose
docker-compose up 

# Execute an interactive bash shell on the container.
docker exec -it ubuntu_bash bash

### docker-compose.yml

#Forwards the exposed port 5000 on the container to port 5000 on the host machine. We use the default port for the Flask web server, 5000.
	ports:
		-5000:5000


### cAdvisor

cAdvisor (Container Advisor) provides container users an understanding of the resource usage and performance characteristics of their running containers. It is a running daemon that collects, aggregates, processes, and exports information about running containers. Specifically, for each container it keeps resource isolation parameters, historical resource usage, histograms of complete historical resource usage and network statistics. This data is exported by container and machine-wide.


### Graphite does three things:

Kick ass.
Chew bubblegum.
Make it easy to store and graph metrics.

```
