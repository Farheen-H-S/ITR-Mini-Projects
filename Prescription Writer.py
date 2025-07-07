from tkinter import *
root = Tk()
root.title("Prescription Writer")
root["bg"] = "lightgray"
root.resizable(False,False)

med_list = []

def update_display():
    display_text=""
    for i,med in enumerate(med_list,start=1):
        display_text+= f"{i}. {med.title()}\n"
    display_meds["text"]=display_text

def add_med():
    med = userin.get()
    if med:
        med_list.append(med)
        update_display()
        userin.delete(0,END)
        print(f"'{med.title()}' added to prescription")

def clear_entry():
    userin.delete(0,END)

def save_pres():
    with open ("prescription.txt","w") as file:
        for i,med in enumerate(med_list,start=1):
            file.write(f"{i}. {med.title()}\n")
    display_meds["text"] = "The prescription.txt has been saved!"
    print("Prescription saved!")

#create
enter_med = Label(root, text="Enter medicine name: ", bg="lightgray")
userin = Entry(root, width=45)
add_med = Button(root, text="Add Medicine", width=15, padx=10, pady=5, bg="green", fg="white", command=add_med)
clear_entry = Button(root, text="CLEAR", width=15, padx=10, pady=5, bg="red", fg="white", command=clear_entry)
save_pres = Button(root, text="Save Prescription", width=35, padx=10, pady=5, bg="blue", fg="white", command=save_pres)
display_meds = Label(root, text="", justify=LEFT, bg='lightgray', fg='blue')

#display
enter_med.grid(row=0, column=0, padx=5)
userin.grid(row=1, column=0, columnspan=2, pady=2)
add_med.grid(row=3, column=0, pady=5, padx=2)
clear_entry.grid(row=3, column=1, padx=2, pady=5)
save_pres.grid(row=4, column=0, columnspan=2, pady=2, padx=3)
display_meds.grid(columnspan=2)

root.mainloop()
