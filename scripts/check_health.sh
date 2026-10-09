#!/bin/bash
echo "=== CORESENTINEL: INSPEÇÃO DE SAÚDE DOS CONTAINERS ==="
docker ps --format "table {{.Names}}\t{{.Status}}\t{{.Ports}}"

echo -e "\n=== TESTANDO RESPOSTA DO PROXY REVERSO (PORTA 80) ==="
HTTP_STATUS=$(curl -s -o /dev/null -w "%{http_code}" http://localhost/)

if [ "$HTTP_STATUS" -eq 200 ]; then
    echo "[OK] Nginx e Aplicação operando normalmente (HTTP $HTTP_STATUS)"
else
    echo "[ALERT] Falha detectada na resposta do serviço (HTTP $HTTP_STATUS)"
fi