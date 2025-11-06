from supabase import create_client, Client
import os
from dotenv import load_dotenv

load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_SERVICE_ROLE_KEY")

class SupabaseClient:
    def __init__(self):
        self.client: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

    # -----------------------
    # INSERT
    # -----------------------
    def insert(self, table:str, data: dict):
        try:
            response = self.client.table(table).insert(data).execute()
            return response.data
        except Exception as e:
            print(f"[ERROR] Insert into {table} failed: {e}")
            return None
    
    # -----------------------
    # SELECT
    # -----------------------
    def select(self, table: str, filters: dict = None):
        try:
            query = self.client.table(table).select("*")
            if filters:
                for key, value in filters.items():
                    query = query.eq(key, value)
            response = query.execute()
            return response.data
        except Exception as e:
            print(f"[ERROR] Select from {table} failed: {e}")
            return None
    
    # -----------------------
    # UPDATE
    # -----------------------
    def update(self, table: str, data: dict, filters: dict):
        try:
            query = self.client.table(table)
            for key, value in filters.items():
                query = query.eq(key, value)
            response = query.update(data).execute()
            return response.data
        except Exception as e:
            print(f"[ERROR] Update {table} failed: {e}")
            return None

    # -----------------------
    # DELETE
    # -----------------------
    def delete(self, table: str, filters: dict):
        try:
            query = self.client.table(table)
            for key, value in filters.items():
                query = query.eq(key, value)
            response = query.delete().execute()
            return response.data
        except Exception as e:
            print(f"[ERROR] Delete from {table} failed: {e}")
            return None