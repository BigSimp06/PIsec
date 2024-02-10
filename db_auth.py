import mysql.connector
import getpass
import hashlib
import uuid
logged_in = False
server_auth = False

def usr_login():
  try:
   #attempting to communicate with the database
    mydb = mysql.connector.connect(
      host = "localhost",
      user = "root",
      password = "",
      database = "PIsec",
      table = "Usr"
    )
    mycursor = mydb.cursor()
    
    #takeing authorisation credentials from the user
    password = entry_pasw.get()
    password = hashlib.sha256(password).hexdigest()
    username = entry_usr.get()
    
    #retrieving informaiton from database
    mycursor.execute("SELECT password FROM Usr WHERE username = %s", (username))
    password_hash = mycursor.fetchall()
    
    #comparison to the true values
    if password_hash != password:
      print("Incorrect Password")
    else:
      Logged_in = True
      return Logged_in

  except Exception as error:
    print(f"An unexpected error has occcured {error}")

def srver_login():
    try:
        #attempting to connect to the database
        mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "",
        database = "PIsec",
        table = "srver_Auth"
        )

        #getting values from the users computer 
        mac_addr = hex(uuid.getnode())
        ip_addr = socket.gethostbyname(socket.gethostname())
        mycursor = mydb.cursor()
        mycursor.execute("SELECT user FROM srver_Auth WHERE mac_addr = %s",(mac_addr))
        mac_addr_db = mycursor.fetchall()

        #comparing to the values in the database
        if mac_addr != mac_addr_db:
            print("Device not authorised")
        else:
            server_auth = True
            return server_auth
    except Exception as error:
        print(f"an unexcpected error has occured: {error}")

