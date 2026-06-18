from services.supabase_service import get_contacts
from services.zapi_service import send_message

contacts = get_contacts()

for contact in contacts:

    message = f"Olá, {contact['name']} tudo bem com você?"

    response = send_message(
        contact["phone"],
        message
    )

    print(
        f"[INFO] Tentando enviar para "
        f"{contact['name']} ({contact['phone']})"
    )

    print(response)