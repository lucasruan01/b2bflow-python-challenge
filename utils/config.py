from dotenv import load_dotenv
import os

load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")   
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

if not SUPABASE_URL:
    raise ValueError(
        "SUPABASE_URL não encontrada no arquivo .env"
    )

if not SUPABASE_KEY:
    raise ValueError(
        "SUPABASE_KEY não encontrada no arquivo .env"
    )

ZAPI_INSTANCE_ID = os.getenv("ZAPI_INSTANCE_ID")
ZAPI_TOKEN = os.getenv("ZAPI_TOKEN")

if not ZAPI_INSTANCE_ID:
    raise ValueError(
        "ZAPI_INSTANCE_ID não encontrada")

if not ZAPI_TOKEN:
    raise ValueError(
        "ZAPI_TOKEN não encontrada")