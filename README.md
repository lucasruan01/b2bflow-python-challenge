# b2bflow Python Challenge

Projeto desenvolvido para o processo seletivo de Estágio em Desenvolvimento Python da b2bflow.

## Objetivo

Ler contatos cadastrados no Supabase e enviar mensagens personalizadas via WhatsApp utilizando a Z-API.

Formato da mensagem:

Olá, <nome_contato> tudo bem com você?

---

## Estrutura do projeto

```text
b2bflow/
│
├── .env.example
├── .gitignore
├── README.md
├── requirements.txt
├── main.py
│
├── services/
│   ├── supabase_service.py
│   └── zapi_service.py
│
└── utils/
    └── config.py
```

---

## Estrutura da tabela

Tabela: contacts

| Campo | Tipo |
| ----- | ---- |
| id    | int8 |
| name  | text |
| phone | text |

Exemplo:

| id | name  | phone         |
| -- | ----- | ------------- |
| 1  | Lucas | 5598999999999 |
| 2  | Maria | 5598888888888 |
| 3  | João  | 5598777777777 |

---

## Variáveis de ambiente

Criar um arquivo `.env` na raiz do projeto:

```env
SUPABASE_URL=your_supabase_url
SUPABASE_KEY=your_supabase_key

ZAPI_INSTANCE_ID=your_instance_id
ZAPI_TOKEN=your_zapi_token
```

---

## Instalação

Instalar as dependências:

```bash
pip install -r requirements.txt
```

---

## Execução

```bash
python main.py
```

---

## Fluxo

1. Busca até 3 contatos no Supabase.
2. Gera a mensagem personalizada para cada contato.
3. Envia a mensagem via Z-API.
4. Exibe logs de sucesso ou erro no terminal.

---

## Tecnologias utilizadas

* Python
* Supabase
* Z-API
* Requests
* python-dotenv
* Git
* GitHub
