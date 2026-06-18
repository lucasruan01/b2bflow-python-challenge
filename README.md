# b2bflow Python Challenge

Projeto desenvolvido para o processo seletivo de Estágio em Desenvolvimento Python da b2bflow.

## Objetivo

Ler contatos do Supabase e enviar mensagens personalizadas via WhatsApp utilizando a Z-API.

Mensagem enviada:

```text
Olá, <nome_contato> tudo bem com você?
```

## Estrutura da tabela (Supabase)

Tabela: `contacts`

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

## Variáveis de ambiente

Crie um arquivo `.env` na raiz do projeto:

```env
SUPABASE_URL=your_supabase_url
SUPABASE_KEY=your_supabase_key

ZAPI_INSTANCE_ID=your_instance_id
ZAPI_TOKEN=your_zapi_token
```

## Instalação

Instale as dependências:

```bash
pip install -r requirements.txt
```

## Executar

```bash
python main.py
```

## Tecnologias utilizadas

* Python
* Supabase
* Z-API
* python-dotenv
