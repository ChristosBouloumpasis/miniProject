from connect_to_db import *
import json
from flask import Flask, jsonify, request, render_template
app = Flask(__name__)

#################################################
#              Website CODE
#################################################


@app.route('/drinks', methods=['GET', 'POST'])
def drinks():
    incomingRequest = request.method

    if(incomingRequest == "GET"):
        dbDrinks = getAllDataFromDbTable("drink")
        drinks = []
        for drink in dbDrinks:
            drinks.append(drink["name"])
        return render_template("add_drinks.html", title="Drinks",currentDrinks=drinks)
    elif(incomingRequest == "POST"):
        postBody = request.form['drink-name']
        if postBody is not None or "":
            insertDrinkToDB(postBody)
            dbDrinks = getAllDataFromDbTable("drink")
            drinks = []
            for drink in dbDrinks:
                drinks.append(drink["name"])
            responseMessage = "The new drink have been saved successfully. You can add another one if you would like!"
        return render_template("add_drinks.html", title="Drinks", responseMessage=responseMessage,currentDrinks=drinks)


@app.route('/people', methods=['GET', 'POST'])
def people():
    incomingRequest = request.method
    if (incomingRequest == "GET"):
         dbPeople = getAllDataFromDbTable("person")
         people = []
         for person in dbPeople:
             people.append(person)
         return render_template("add_people.html", title="People", currentPeople=people)
    elif (incomingRequest == "POST"):
         firstName = request.form['person-firstname']
         lastName = request.form['person-lastname']
         email = request.form['person-email']

         if firstName and lastName and email is not None or "":
            insertPersonToDB(firstName, lastName, email)
            dbPeople = getAllDataFromDbTable("person")
            people = []
            for person in dbPeople:
                people.append(person)
            responseMessage = "The new person have been saved successfully. You can add another one if you would like!"
            return render_template("add_people.html",title="People", currentPeople=people,responseMessage=responseMessage)

@app.route('/preferences', methods=['GET','POST'])
def preference():
    incomingRequest = request.method
    if (incomingRequest == "GET"):
        preferences = getAllPreferenceDataFromDB()
        people= getAllDataFromDbTable("person")
        drinks= getAllDataFromDbTable("drink")
        peopleWithoutPreference = getPeopleWithoutAPreferenceFromDB()
        return render_template("add_preference.html", title="Preference", currentPreferences=preferences, people=people,drinks=drinks)
    elif (incomingRequest == "POST"):
        person_email= request.form.get("new_person")
        drink_name = request.form.get("new_drink")
        description = request.form.get("description")
        insertNewPreference(person_email, description, drink_name)
        preferences = getAllPreferenceDataFromDB()
        people = getAllDataFromDbTable("person")
        drinks = getAllDataFromDbTable("drink")
        peopleWithoutPreference = getPeopleWithoutAPreferenceFromDB()
        responseMessage = "The new preference have been saved successfully. You can add another one if you would like!"
        return render_template("add_preference.html", title="Preference", currentPreferences=preferences, people=people,drinks=drinks,responseMessage=responseMessage)

@app.route('/rounds', methods=['GET','POST'])
def rounds():
    incomingRequest = request.method
    if (incomingRequest == "GET"):
        activeRoundsDB = getAllActiveRoundsFromDB()
        people = getAllDataFromDbTable("person")
        return render_template("add_round.html", title="Rounds", activeRounds=activeRoundsDB,people=people)
    elif (incomingRequest == "POST"):
        creator_email= request.form.get("creator")
        insertNewRound(creator_email)
        activeRoundsDB = getAllActiveRoundsFromDB()
        people = getAllDataFromDbTable("person")
        responseMessage = "The new round have been saved successfully. You can add another one if you would like!"
        return render_template("add_round.html", title="Rounds",responseMessage=responseMessage,activeRounds=activeRoundsDB,people=people)

