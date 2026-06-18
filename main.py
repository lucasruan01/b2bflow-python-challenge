from services.supabase_service import get_contacts

contacts = get_contacts()

for contact in contacts:
    message = (
        f"Olá, {contact['name']} tudo bem com você?"
    )

    print(message)