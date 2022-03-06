UNAME := $(shell whoami)
UID := $(shell id -u `whoami`)
HOSTNAME := $(shell hostname)
GROUPNAME := $(shell id -gn `whoami`)
GROUPID := $(shell id -g `whoami`)

PROJECT ?= reverse-dictionary
MOUNT_DIR ?= `pwd`

DOCKER_TAG ?= main
DOCKER_IMAGE := cs224n-$(PROJECT):$(DOCKER_TAG)
DOCKER_NAME := cs224n-$(PROJECT)-$(DOCKER_TAG)

DOCKER_MOUNTS += -v $(MOUNT_DIR):/app

build_docker:
	docker build -t $(DOCKER_IMAGE)-latest --network host -f docker/Dockerfile docker

add_user_docker: build_docker
	@echo "Adding current user to $(DOCKER_IMAGE)"
	docker build -t $(DOCKER_IMAGE) \
		--network host \
		--build-arg BASE_IMAGE=$(DOCKER_IMAGE)-latest \
		--build-arg GID=$(GROUPID) \
		--build-arg UID=$(UID) \
		--build-arg GROUP=$(GROUPNAME) \
		--build-arg USER=$(UNAME) \
		--build-arg SHELLNAME=cs224n-$(PROJECT) \
		- < docker/add_user.docker

launch_docker: add_user_docker
	@echo "Launching Docker session"
	docker run --gpus=all --rm -it \
		--shm-size=16gb \
		--name $(DOCKER_NAME) -h $(DOCKER_NAME) -p 8888:8888 -p 8000:8000 \
		--user $(UID):$(GROUPID) \
		$(DOCKER_MOUNTS) \
		$(DOCKER_ARGS) \
		$(DOCKER_IMAGE) \
		/bin/bash
