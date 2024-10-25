def display_schedule(skill):    #find the schedule for the user
    schedule = {
        "skating": "Monday and Thursday",
        "stickhandling": "Tuesday and Friday",
        "shooting": "Wednesday and Saturday",
        "passing": "Thursday and Sunday",        #tells when these certain skills will be practiced
        "defense": "Friday and Monday",
        "goalie drills": "Saturday and Tuesday"}
    
    if skill in schedule:
        print(f"\nYou will practice {skill.title()} on {schedule[skill]}.\n")  #tells user when they will pracatice the skill selected
    else:
        print(f"\nSorry, {skill} is not in the practice schedule.\n") #tells user that the skill is not available

skills = ["skating", "stickhandling", "shooting", "passing", "defense", "goalie drills"]  #tells skills that are practiced

print("Welcome to the Ice Hockey Practice Schedule Program!")     #Welcomes user to the program

while True:
    print("\nAvailable Skills:")
    for skill in skills:               #uses a loop to prompt the user with a selection of skills to practice
        print(f"- {skill.title()}")
    
    user_skill = input("\nWhich hockey skill would you like to practice? (or type 'done' to exit): ").lower() #asks user which skill they want to practice 

    if user_skill == 'done': #code word to end program when the user is done
        print("Thank you for using the Ice Hockey Practice Schedule Program! Good luck with your practice!")  #thanks the user for using the practice plan program
        break #ends the code for the user 
    
    display_schedule(user_skill) #calls the function and uses an argument