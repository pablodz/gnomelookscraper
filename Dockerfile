# Reference: https://hub.docker.com/r/selenium/standalone-firefox
FROM selenium/standalone-firefox:4.1.2-20220131

# Install the packages as root.
USER root
RUN apt-get update -yqq && \
    apt-get install -yqq python3-pip python-is-python3 && \
    pip install requests selenium lxml

# Run the code as seluser, which is required by Selenium.
USER seluser
COPY scraper.py /home/seluser
WORKDIR /home/seluser

# Run the scraping job when a container is started.
ENTRYPOINT [ "python", "/home/seluser/scraper.py"]