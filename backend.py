
import os
from supabase import create_client, Client

url = "your_supabase_url_here"
key = "your_supabase_api_key_here"
supabase: Client = create_client(url, key)

def check():
    # Placeholder for fetching user data
    response = supabase.table("Record").select("*").execute()
    return response.data

def sign_up(user_id, name, email, password):
    # Placeholder for signing up user
    response = supabase.table("Record").insert({"id": user_id, "Name": name, "email": email, "Password": password}).execute()
    return response

def get_user_by_email(email):
    # Placeholder for fetching user by email
    response = supabase.table("Record").select("*").eq("email", email).execute()
    return response.data
