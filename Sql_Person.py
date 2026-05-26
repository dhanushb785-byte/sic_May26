import pymysql
 
def connect_db():

    connection =pymysql.connect( user  = 'root' , password = 'root' , port =3306 , database= 'world' , charset = "utf8",  host= 'localhost', 
    )
    return connection 

def disconnect_db(connection):
    print('DB disconnected')
    connection.close()
    
def create_person_demo():
    query = ' insert into people(name ,gender , location , age) values( %s , %s ,%s ,%s ); '
    person = read_person()
    connection = connect_db()
    cursor = connection.cursor()
    count = cursor.execute(query , person)
    if count == 1:
        print('Person created ')
    else:
        print('person creation failed ')
    connection .commit()
    cursor.close()
    disconnect_db(connection)
        

def read_person():
    name = input(" Enter the person name")
    age = input(" Enter the person's age")
    gender = input(" Enter the person's gender m/f")
    location = input(" Enter the person's location")
    if gender.lower() == 'f':
        gender = True
    else:
        gender = False
    return (name , gender , location , age)



def serach_person():
    pass

def update_person():
    pass

def delete_person():
    pass

def list_people():
    pass

create_person_demo()

