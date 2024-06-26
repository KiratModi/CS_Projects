# All responses are hypothetical and just assumptions. Please don't use this for diagnosis! LOL

# I know the program is long but if I wanna make it big its now easier then editing lots of conditionals
# Iknow theres improvement needed but TIME!!

#disease.txt file has symptoms which will be loaded. 
def load_symptoms_from_file(filename):
    try:
        with open(filename, 'r') as file:
            symptoms = [line.strip() for line in file.readlines()]
        return symptoms
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return []

# Final results as per y/n sequence
def diagnose_illness(responses):
    if responses == ['yes', 'yes', 'yes', 'yes']:
        return "severe cold"
    elif responses == ['yes', 'yes', 'no', 'no']:
        return "COVID-19"
    elif responses == ['yes', 'no', 'no', 'no']:
        return "light cold"
    elif responses == ['no', 'no', 'yes', 'no']:
        return "flight sickness"
    else:
        return None

# Threshold is values if exceeded then appointment is must
def ask_symptoms(symptoms, threshold):
    responses = []
    positive_symptoms = []
    
    print("Please respond with 'yes' or 'no' to the following symptoms:")
    for symptom in symptoms:
        while True:
            response = input(f"Do you have {symptom}? (yes/no): ").strip().lower()
            if response in ('yes', 'no'):
                responses.append(response)
                if response == 'yes':
                    positive_symptoms.append(symptom)
                break
            else:
                print("Invalid response. Please answer with 'yes' or 'no'.")
    
    diagnosis = diagnose_illness(responses)
    if diagnosis:
        print(f"Based on your responses, you might have {diagnosis}.")
    elif responses.count('yes') >= threshold:
        print("You should come in for an appointment for further testing.")
        print("You reported the following symptoms:", ", ".join(positive_symptoms))
    else:
        print("You do not need to come in for further testing at this time.")

def add_symptoms(symptoms):
    while True:
        additional_symptom = input("Enter an additional symptom to add (or 'done' to finish): ").strip()
        if additional_symptom.lower() == 'done':
            break
        symptoms.append(additional_symptom)

def main():
    filename = 'diseases.txt'
    symptoms_list = load_symptoms_from_file(filename)
    
    if not symptoms_list:
        print("No symptoms loaded. Exiting the program.")
        return

    threshold_symptoms = 4
    
    while True:
        print("\nSymptom Checker Menu")
        print("1. Check symptoms")
        print("2. Add more symptoms")
        print("3. Exit")
        choice = input("Enter your choice: ").strip()
        
        if choice == '1':
            ask_symptoms(symptoms_list, threshold_symptoms)
        elif choice == '2':
            add_symptoms(symptoms_list)
        elif choice == '3':
            print("Exiting the program. Stay healthy!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

