import pymysql
from os import environ

#class Database:
#
# class DBHelper:
#
#     def __init__(self):
#         self.host = "127.0.0.1"
#         self.user = "root"
#         self.password = ""
#         self.db = "emp"
#
#     def __connect__(self):
#         try:
#             self.connnection = pymysql.connect(environ.get('DB_Host'), environ.get('DB_User'), environ.get('DB_Password'), environ.get('DB_Name'))
#             self.cursor = self.connnection.cursor(pymysql.cursors.DictCursor)
#
#         except Exception as e:
#             # TODO use WITH
#             self.connnection.close()
#
#     def __disconnect__(self):
#         self.connnection.close()
#
#     def fetch(self, sql):
#         self.__connect__()
#         self.cursor.execute(sql)
#         result = self.cursor.fetchall()
#         self.__disconnect__()
#         return result
#
#     def execute(self, sql):
#         self.__connect__()
#         self.cursor.execute(sql)
#         self.__disconnect__()


#
# class DBHelper:
#     def CconnectToDatabase(self):
#         try:
#
#             db = pymysql.connect(environ.get('DB_Host'), environ.get('DB_User'), environ.get('DB_Password'),
#                                  environ.get('DB_Name'))
#             return db
#         except:
#             db.close()
#
#     def insertDrinkToDB(self,drinkName):
#         try:
#             db = self.CconnectToDatabase()
#             cursor = db.cursor()
#             query = f"INSERT INTO drink (name) VALUES ('{drinkName}');"
#             cursor.execute(query)
#             db.commit()
#             db.close()
#             return True
#         except Exception as e:
#             print(e)
#             db.close()
#             return False


def connectToDatabase():
    try:

        # db = pymysql.connect(environ.get('DB_Host'), environ.get('DB_User'), environ.get('DB_Password'),
        #                         environ.get('DB_Name'))
        db = pymysql.connect("127.0.0.1","root", "password",
                              "christos")
        return db
    except Exception as e:
        print(e)
        db.close()

def insertDrinkToDB(drinkName):
    try:
        db = connectToDatabase()
        cursor = db.cursor()
        query = f"INSERT INTO drink (name) VALUES ('{drinkName}');"
        cursor.execute(query)
        db.commit()
        db.close()
        return True
    except Exception as e:
        print(e)
        db.close()
        return False


def getPersonFromDbByEmail(email):
    try:
        db = connectToDatabase()
        cursor = db.cursor(pymysql.cursors.DictCursor)
        query = f"SELECT * FROM person WHERE email='{email}'"
        cursor.execute(query)
        db.close()
        return cursor.fetchone()
    except Exception as e:
        print(e)
        db.close()
        return False

def insertPersonToDB(firstName, lastName, email):

    try:
        db = connectToDatabase()
        cursor = db.cursor()
        query = f"INSERT INTO person (first_name, last_name, email) VALUES ('{firstName}', '{lastName}', '{email}');"
        cursor.execute(query)
        db.commit()
        db.close()
        return True
    except Exception as e:
        print(e)
        db.close()
        return False

def getAllPreferencesOfAPerson(email):
    try:
        db = connectToDatabase()
        cursor = db.cursor(pymysql.cursors.DictCursor)
        query = f"SELECT * FROM preference WHERE person_id=(SELECT person_id FROM person WHERE email = '{email}')"
        cursor.execute(query)
        db.close()
        return cursor.fetchone()
    except Exception as e:
        print(e)
        db.close()
        return False

def getAllDataFromDbTable(tableName):
    try:
        db = connectToDatabase()
        cursor = db.cursor(pymysql.cursors.DictCursor)
        query = f"SELECT * FROM {tableName}"
        cursor.execute(query)
        db.close()
        result = cursor.fetchall()
        return result
    except Exception as e:
        print(e)
        db.close()
        return False

def getAllRoundItemsFromDB(creatorEmail):
    try:
        db = connectToDatabase()
        cursor = db.cursor(pymysql.cursors.DictCursor)
        query = f"  SELECT * FROM round_item WHERE round_id = (SELECT round_id FROM round WHERE status= 1 AND creator_id = (SELECT person_id FROM person WHERE email = '{creatorEmail}'))"
        cursor.execute(query)
        db.close()
        result = cursor.fetchall()
        return result
    except Exception as e:
        print(e)
        db.close()
        return False


def getAllRoundItemsWithRoundIdFromDB(roundId):
    try:
        db = connectToDatabase()
        cursor = db.cursor(pymysql.cursors.DictCursor)
        query = f"SELECT * FROM round_item WHERE round_id = '{roundId}'"
        cursor.execute(query)
        db.close()
        result = cursor.fetchall()
        return result
    except Exception as e:
        print(e)
        db.close()
        return False

def insertNewPreference(email,description,drinkName):
    try:
        db = connectToDatabase()
        cursor = db.cursor()
        query = f"INSERT INTO preference SET description = '{description}',person_id = (SELECT person_id FROM person WHERE email = '{email}'), drink_id = (SELECT drink_id FROM drink WHERE name = '{drinkName}');"
        cursor.execute(query)
        db.commit()
        db.close()
        return True

    except Exception as e:
        print(e)
        db.close()
        return False



