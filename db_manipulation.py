import mysql.connector

def create_Db():
    try:
        # Connecting to the MySQL server with necessary parameters
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password=""
        )

        # Querying the database
        mycursor = mydb.cursor()
        mycursor.execute("SHOW DATABASES")
        databases = mycursor.fetchall()

        # Checking that the database doesn't already exist
        if ("PIsec",) not in databases:
            mycursor.execute("CREATE DATABASE PIsec")
            print("Database created")
        else:
            print("Database already exists")

    except Exception as error:
        print(f"An unexpected error has occurred: {error}")

def create_Tb_Usr():
    try:
        # Connecting to the MySQL server and editing the PIsec database
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="PIsec"
        )
        mycursor = mydb.cursor()
        mycursor.execute("SHOW TABLES")
        tables = mycursor.fetchall()

        if ("Usr",) not in tables:
            # Creating the rows of the table, stating the datatype and any connections
            mycursor.execute(
                "CREATE TABLE Usr(id INT AUTO_INCREMENT PRIMARY KEY, username NVARCHAR(255), password NVARCHAR(255), clientID INT AUTO_INCREMENT, FOREIGN KEY (clientID) REFERENCES srver_Auth(clientID) ON UPDATE CASCADE ON DELETE CASCADE, email NVARCHAR(255))"
            )
            print("Table created")
        else:
            print("Table already exists")

    except Exception as error:
        print(f"An unexpected error has occurred: {error}")

def create_Tb_srver_Auth():
    try:
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="PIsec"
        )
        mycursor = mydb.cursor()
        mycursor.execute("SHOW TABLES")
        tables = mycursor.fetchall()

        if ("srver_Auth",) not in tables:
            mycursor.execute(
                "CREATE TABLE srver_Auth(clientID INT AUTO_INCREMENT PRIMARY KEY, ip_address NVARCHAR(255), MAC_adr NVARCHAR(255))"
            )
            print("Table created")
        else:
            print("Table already exists")

    except Exception as error:
        print(f"An unexpected error has occurred: {error}")

def create_Tb_usr_photos():
    try:
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="PIsec"
        )
        mycursor = mydb.cursor()
        mycursor.execute("SHOW TABLES")
        tables = mycursor.fetchall()

        if ("usr_photos",) not in tables:
            mycursor.execute(
                "CREATE TABLE usr_photos(photo_id INT AUTO_INCREMENT PRIMARY KEY, date NVARCHAR(255), info LONGTEXT, path_to_photo NVARCHAR(255))"
            )
            print("Table created")
        else:
            print("Table already exists")

    except Exception as error:
        print(f"An unexpected error has occurred: {error}")

# Call the functions
create_Db()
create_Tb_Usr()
create_Tb_srver_Auth()
create_Tb_usr_photos()
