FROM jenkins/jenkins:lts

USER root

# Install Docker CLI and Python tools used by the pipeline.
RUN apt-get update \
    && apt-get install -y docker.io python3 python3-pip \
    && rm -rf /var/lib/apt/lists/*
