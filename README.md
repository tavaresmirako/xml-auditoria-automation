# xml-auditoria-automation

## Automação em Python para Processamento de XMLs de Auditoria

Este repositório contém um projeto Python desenvolvido para automatizar o processo de auditoria de arquivos XML. A solução integra-se com o Google Drive para localizar e baixar documentos XML, extrai dados cruciais utilizando expressões XPath, permite a alteração ou normalização desses XMLs com `xml.etree.ElementTree`, converte os dados selecionados para o formato JSON e, finalmente, envia o payload resultante para uma API externa. Esta API é responsável por persistir os dados em um banco de dados e alimentar um frontend.

## Funcionalidades Principais

*   **Conectividade com Google Drive**: Autenticação e acesso seguro a arquivos XML armazenados no Google Drive.
*   **Localização e Download de XMLs**: Capacidade de listar e baixar arquivos XML de pastas específicas no Google Drive.
*   **Extração de Dados com XPath**: Utilização de expressões XPath para extrair informações específicas e relevantes dos documentos XML.
*   **Normalização e Transformação de XML**: Manipulação de estruturas XML usando `xml.etree.ElementTree` para normalizar ou alterar dados conforme a necessidade da auditoria.
*   **Geração de JSON**: Conversão dos dados extraídos e processados para o formato JSON, ideal para consumo por APIs e aplicações web.
*   **Integração com API Externa**: Envio dos dados JSON para um endpoint de API configurável, que se encarrega de salvar as informações no banco de dados e atualizar o frontend.

## Estrutura do Projeto

```
xml-auditoria-automation/
├── main.py
├── requirements.txt
└── README.md
```

*   `main.py`: Contém a lógica principal da automação, incluindo funções para autenticação no Google Drive, manipulação de XML, conversão para JSON e envio para a API.
*   `requirements.txt`: Lista as dependências Python necessárias para o projeto.
*   `README.md`: Este arquivo, fornecendo uma visão geral do projeto e instruções.

## Como Usar

### 1. Configuração do Ambiente

1.  **Clone o repositório**:
    ```bash
    git clone https://github.com/tavaresmirako/xml-auditoria-automation.git
    cd xml-auditoria-automation
    ```

2.  **Crie um ambiente virtual** (recomendado):
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Instale as dependências**:
    ```bash
    pip install -r requirements.txt
    ```

### 2. Configuração do Google Drive API

1.  Siga as instruções da documentação do Google para habilitar a Google Drive API e baixar suas `credentials.json`.
2.  Coloque o arquivo `credentials.json` na raiz do projeto.

### 3. Execução

1.  **Modifique `main.py`**: Atualize as variáveis `YOUR_GOOGLE_DRIVE_FOLDER_ID` e `http://your-api-endpoint.com/upload` com seus respectivos valores.
2.  **Execute o script**:
    ```bash
    python3 main.py
    ```

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests.

## Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes. (O arquivo LICENSE será adicionado posteriormente)
