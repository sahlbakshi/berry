import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate('firestore.json')
app = firebase_admin.initialize_app(cred)
db = firestore.client()

##def createCollection(name, key):
##def addDocuments(records):
##for record in data:
##    doc_ref = db.collection("companies").document(record['Name'])
##    doc_ref.set(record)