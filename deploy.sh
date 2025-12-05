#!/bin/bash
cd /root/langchain-course
git pull origin infra/cloud-setup
docker-compose down
docker-compose up -d --build
