FROM jenkins/inbound-agent:latest

USER root

RUN apt-get update && apt-get install -y --no-install-recommends \
    python3 \
    python3-pip \
    python3-venv \
    sshpass \
    openssh-client \
    iputils-ping \
    fping \
    && rm -rf /var/lib/apt/lists/*

RUN python3 -m venv /opt/ansible && \
    /opt/ansible/bin/pip install --no-cache-dir \
    ansible-core \
    passlib \
    PyYAML \
    pynetbox \
    netaddr

ENV PATH="/opt/ansible/bin:${PATH}"

# Install Ansible collections
COPY ansible_requirements.yml /tmp/ansible_requirements.yml
RUN mkdir -p /usr/share/ansible/collections && \
    ansible-galaxy collection install -r /tmp/ansible_requirements.yml -p /usr/share/ansible/collections && \
    chmod -R +r /usr/share/ansible/collections

USER jenkins