def insertNewRound(personEmail):
    try:
        db = connectToDatabase()
        cursor = db.cursor()
        query = f"INSERT INTO round SET status = true,creator_id=(SELECT person_id FROM person WHERE email = '{personEmail}')"
        cursor.execute(query)
        db.commit()
        db.close()
        return True
    except Exception as e:
        print(e)
        db.close()
        return False



def insertNewRoundItem(creatorsEmail,personEmail,drinkName):
    try:
        db = connectToDatabase()
        cursor = db.cursor()
        query = f"INSERT INTO round_item SET round_id = (SELECT round_id FROM round WHERE creator_id = (SELECT person_id FROM person WHERE email ='{creatorsEmail}')),preference_id = (SELECT preference_id from preference WHERE person_id = (SELECT person_id FROM person WHERE email = '{personEmail}') AND drink_id =(SELECT drink_id FROM drink WHERE name ='{drinkName}'))"
        cursor.execute(query)
        db.commit()
        db.close()
        return True
    except Exception as e:
        print(e)
        db.close()
        return False

def insertNewRoundByIdsItem(roundid,preferenceid):
    try:
        db = connectToDatabase()
        cursor = db.cursor()
        query = f"INSERT INTO round_item SET round_id ='{roundid}',preference_id = {preferenceid}"
        cursor.execute(query)
        db.commit()
        db.close()
        return True
    except Exception as e:
        print(e)
        db.close()
        return False

def getPersonDetailsBasedOnPreferenceFromDB(preferenceID):
    try:
        db = connectToDatabase()
        cursor = db.cursor(pymysql.cursors.DictCursor)
        query = f" select first_name, last_name, email from person where person_id = (select person_id from preference where preference_id = '{preferenceID}')"
        cursor.execute(query)
        db.close()
        result = cursor.fetchone()
        return result
    except Exception as e:
        print(e)
        db.close()
        return False

def getDrinkDetailsBasedOnPreferenceFromDB(preferenceID):
    try:
        db = connectToDatabase()
        cursor = db.cursor(pymysql.cursors.DictCursor)
        query = f"select d.name, pref.description from christos.drink as d inner join christos.preference as pref on pref.drink_id = d.drink_id where pref.preference_id = '{preferenceID}'"
        cursor.execute(query)
        db.close()
        result = cursor.fetchone()
        return result
    except Exception as e:
        print(e)
        db.close()
        return False



def getAllPreferenceDataFromDB():
    try:
        db = connectToDatabase()
        cursor = db.cursor(pymysql.cursors.DictCursor)
        query = f"select p.first_name, p.last_name, p.email, d.name, pref.preference_id, pref.description from christos.preference as pref inner join christos.person as p on p.person_id = pref.person_id inner join christos.drink as d on d.drink_id = pref.drink_id;"
        cursor.execute(query)
        db.close()
        result = cursor.fetchall()
        return result
    except Exception as e:
        print(e)
        db.close()
        return False

def getPeopleWithoutAPreferenceFromDB():
    try:
        db = connectToDatabase()
        cursor = db.cursor(pymysql.cursors.DictCursor)
        query = f"select p.first_name, p.last_name, p.email from christos.person as p  WHERE NOT EXISTS (SELECT pref.person_id FROM christos.preference pref WHERE p.person_id = pref.person_id);"
        cursor.execute(query)
        db.close()
        result = cursor.fetchall()
        return result
    except Exception as e:
        print(e)
        db.close()
        return False

def getAllActiveRoundsFromDB():
    try:
        db = connectToDatabase()
        cursor = db.cursor(pymysql.cursors.DictCursor)
        query = f"select r.round_id, r.status, r.DateCreated, p.first_name, p.last_name, p.email from christos.round as r inner join christos.person as p on p.person_id = r.creator_id where r.status = 1"
        cursor.execute(query)
        db.close()
        result = cursor.fetchall()
        return result
    except Exception as e:
        print(e)
        db.close()
        return False

def updateRoundStatusInDB(roundId):
    try:
        db = connectToDatabase()
        cursor = db.cursor()
        query = f"UPDATE christos.round SET status = false where round_id = '{roundId}'"
        cursor.execute(query)
        db.commit()
        db.close()
        return True

    except Exception as e:
        print(e)
        db.close()
        return False

#print(getPersonDetailsBasedOnPreferenceFromDB(1))
#insertPersonToDB("John","James","J.J@infinityworks.com")
#print(getAllDataFromDbTable('person'))
   # Insert Person to database
   # Retrieve People
   #Insert Drink
   #Rretrieve Drinks
#db = pymysql.connect(environ.get('DB_Host'),environ.get('DB_User'), environ.get('DB_Password'),environ.get('DB_Name'))
#cursor = db.cursor()
# execute SQL query using execute() method.
#cursor.execute("SELECT VERSION()")
# Fetch a single row using fetchone() method.
#data = cursor.fetchone()
#print ("Database version : %s " % data)