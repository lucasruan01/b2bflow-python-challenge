from supabase import create_client
from utils.config import SUPABASE_URL, SUPABASE_KEY

supabase = create_client(
    SUPABASE_URL,
    SUPABASE_KEY
)

def get_contacts():
    response = (
        supabase
        .table("contacts")
        .select("*")
        .limit(3)
        .execute()
    )

    return response.data