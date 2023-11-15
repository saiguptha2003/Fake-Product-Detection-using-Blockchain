import pymysql

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

def createUserbyrole(email, password, role, remarks, address):
    try:
        db=get_db()
        cursor=db.cursor()
        if role == 'supplier':
            cursor.execute('INSERT INTO suppliers (email, remarks, password, address) VALUES (%s, %s, %s, %s)',
                    (email, remarks, password, address))
        elif role == 'distributor':
            cursor.execute('INSERT INTO distributors (email, remarks, password, address) VALUES (%s, %s, %s, %s)',
                    (email, remarks, password, address))
        elif role == 'wholesaler':
            cursor.execute('INSERT INTO wholesalers (email, remarks, password, address) VALUES (%s, %s, %s, %s)',
                           (email, remarks, password, address))
        elif role == 'retailer':
            cursor.execute('INSERT INTO retailers (email, remarks, password, address) VALUES (%s, %s, %s, %s)',
                           (email, remarks, password, address))
        elif role == 'customer':
            cursor.execute('INSERT INTO customer (email, remarks, password, address) VALUES (%s, %s, %s, %s)',
                           (email, remarks, password, address))
        else:
            return False 
        db.commit()
        db.close()
        return True
    except Exception as e:
        print(e)
        return False
    
def rolebased_login(email, password, role):
    try:
        db = get_db()
        cursor = db.cursor()

        table_name = None
        if role == 'supplier':
            table_name = 'suppliers'
        elif role == 'distributor':
            table_name = 'distributors'
        elif role == 'wholesaler':
            table_name = 'wholesalers'
        elif role == 'retailer':
            table_name = 'retailers'
        elif role == 'customer':
            table_name = 'customer'
        else:
            return False

        query = f"SELECT * FROM {table_name} WHERE email = %s AND password = %s"
        cursor.execute(query, (email, password))
        user = cursor.fetchone()

        db.close()

        if user:
            return True
        else:
            return False

    except Exception as e:
        print(e)
        return False, "An error occurred during login"

    