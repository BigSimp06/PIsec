import mysql.connector
import hashlib
import getpass
import uuid
import socket

# hashes and converts hash into hexadecimal
def hash_password(password):
    password = hashlib.sha256(password.encode()).hexdigest()
    return password

def create_Usr():
  try:
  
    #connecting to the database
    mydb = mysql.connector.connect(
      host = "localhost",
      user = "root",
      password = "",
      database = "PIsec",
      table = "Usr"
      )
    mycursor = mydb.cursor()

    #Retrieving information from the user 
    username = entry_usr.get()
    password = entry_pasw.get()
    email = entry_email.get()

    #Sending that data to the database to be stored 
    sqlformula= "INSERT INTO Usr (username, password, email) VAlUES (%s, %s, %s)"
    usr = (username, hash_password(password), email)
    mysql.execute(sqlformula, usr)
    mydb.commit()
  except Exception as error:
    print(f"An unexpected error has occcured {error}")                                   

def create_authprof():
    try:
        # connecting to the database
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="PIsec"
        )
        mycursor = mydb.cursor()

        # retrieving IP and MAC addresses
        mac_addr = hex(uuid.getnode())
        ip_addr = socket.gethostbyname(socket.gethostname())

        # building the SQL query
        sqlformula = "INSERT INTO srver_Auth(mac_addr, ip_addr) VALUES (%s, %s)"
        authprof = (mac_addr, ip_addr)

        # committing the data to the database
        mycursor.execute(sqlformula, authprof)
        mydb.commit()
        print("Authentication profile created successfully!")
    except Exception as error:
        print(f"An unexpected error has occurred: {error}")

# Example Usage
create_Usr()
create_authprof()
