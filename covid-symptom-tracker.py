numSymptoms = 0;
y = "yes";
n = "no";

questionArray = [
    "1. Do you have a FEVER? \n y or n: ",
    "2. Do you have a DRY COUGH? \n y or n: ",
    "3. Do you feel MORE TIRED THAN USUAL? \n y or n: ",
    "4. Do you have a ACHES AND PAIN? \n y or n: ",
    "5. Do you have a SORE THROAT? \n y or n: ",
    "6. Do you have a DIAHRREA? \n y or n: "
    "7. Do you have a PINK EYE (CONJECTIVITIS)? \n y or n: ",
    "8. Do you have a HEADACHE? \n y or n: ",
    "9. Do you have a LOSS OF TASTE OR SMELL? \n y or n: ",
    "10. Do you have a RASH on the skin, or DISCOLORATION of FINGERS AND TOES? \n y or n: ",
    "11. Are you experiencing DIFFICULTY  BREATHING or SHORTNESS OF BREATH? \n y or n: ",
    "12. Are you experiencing CHEST PAIN or PRESSURE? \n y or n: ",
    "13. Are you experiencing LOSS OF SPEECH or MOVEMENT? \n y or n: "
]

def countSymptoms(answer):
    if answer == y:
        global numSymptoms
        numSymptoms += 1

def main ():

    for i in questionArray:
        answer = input(i);
        countSymptoms(answer)

    print("You have " + str(numSymptoms) + " out of 13 COVID-19 symptoms.");

main()