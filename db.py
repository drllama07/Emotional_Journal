from sqlalchemy import create_engine, Column , String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import literal


Base= declarative_base()

class daily_emotions(Base):
    __tablename__ = "days"
    
    unq_id = Column("id", Integer, primary_key=True )
    date = Column("date", String)
    emotion1 = Column("emotion1", String)
    emotion2 = Column("emotion2", String)
    emotion3 = Column("emotion3", String)
    emotion4 = Column("emotion4", String)
    emotion5 = Column("emotion5", String)
    emotion6 = Column("emotion6", String)
    emotion7 = Column("emotion7", String)
    emotion8 = Column("emotion8", String)
    emotion9 = Column("emotion9", String)
    emotion10 = Column("emotion10", String)
    emotion11= Column("emotion11", String)
    emotion12= Column("emotion12", String)
    

    def __init__(self,unq_id, date, emotion1, emotion2,emotion3,emotion4,emotion5,emotion6,emotion7,emotion8,emotion9,emotion10,emotion11,emotion12) :
        self.unq_id = unq_id
        self.date = date
        self.emotion1 = emotion1
        self.emotion2 = emotion2
        self.emotion3 = emotion3
        self.emotion4 = emotion4
        self.emotion5 = emotion5
        self.emotion6 = emotion6
        self.emotion7 = emotion7
        self.emotion8 = emotion8
        self.emotion9 = emotion9
        self.emotion10 = emotion10
        self.emotion11 = emotion11
        self.emotion12= emotion12
        

    def __repr__(self) :
        return self.unq_id,self.date , self.emotion1,self.emotion2,self.emotion3,self.emotion4,self.emotion5,self.emotion6,self.emotion7,self.emotion8,self.emotion9,self.emotion10,self.emotion11,self.emotion12
        


engine = create_engine("sqlite:///mydb.db", echo= True)

Base.metadata.create_all(bind = engine)

Session = sessionmaker(bind = engine)
session = Session()



def ints_to_string(int_list,intx):
    # Convert list of integers to a string
    a = ','.join(map(str, int_list))
    return a + ',' + str(intx)

def string_to_ints(string):
    # Convert string back to list of integers
    a =  list(map(int, string.split(',')))
    b = a[-1]
    a.pop(-1)

    return a , b


