#A Python-based application that generates prescriptions using patient and medication details, utilizing basic programming concepts and file I/O
pat_med = {"Name": "", "Date": "","Weight": "","BP": "","Symptoms": "","Medicine": []}

welcome_mssg = '''
    ** Welcome to Doctor Prescription System **

Enter medicine names one by one. Type 'n' to finish.
M = Morning
A = Afternoon
N = Night
'''

print(welcome_mssg)

def get_details():
    '''
        Input (as String): Patient details such as
            - Patient's name
            - Date of visitt
            - Patient's weight
            - Patient's BP
            - Symptoms

        It appends the input to value of corresponding key of 'pat_med' dictionary

        Returns: Patient name 
    '''
    p_name = input("Enter patient name: ").title()
    pat_med["Name"] = p_name[:31].ljust(31)

    date = input("Enter date (dd/mm/yyyy): ")
    pat_med["Date"] = date.ljust(14)

    weight = input("Enter weigth (in kg): ")
    pat_med["Weight"] = weight.ljust(25)

    bp = input("Enter BP (in mm Hg): ")
    pat_med["BP"] = bp.ljust(8)

    sym = input("Enter symptoms: ").title()
    pat_med["Symptoms"] = sym
    print("\n")
    return p_name

def get_med():
    '''
    Input (as String): Medicine details such as
        - Medicine name
        - Time of consumption
        - Number of days

    It appends the input to value of corresponding key of 'pat_med' dictionary

    Returns: Medicine name 
    '''
    m_name = input("Enter medicine name (or enter n to finish): ").title()
    if m_name != 'N':
        m_time = input("Enter time (M/A/N): ").upper()
        m_qty = input("Enter quantity to consume at a time (in g/ml/nos): ")
        m_days = input("Enter number of days: ")

        pat_med["Medicine"].append({"Med_name": m_name.ljust(27),"Time": m_time.center(11),"Qty": m_qty.center(8),"Days": m_days.center(8)})
    return m_name

pat_name = get_details()
med_name = get_med()

prescription = f'''
                   Doctor's Prescription
--------------------------------------------------------------
| Name: {pat_med["Name"]}| Date:{pat_med["Date"]} | 
| Weight(kg): {pat_med["Weight"]}| BP(mm Hg): {pat_med["BP"]} |
--------------------------------------------------------------
| Symptoms: {pat_med["Symptoms"][:48].ljust(48)} |
| {pat_med["Symptoms"][48:106].ljust(58)} |
--------------------------------------------------------------  
|          Medicine          |   Time    |   QTY   |   Days  |
--------------------------------------------------------------'''

while med_name != 'N':
    med_name = get_med()

with open(f"{pat_name}.txt","w") as file:
    file.write(prescription)
    for i,med in enumerate(pat_med['Medicine']): 
        file.write(f"\n|{i+1}. {med["Med_name"][:25]}|{med["Time"]}| {med["Qty"]}| {med["Days"]}|")
        file.write(f"\n|{med["Med_name"][24:52].ljust(28)}|           |         |         |")
    file.write("\n"+("-"*62))
    file.write("\n                       GET WELL SOON")

with open(f"{pat_name}.txt","r") as fileread:
    data=fileread.read()
print(data)

print("\nPrescription is ready to print!")
print(f"Saved as {pat_name}.txt")
print("\nThank you!")
