import pymysql
from web3 import Web3

def get_db():
    db = pymysql.connect(
        host="localhost",
        user="root",
        password="Pandusai@2003",
        database="cpd"
    )
    return db

def createuser(email, password, rol):
    db = get_db()
    cursor = db.cursor()
    cursor.execute("INSERT INTO users (email, pass, roleofuser) VALUES (%s, %s, %s)", (email, password, rol))
    db.commit()
    db.close()
    if cursor.rowcount > 0:
        return True
    else:
        return False


def checkuser(email, password, rol):
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM users WHERE email = %s AND pass = %s AND roleofuser = %s", (email, password, rol))
    result = cursor.fetchone()
    db.close()
    print(result)
    if result!=None:
        return True
    else:
        return False

def addproduct(name, id, role, status, source, destination, remarks):
    db = get_db()
    cursor = db.cursor()
    insert_query = "INSERT INTO product (product_name, product_id, rrole, _status, source, destination, remarks) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    values = (name, id, role, status, source, destination, remarks)
    cursor.execute(insert_query, values)
    db.commit()
    db.close()
    if cursor.rowcount > 0:
        return True
    else:
        return False
    


get_db()