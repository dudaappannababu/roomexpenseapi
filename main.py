from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

from database import Database

app = FastAPI()
db = Database()

origins = ["http://localhost:3000", "http://127.0.0.1:3000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/alltransactions")
def read_transactions():
    return db.get_transactions()

@app.post("/addtransaction")
def add_transaction(date: str, time: str, amount: float, category: str, description: str, paid_by: str, AB: float, GS: float, AJ: float, SJ: float, for_room: bool):
    db.add_transaction(date, time, amount, category, description, paid_by, AB, GS, AJ, SJ, for_room)
    return {"status": "success"}

class Transaction(BaseModel):
    date: str
    time: str
    amount: float
    category: str
    description: str
    paid_by: str
    AB: float
    GS: float
    AJ: float
    SJ: float
    for_room: bool

@app.post("/addtransactions")
def add_transactions(transactions: list[Transaction]):
    print(transactions)
    for transaction in transactions:
        db.add_transaction(date=transaction.date,
                            time=transaction.time,
                            amount=transaction.amount,
                            category=transaction.category,
                            description=transaction.description,
                            paid_by=transaction.paid_by,
                            AB=transaction.AB,
                            GS=transaction.GS,
                            AJ=transaction.AJ,
                            SJ=transaction.SJ,
                            for_room=transaction.for_room)
    return {"status": "success"}

@app.delete("/deletetransaction")
def delete_transaction(id: int):
    db.delete_transaction(id)
    return {"status": "success"}

@app.get("/transaction/{id}")
def read_transaction(id: int):
    return db.get_transaction_by_id(id)

@app.put("/updatetransaction")
def update_transaction(id: int, date: str, time: str, amount: float, category: str, description: str, paid_by: str, AB: float, GS: float, AJ: float, SJ: float, for_room: bool):
    db.update_transaction(id, date, time, amount, category, description, paid_by, AB, GS, AJ, SJ, for_room)
    return {"status": "success"}