# Arquitetura da Solução

Este projeto segue uma arquitetura modular para facilitar manutenção, testes e evolução.

## Visão geral

```txt
Google Drive
   ↓
GoogleDriveService
   ↓
XMLAuditProcessor
   ↓
JSON estruturado
   ↓
APIClient
   ↓
FastAPI Receiver
   ↓
Banco de dados / Frontend
```

## Componentes

### GoogleDriveService

Responsável por autenticar com Google Drive usando Service Account, listar arquivos XML em uma pasta e baixar os documentos para processamento local.

### XMLAuditProcessor

Responsável por ler XMLs compactos, lidar com namespaces, extrair dados via XPath e adicionar marca de auditoria usando `xml.etree.ElementTree`.

### APIClient

Cliente HTTP responsável por enviar o payload JSON para uma API externa.

### FastAPI Receiver

API de exemplo que recebe o payload de auditoria, valida com Pydantic e representa o ponto de entrada para persistência no banco de dados.

## Dados extraídos

- Número da nota
- Série
- Data de emissão
- Chave de acesso
- CNPJ do emitente
- Nome do emitente
- CNPJ/CPF do destinatário
- Nome do destinatário
- Valor total
- Produtos
- NCM
- CFOP
- Quantidade
- Valor unitário
- Valor total por item

## Estratégia para produção

Para um ambiente real, recomenda-se adicionar:

- Controle de arquivos já processados.
- Persistência em PostgreSQL ou SQL Server.
- Logs centralizados.
- Retry em falhas de API.
- Fila assíncrona para alto volume.
- Docker Compose.
- Dashboard de auditoria.
