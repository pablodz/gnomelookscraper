# specify the name of the Docker image
IMAGE_NAME=gnmelookscraper

# specify the name of the Python script
SCRIPT=scraper.py

# build the Docker image
build:
	docker build -t $(IMAGE_NAME) .

# run the Docker image
run:
	docker run $(IMAGE_NAME)

# remove the Docker image
clean:
	docker rmi $(IMAGE_NAME)

# run the Docker image in interactive mode
run-interactive:
	docker run -it $(IMAGE_NAME) /bin/bash
