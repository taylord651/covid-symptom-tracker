numSymptoms = 0;
question = 1;

questionArray = [
    # Common Symptoms:y
    "1. Do you have a FEVER? \n y or n: ",
    "2. Do you have a DRY COUGH? \n y or n: ",
    "3. Do you feel MORE TIRED THAN USUAL? \n y or n: ",

    # Less common symptoms:
    "4. Do you have a ACHES AND PAIN? \n y or n: ",
    "5. Do you have a SORE THROAT? \n y or n: ",
    "6. Do you have a DIAHRREA? \n y or n: ",
    "7. Do you have a PINK EYE (CONJECTIVITIS)? \n y or n: ",
    "8. Do you have a HEADACHE? \n y or n: ",
    "9. Do you have a LOSS OF TASTE OR SMELL? \n y or n: ",
    "10. Do you have a RASH on the skin, or DISCOLORATION of FINGERS AND TOES? \n y or n: ",

    # Serious symptoms:
    "11. Are you experiencing DIFFICULTY  BREATHING or SHORTNESS OF BREATH? \n y or n: ",
    "12. Are you experiencing CHEST PAIN or PRESSURE? \n y or n: ",
    "13. Are you experiencing LOSS OF SPEECH or MOVEMENT? \n y or n: "
]

responseArray = []

def countSymptoms(answer):
    global question
    if answer == "y":
        global numSymptoms
        numSymptoms += 1
    responseArray.append("Question " + str(question) + ": " + answer)
    question += 1;

def validateResponse(response, question):
    if response.lower() not in ('y', 'n'):
        print("Response: " + response)
        print("Your response was invalid. Please enter 'y' for YES or 'n' for NO.")
        repeatQuestion(question);
    else:
        print("Response: " + response)
        print("Valid \n");
        countSymptoms(response)

def repeatQuestion(question):
    answer = raw_input(question);
    validateResponse(answer, question);

def getResponse():
    for question in questionArray:
        answer = raw_input(question);
        validateResponse(answer, question)

def main ():
    print("\n***COVID-19 Symptom Tracker***");
    print("Welcome, use this app to track the COVID-19 symptoms \n")
    print("Please enter 'y' for YES or 'n' for NO. \n")

    getResponse();

    print("You have " + str(numSymptoms) + " out of 13 COVID-19 symptoms.");
    print("Responses: ");
    print(responseArray);

main()