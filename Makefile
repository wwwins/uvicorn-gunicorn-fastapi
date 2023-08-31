DOCKER = sudo docker
MKDIR = sudo mkdir -p
CP = sudo cp
RUN = run --rm

# Tag
APP_TAG = 1.0.0

default: build
build:
	@echo
	@echo "Build a isobar inferance:$(APP_TAG) image"
	$(DOCKER) build -t isobar/ai-service:$(APP_TAG) -f Dockerfile .

build-pytorch:
	@echo
	@echo "Build a pytorch:$(APP_TAG) image"
	$(DOCKER) build -t isobar/pytorch:$(APP_TAG) -f Dockerfile-pytorch .

build-fastapi:
	@echo
	@echo "Build a fastapi:$(APP_TAG) image"
	$(DOCKER) build -t isobar/fastapi:$(APP_TAG) -f Dockerfile-fastapi .

run:
	@echo
	@echo "Start an app:$(APP_TAG)"
	$(DOCKER) $(RUN) --name ai-service -p 80:80 isobar/ai-service:$(APP_TAG)

dev:
	@echo
	#echo "Start an dev app:$(APP_TAG)"
	$(DOCKER) $(RUN) --name ai-service -p 80:80 -v `pwd`:/app isobar/ai-service:$(APP_TAG)

stress:
	@echo
	@echo "Stressing"
	@sh/stressing.sh -c 1

stress-loop:
	@echo
	@echo "Stressing loop"
	@sh/stressing.sh -c 100
