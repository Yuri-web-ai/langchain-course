#!/bin/bash
# deploy.sh — запускается на сервере

echo "Запуск деплоя..."

# 1. Перейти в папку
cd /root/langchain-course || exit

# 2. Обновить код
git pull origin infra/cloud-setup

# 3. Получить SSL (если домен есть)
if [ -n "$DOMAIN" ]; then
    certbot certonly --standalone -d $DOMAIN --non-interactive --agree-tos -m admin@$DOMAIN
    cp /etc/letsencrypt/live/$DOMAIN/fullchain.pem nginx/certs/
    cp /etc/letsencrypt/live/$DOMAIN/privkey.pem nginx/certs/
fi

# 4. Перезапустить Docker
docker-compose down
docker-compose up -d --build

echo "Деплой завершён! Открой: https://$DOMAIN"
