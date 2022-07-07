
from sqlalchemy.orm import sessionmaker
from db_lesson import OurDataStructure, engine

Session = sessionmaker(bind=engine)
session = Session()

first = OurDataStructure("My_first_record", 20000)
session.add(first)
session.commit()

second = OurDataStructure("New_second", 55000)
session.add(second)
session.commit()

# arba 
# pr = session.query(OurDataStructure).all()
# print(pr)

pr = session.query(OurDataStructure).get(1)

pr.price = 500
session.commit()

print(pr)

# arba
# print(pr)
# session.delete(pr)

# pr_all = session.query(OurDataStructure).all()

# print(pr_all)

# CRUD dreate read update delete
