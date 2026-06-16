"""This project is a time calculator. but it is designed for a laboratory that uses climatic chambers
to incubate vials. the vials must be incubated 7 days at 25ºC, then switch to 35ºC and
incubate for another 7 days. The problem is that there are several chambers and each one
has a different switch time from 25ºC to 35ª that does not count for the total incubation time

This is a program to solve a problem in my daily bassis at work, so I create it to help me to control all the incubations times an rooms
"""


from datetime import datetime, timedelta  #Library that i need to import to do the maths with dates and time. do not know if its work on stanford IDE

#I create a dictionary with all the climatic chambers and its incubation swich-times: {Name of the chamber : hours of switch-times}

INCUBATION_CHAMBERS= {
    "MC28" : 18,
    "MC29" : 16,
    "H1-11" : 13,
    "P1-44" : 13,
    "8132" : 25,
}
CHAMBER_LIST = list(INCUBATION_CHAMBERS.keys())  #I transferred all the chambers from the dictionary to a list, so I can print all of them

#Then I created this dictionary to check the status of every chamber, if it is free or not and their times
INCUBATION_CHAMBERS_STATUS= {   
    "MC28" : None,
    "MC29" : None,
    "H1-11" : None,
    "P1-44" : None,
    "8132" : None,
}



def main():

    """ Initial Interface Idea
    The program should first ask what the user wants. Like check the status of a incubation chamber; start an incubation, check the status or modify the status of a chamber.
    It would be nice if the navigablable menu works by numbers, so the user only needs to write a number, instead the full option: 
    1) Start incubation: aks the usser if you want to Start an incubation at any chamber
    2) Check the status of X chamber (Empty or incubation at X ºC, days left of incubation X days for pahse 25ºC and X days for 35ºC)
    3) Modify incubation: Allows to delete the incubation data at a chamber (if a mistake is made or something like that); Modify a switch time; add or eliminate a new climatic chamber
    4) Add a step of "Go back" in every navigation point.
    """

# 1) Start and incubation: the program ask the usser to choose a climatic chamber and the start date
    def start_incubation():
        while True:
            print(f"List of Chambers: {CHAMBER_LIST}")
            chamber_selected = input(f"Select and incubation chamber or press 0 to retunr to the Main Menu: ")
            if chamber_selected in INCUBATION_CHAMBERS:
                switch_time = INCUBATION_CHAMBERS[chamber_selected]
                print(f"for the incubation chamber {chamber_selected} the switch time is {switch_time} hours")
                check_chamber(chamber_selected, switch_time) #This function is the same than the 2) Check incubation from main menu, but it keeps going with the calculations
                return
            elif chamber_selected == "0": #Returns to the main menu if usser presses "0"
                return
            else: #If a mistakes is made with the imput, it warms the user
                print("That chamber is not on the list")

        #It should also chek here if the chamber is ocupied and alarm the user!!!! PENDING!!! def check_chamber_status

# Check if the chamber is free or occupied, as well as their incubation times and current incubation phase
    def check_chamber(chamber_selected, switch_time):
        if INCUBATION_CHAMBERS_STATUS[chamber_selected] is None:
            print("The chamber is free. Do you want to incubate here? 1)Yes / 2)No")
            book_chamber = input(" ")
            if book_chamber == "1":
                print(f"Incubation chamber {chamber_selected} has been booked")
                calculating_incubation_times(switch_time, chamber_selected) #do the incubation maths for that chamber
            elif book_chamber == "2":
                return

            else: print("That option is not avaiable")
            
        #Continue developping here. To make the program have a memory of the status and time of every chamber
        
        #For future versions the program could check the current date of the compute, checking if the incubation is on going or finished.
    

        #Ask for starting date and do the maths with the hour swift time taking into acount. divide it into 2 phases, 25ºC and 35ºC and do the maths
    def calculating_incubation_times(switch_time, chamber_selected):
        incubation_start_input = input ("Enter the incubation star time (DD/MM/YYYY HH:MM): ") #user input of the starting time
        start_date = datetime.strptime(incubation_start_input, "%d/%m/%Y %H:%M") #Converting input on a string #If a mistake is made with the formart. It creates an error, I could try to fix that

        #25º Incubation phase = Starting time + 7 days
        first_incubation = start_date + timedelta(days=7)
        print(f"-The incubation at 25ºC starts on the {start_date.strftime('%d/%m/%Y %H:%M')} and ends on the {first_incubation.strftime('%d/%m/%Y %H:%M')}")

        # Add the switch time of the incubation chamber from 25ª to 35ºC, to the first incubation phase
        incubation_after_switch = first_incubation + timedelta(hours=switch_time)
        print(f"-The switch from 25ºC to 35ºC ends at {incubation_after_switch.strftime('%d/%m/%Y %H:%M')}")

        #35ºC incubation phase = incubation_after_switch + 7 days
        end_date = incubation_after_switch + timedelta(days=7)
        print(f"-The incubation at 35ºC ends at {end_date.strftime('%d/%m/%Y %H:%M')}")
        #Save information about the incubation status of the selected chamber

        INCUBATION_CHAMBERS_STATUS[chamber_selected] = {
        "start_date": start_date,
        "switch_date": first_incubation,
        "transition_end": incubation_after_switch,
        "end_date": end_date
        }


#2) Check the status of any chamber
    def check_incubation():
        print(f"List of Chambers: {CHAMBER_LIST}")
        chamber_info = input (f"Wich chamber do you want to check? ")
        if INCUBATION_CHAMBERS_STATUS[chamber_info] is None:
            print("The chamber is free.")
            return
        else: 
            print("The chamber is booked")
            
            data = INCUBATION_CHAMBERS_STATUS[chamber_info]
            print(f"Start date: {data['start_date'].strftime('%d/%m/%Y %H:%M')}")
            print(f"Switch date: {data['switch_date'].strftime('%d/%m/%Y %H:%M')}")
            print(f"Transition ends: {data['transition_end'].strftime('%d/%m/%Y %H:%M')}")
            print(f"End date: {data['end_date'].strftime('%d/%m/%Y %H:%M')}")
            return


#0) Initial Menu, 3 options are given. Ass you navigate, an option of "Going Back" is inclueded, wich will take usser back to the main menu

    def main_menu():
        while True:
            print("\n--- MAIN MENU ---")
            print("1) Start incubation")
            print("2) Check incubation") #Under Construction
            #print("3) Configuration") #Configuration will be avaiable in future versions of the programm

            option = input("Select an option: ")
                
            if option == "1":
                start_incubation()
            elif option == "2":
                check_incubation()
            #elif option == "3":
                #configuration() #Configuration will be avaiable in future versions of the programm
            elif option == "0":
                break
            else:
                print("Error, write again your option")


    main_menu()

if __name__ == "__main__":
    main()