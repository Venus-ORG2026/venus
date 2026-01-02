import firebase_admin
from firebase_admin import credentials, auth, firestore

cred = credentials.Certificate("firebase-service-account.json")

firebase_admin.initialize_app(cred)

db = firestore.client()

def verify_token(id_token: str):
    decoded = auth.verify_id_token(id_token)
    return decoded
