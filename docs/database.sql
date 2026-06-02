CREATE TABLE auditoria_xml (
    id SERIAL PRIMARY KEY,
    arquivo VARCHAR(255),
    origem VARCHAR(100),
    tipo_documento VARCHAR(100),
    status VARCHAR(50),
    chave_acesso VARCHAR(100) UNIQUE,
    numero_nota VARCHAR(50),
    serie VARCHAR(20),
    data_emissao VARCHAR(80),
    cnpj_emitente VARCHAR(20),
    nome_emitente VARCHAR(255),
    cnpj_destinatario VARCHAR(20),
    cpf_destinatario VARCHAR(20),
    nome_destinatario VARCHAR(255),
    valor_total NUMERIC(15,2),
    payload_json JSONB,
    criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE auditoria_xml_produtos (
    id SERIAL PRIMARY KEY,
    auditoria_xml_id INTEGER REFERENCES auditoria_xml(id),
    numero_item VARCHAR(20),
    codigo VARCHAR(100),
    descricao TEXT,
    ncm VARCHAR(20),
    cfop VARCHAR(20),
    quantidade NUMERIC(15,4),
    valor_unitario NUMERIC(15,4),
    valor_total NUMERIC(15,2)
);
