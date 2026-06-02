# XML Auditoria Automation

Automação em Python para processar arquivos XML rígidos e compactos diretamente do Google Drive, extrair dados críticos com XPath, normalizar documentos com `xml.etree.ElementTree`, gerar JSON estruturado e enviar o payload para uma API integrada ao banco de dados e ao frontend.

## Destaque para recrutadores

Este projeto demonstra competências práticas em automação backend, integração com APIs externas, processamento de documentos XML, estruturação de dados, arquitetura modular, FastAPI e preparação para persistência em banco de dados.

A solução foi pensada para cenários reais onde empresas recebem arquivos XML em massa e precisam auditar, validar, transformar e disponibilizar essas informações para sistemas internos.

## Fluxo da solução

```txt
Google Drive
   ↓
Busca arquivos XML
   ↓
Baixa e processa documentos
   ↓
Extrai dados com XPath
   ↓
Altera/normaliza XML com ElementTree
   ↓
Gera JSON estruturado
   ↓
Envia para API FastAPI
   ↓
API salva no banco
   ↓
Frontend consome os dados
```

## Stack utilizada

- Python 3.11+
- Google Drive API
- XPath com `lxml`
- Manipulação XML com `xml.etree.ElementTree`
- FastAPI
- Pydantic
- Requests
- PostgreSQL/SQL Server ready
- Arquitetura modular orientada a serviços

## Funcionalidades

- Conexão com Google Drive via Service Account.
- Busca automática de arquivos `.xml` em uma pasta configurada.
- Leitura de XMLs compactos, com namespace e estrutura rígida.
- Extração de dados cruciais usando XPath.
- Normalização e alteração de XML com `ElementTree`.
- Conversão dos dados selecionados para JSON.
- Envio do payload para API REST.
- API pronta para persistência em banco e integração com frontend.
- Estrutura segura para credenciais e arquivos sensíveis.

## Estrutura do projeto

```txt
xml-auditoria-automation/
│
├── api/
│   └── main.py
│
├── src/
│   ├── main.py
│   ├── config.py
│   │
│   ├── services/
│   │   ├── google_drive_service.py
│   │   ├── xml_processor.py
│   │   └── api_client.py
│   │
│   ├── models/
│   │   └── schemas.py
│   │
│   └── utils/
│       └── logger.py
│
├── docs/
│   ├── arquitetura.md
│   └── database.sql
│
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

## Instalação

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Copie o arquivo de ambiente:

```bash
cp .env.example .env
```

Configure no `.env`:

```env
GOOGLE_DRIVE_FOLDER_ID=
GOOGLE_CREDENTIALS_FILE=credentials/service_account.json
API_ENDPOINT=http://localhost:8000/api/auditoria/xml
API_TOKEN=token-interno-da-api
```

## Executar a automação

```bash
python -m src.main
```

## Executar a API local

```bash
uvicorn api.main:app --reload
```

Documentação interativa:

```txt
http://localhost:8000/docs
```

## Exemplo de payload JSON

```json
{
  "arquivo": "nota_123.xml",
  "origem": "GOOGLE_DRIVE",
  "tipo_documento": "XML_NFE",
  "status": "PROCESSADO",
  "dados": {
    "numero_nota": "123",
    "serie": "1",
    "data_emissao": "2026-06-02T09:00:00-03:00",
    "cnpj_emitente": "12345678000199",
    "nome_emitente": "EMPRESA EXEMPLO LTDA",
    "cnpj_destinatario": "98765432000188",
    "nome_destinatario": "CLIENTE EXEMPLO LTDA",
    "valor_total": "1500.00",
    "chave_acesso": "33260612345678000199550010000001231000001234",
    "produtos": []
  }
}
```

## Status sugeridos

```txt
PENDENTE
PROCESSANDO
PROCESSADO
ERRO
REPROCESSADO
```

## Diferenciais técnicos

- Separação clara entre serviços, modelos, API e configuração.
- Código preparado para ambientes locais, servidores e automações agendadas.
- Pronto para rodar com cron, Docker, n8n ou workers assíncronos.
- XPath robusto com suporte a XML com namespace.
- Boas práticas de segurança para credenciais.
- Modelo de banco documentado em `docs/database.sql`.

## Roadmap

- Controle de arquivos já processados.
- Persistência real com PostgreSQL ou SQL Server.
- Dashboard web de auditoria.
- Upload do XML normalizado para Google Drive.
- Logs persistentes por arquivo.
- Fila assíncrona com Celery/RabbitMQ.
- Docker Compose com API e banco.

## Autor

Desenvolvido por [Thiago Tavares](https://github.com/tavaresmirako).
