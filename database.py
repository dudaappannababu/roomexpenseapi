# reference links, https://fastapi.tiangolo.com/tutorial/sql-databases/, https://www.koyeb.com/docs/databases

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from sqlalchemy import Column, Integer, String, Float, Boolean

# SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
# might get error, some references,
#       1. https://stackoverflow.com/questions/62688256/sqlalchemy-exc-nosuchmoduleerror-cant-load-plugin-sqlalchemy-dialectspostgre
#       2. pip install psycopg2-binary , found in https://stackoverflow.com/questions/12906351/importerror-no-module-named-psycopg2

SQLALCHEMY_DATABASE_URL = "postgresql://koyeb-adm:sTZeDg9fzb6u@ep-dark-cake-a2osiv9p.eu-central-1.pg.koyeb.app/koyebdb"

class Database:
    def __init__(self):
        self.engine = create_engine(SQLALCHEMY_DATABASE_URL)
        self.SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)
        self.Base = declarative_base()
        class Transactions(self.Base):  # keyword = update_attributes
            __tablename__ = "transactions"
            id = Column(Integer, primary_key=True, index=True)
            date = Column(String)
            time = Column(String)
            amount = Column(Float)
            category = Column(String)
            description = Column(String)
            paid_by = Column(String)
            AB = Column(Float)
            GS = Column(Float)
            AJ = Column(Float)
            SJ = Column(Float)
            for_room = Column(Boolean)
        
        self.Transactions = Transactions
        
        self.Base.metadata.create_all(bind=self.engine)

    def create_sub_session(self):
        return self.SessionLocal()
    
    def get_transactions(self):
        session = self.create_sub_session()
        transactions = session.query(self.Transactions).all()
        session.close()
        return transactions
    
    def add_transaction(self, date, time, amount, category, description, paid_by, AB, GS, AJ, SJ, for_room): # keyword = update_attributes
        session = self.create_sub_session()
        transaction = self.Transactions(date=date, 
                                        time=time, 
                                        amount=amount, 
                                        category=category, 
                                        description=description,
                                        paid_by=paid_by,
                                        AB=AB,
                                        GS=GS,
                                        AJ=AJ,
                                        SJ=SJ,
                                        for_room=for_room)
        session.add(transaction)
        session.commit()
        session.close()

    def delete_transaction(self, id):
        session = self.create_sub_session()
        session.query(self.Transactions).filter(self.Transactions.id == id).delete()
        session.commit()
        session.close()
    
    def drop_table(self): # Dangerous function, use with caution (drops all tables and recreates them)
        confirmation = input("Are you sure you want to drop all tables and recreate them? (y/n): ")
        if confirmation.lower() == "y":
            self.Base.metadata.drop_all(bind=self.engine)
            self.Base.metadata.create_all(bind=self.engine)
            print("Tables dropped and recreated successfully.")
        else:
            print("Operation cancelled.")

    def get_transaction_by_id(self, id):
        session = self.create_sub_session()
        transaction = session.query(self.Transactions).filter(self.Transactions.id == id).first()
        session.close()
        return transaction
    
    def update_transaction(self, id, date, time, amount, category, description, paid_by, AB, GS, AJ, SJ, for_room): # keyword = update_attributes
        session = self.create_sub_session()
        session.query(self.Transactions).filter(self.Transactions.id == id).update({self.Transactions.date: date, 
                                                                                    self.Transactions.time: time, 
                                                                                    self.Transactions.amount: amount, 
                                                                                    self.Transactions.category: category,
                                                                                    self.Transactions.description: description,
                                                                                    self.Transactions.paid_by: paid_by,
                                                                                    self.Transactions.AB: AB,
                                                                                    self.Transactions.GS: GS,
                                                                                    self.Transactions.AJ: AJ,
                                                                                    self.Transactions.SJ: SJ,
                                                                                    self.Transactions.for_room: for_room})
        session.commit()
        session.close()


    

    
    


    
