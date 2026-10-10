# CoreSentinel | Architecture & Reliability Stack

**CoreSentinel** é uma demonstração prática de arquitetura para **Sustentação de Ambientes Conteinerizados (ITOps/N2/N3)**, focada em resiliência, diagnóstico de incidentes e observabilidade de causa-raiz em microserviços.

O projeto simula um ambiente de produção completo com **Proxy Reverso (Nginx)**, **API de Aplicação (FastAPI)** e **Banco de Dados Relacional (PostgreSQL)**, acompanhado de uma suíte de scripts para auditoria contínua e análise de logs.

---

## Arquitetura da Solução

O tráfego de entrada é centralizado no Nginx, garantindo que os componentes internos (API e Banco de Dados) permaneçam isolados em uma rede corporativa virtual (`core_sentinel_net`).

```text
 [ Cliente / Internet ]
           │
           ▼ (Porta 80)
┌─────────────────────────┐
│   Nginx Reverse Proxy   │
└────────────┬────────────┘
             │ (Rede Isolada Docker: core_sentinel_net)
             ▼
┌─────────────────────────┐      ┌─────────────────────────┐
│  FastAPI App (Python)   │ ────►│  PostgreSQL (Database)  │
└─────────────────────────┘      └─────────────────────────┘
             ▲
             │ (Auditoria & Diagnóstico Operacional)
┌────────────┴─────────────────────────────────────────────┐
│                 SUÍTE CORESENTINEL                       │
│  ├── check_health.sh  (Probe de Saúde N1/N2)            │
│  └── log_analyzer.py  (Parser de Causa-Raiz N2/N3)      │
└──────────────────────────────────────────────────────────┘
```
## Componentes do Ecossistema
* Nginx (Reverse Proxy):
Atua como Ponto Único de Entrada (Single Point of Entry), escondendo a arquitetura interna e realizando a ponte de comunicação na porta 80.

* FastAPI (Service Application): 
Aplicação backend que processa requisições de negócio e expõe rotas de auditoria e de erro simulado (/error) para validação de fluxos de exceção.

* PostgreSQL (Persistence Layer): 
Banco de dados relacional isolado sem exposição pública de portas.

## Suíte de Scripts de Sustentação:

### `check_health.sh`: 
Realiza a sondagem de integridade dos containers Docker em tempo real e inspeciona códigos de resposta HTTP.

### `log_analyzer.py`: 
Parser automatizado de logs para isolamento rápido do tempo médio de reparo (MTTR) e filtragem de falhas críticas `500 ERROR`.

## Guia de Operação (Runbook de Implantação)

## 1. Inicializando a Infraestrutura

Para subir toda a pilha de serviços em segundo plano:

```Bash
docker-compose up -d --build
```

Verifique se todos os containers estão ativos (coresentinel_nginx, coresentinel_app, coresentinel_db):

```Bash
docker ps
```

Procedimentos de Sustentação & Troubleshooting

### A. Sondagem de Saúde do Ambiente (L1/L2)
Para executar uma verificação rápida dos containers e da resposta do proxy:

```Bash
bash scripts/check_health.sh
```

### B. Simulação de Incidente (Trigger de Falha)
Acesse a rota de erro via navegador ou cURL para gerar exceções simuladas na aplicação:

```Bash
curl http://localhost/error
```

### C. Análise Automatizada de Causa-Raiz (L2/L3)
Execute o parser de logs para filtrar eventos do tipo ERROR ou FAILURE sem necessidade de varredura manual de logs brutos:

```Bash
python scripts/log_analyzer.py
```

## Habilidades e Conceitos Aplicados

Orquestração & Mapeamento de Redes: Docker, Docker Compose, redes virtuais do tipo bridge.

Segurança & Infraestrutura: Proxy Reverso, isolamento de portas e arquitetura de microserviços.

Automação & Sustentação: Shell Scripting (Bash), Python para parsing de dados/logs e diagnóstico de causa-raiz.

Governança & ITSM: Conceitos de Runbook, visibilidade de saúde de serviços, redução de MTTR (Mean Time to Repair) e gestão de incidentes.
