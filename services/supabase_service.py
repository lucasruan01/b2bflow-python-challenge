from supabase import create_client
from utils.config import SUPABASE_URL, SUPABASE_KEY

supabase = create_client(
    SUPABASE_URL,
    SUPABASE_KEY
)

def get_contacts():

    try:

        response = (
            supabase
            .table("contacts")
            .select("*")
            .limit(3)
            .execute()
        )

        return response.data

    except Exception as e:

        print(
            f"Erro ao consultar Supabase: {e}"
        )

        return []