@app.route("/round", methods=['GET','POST'])
def round():
    incomingRequest = request.method
    if (incomingRequest == "GET"):
        round_id = request.args["round_id"]
        creator_email = request.args["creator_email"]
        creator_details = getPersonFromDbByEmail(creator_email)
        rawRoundData = getAllRoundItemsWithRoundIdFromDB(round_id)
        roundItem = []
        preferences = getAllPreferenceDataFromDB()
        for round_item in rawRoundData:
            personDetails = getPersonDetailsBasedOnPreferenceFromDB(round_item["preference_id"])
            drinkDetails = getDrinkDetailsBasedOnPreferenceFromDB(round_item["preference_id"])
            fullName = f"{personDetails['first_name']} {personDetails['last_name']}"
            roundItem.append({
                "person_email": personDetails["email"],
                "person_name": fullName,
                "drink_name": drinkDetails["name"],
                "description": drinkDetails["description"]
            })

        return render_template("round_details.html", title="Round",round_id=round_id,creator_details=creator_details,round_items=roundItem,preferences=preferences)
    elif (incomingRequest == "POST"):
        preferences= request.form.get("preferences").split(",")
        insertNewRoundByIdsItem(preferences[0], preferences[1])
        round_id = request.args["round_id"]
        creator_email = request.args["creator_email"]
        creator_details = getPersonFromDbByEmail(creator_email)
        rawRoundData = getAllRoundItemsWithRoundIdFromDB(round_id)
        roundItem = []
        preferences = getAllPreferenceDataFromDB()
        for round_item in rawRoundData:
            personDetails = getPersonDetailsBasedOnPreferenceFromDB(round_item["preference_id"])
            drinkDetails = getDrinkDetailsBasedOnPreferenceFromDB(round_item["preference_id"])
            fullName = f"{personDetails['first_name']} {personDetails['last_name']}"
            roundItem.append({
                "person_email": personDetails["email"],
                "person_name": fullName,
                "drink_name": drinkDetails["name"],
                "description": drinkDetails["description"]
            })

        responseMessage = "The new round have been saved successfully. You can add another one if you would like!"
        return render_template("round_details.html", title="Round",responseMessage=responseMessage,round_id=round_id,creator_details=creator_details,round_items=roundItem,preferences=preferences)


@app.route("/print", methods=['GET'])
def print():
    incomingRequest = request.method
    if (incomingRequest == "GET"):
        round_id = request.args["round_id"]
        updateRoundStatusInDB(round_id)
        rawRoundData = getAllRoundItemsWithRoundIdFromDB(round_id)
        roundItem = []
        for round_item in rawRoundData:
            personDetails = getPersonDetailsBasedOnPreferenceFromDB(round_item["preference_id"])
            drinkDetails = getDrinkDetailsBasedOnPreferenceFromDB(round_item["preference_id"])
            fullName = f"{personDetails['first_name']} {personDetails['last_name']}"
            roundItem.append({
                "person_email": personDetails["email"],
                "person_name": fullName,
                "drink_name": drinkDetails["name"],
                "description": drinkDetails["description"]
            })
        return render_template("print_round.html", title="Round",round_items=roundItem)



#################################################
#              API CODE
#################################################
@app.route('/helloworld')
def hello_world():
    return "hello World"

@app.route('/getpeople', methods=['GET'])
def get_people():
    people = getAllDataFromDbTable("person")
    return jsonify(people)
    # return jsonify(person.to_json() for person in people])

@app.route('/createpeople',methods=['POST'])
def input_new_person():
    for person in request.json:
        insertPersonToDB(person["first_name"], person["last_name"], person["email"])
    return "Received"
    #request.form.get('language')

@app.route('/getdrinks', methods=['GET'])
def get_drinks():
    drinks = getAllDataFromDbTable("drink")
    return jsonify(drinks)

@app.route('/createdrinks',methods=['POST'])
def input_new_drink():
    for drink in request.json:
        insertDrinkToDB(drink["name"])
    return "Received"


@app.route('/createpreference',methods=['POST'])
def input_new_preference():
    for preference in request.json:
        insertNewPreference(preference["person_email"],preference["description"],preference["drink_name"])
    return "Received"


@app.route('/personpreferences', methods=['GET'])
def get_person_preferences():
    preferences = getAllPreferencesOfAPerson(request.args["person_email"])
    return jsonify(preferences)


@app.route('/createround',methods=['POST'])
def input_new_round():
    for person in request.json:
        insertNewRound(person["person_email"])
    return "Received"

@app.route('/addrounditem',methods=['POST'])
def input_new_round_item():
    for round_item in request.json:
        insertNewRoundItem(round_item["creators_email"], round_item["person_email"], round_item["drink_name"])
    return "Received"

@app.route('/getround', methods=['GET'])
def get_round_items():
    creators_email = request.args["creators_email"]
    rawRoundData = getAllRoundItemsFromDB(creators_email)
    roundItem = []
    for round_item in rawRoundData:
        personDetails = getPersonDetailsBasedOnPreferenceFromDB(round_item["preference_id"])
        drinkDetails = getDrinkDetailsBasedOnPreferenceFromDB(round_item["preference_id"])
        fullName = f"{personDetails['first_name']} {personDetails['last_name']}"
        roundItem.append({
            "person_email" : personDetails["email"],
            "person_name" : fullName,
            "drink_name" : drinkDetails["name"]
        })

    return jsonify(roundItem)

if __name__ == "__main__":
    app.run(host='localhost', port=8088, debug=True )



