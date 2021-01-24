numSymptoms = 0;
y = "yes";
n = "no";

def countSymptoms(answer):
    if answer == y:
        global numSymptoms
        numSymptoms += 1

def main ():
    # common symptoms
    
    # fever
    answer = input("1. Do you have a FEVER? \n y or n: ");
    countSymptoms(answer)
    print("Answer: " + answer);
    print(numSymptoms);

    # dry cough
    answer = input("2. Do you have a DRY COUGH? \n y or n: ");
    countSymptoms(answer)

    #tiredness
    answer = input("3. Do you feel MORE TIRED THAN USUAL? \n y or n: ");
    countSymptoms(answer)

    #Less common symptoms:

    # aches and pains
    answer = input("4. Do you have a ACHES AND PAIN? \n y or n: ");
    countSymptoms(answer)

    # sore throat    
    answer = input("5. Do you have a SORE THROAT? \n y or n: ");
    countSymptoms(answer)

    # diarrhoea
    answer = input("6. Do you have a DIAHRREA? \n y or n: ");
    countSymptoms(answer)

    # pink eye (conjunctivitis)
    answer = input("7. Do you have a PINK EYE (CONJECTIVITIS)? \n y or n: ");
    countSymptoms(answer)

    # headache
    answer = input("8. Do you have a HEADACHE? \n y or n: ");
    countSymptoms(answer)

    # loss of taste or smell
    answer = input("9. Do you have a LOSS OF TASTE OR SMELL? \n y or n: ");
    countSymptoms(answer)

    # a rash on skin, or discolouration of fingers or toes
    answer = input("10. Do you have a RASH on the skin, or DISCOLORATION of FINGERS AND TOES? \n y or n: ");
    countSymptoms(answer)

    # Serious symptoms:

    # difficulty breathing or shortness of breath.
    answer = input("11. Are you experiencing DIFFICULTY  BREATHING or SHORTNESS OF BREATH? \n y or n: ");
    countSymptoms(answer)

    # chest pain or pressure
    answer = input("12. Are you experiencing CHEST PAIN or PRESSURE? \n y or n: ");
    countSymptoms(answer)

    # loss of speech or movement
    answer = input("13. Are you experiencing LOSS OF SPEECH or MOVEMENT? \n y or n: ");
    countSymptoms(answer)

    print("You have " + str(numSymptoms) + " out of 13 COVID-19 symptoms.");

main()