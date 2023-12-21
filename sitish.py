
from datetime import datetime,time



week1 = {
    "Monday" : ["Σπανακορυζο , Ριγκατονι με σαλτσα τυριων ή Πενες με σαλτσα Αμαριτσιανα , Σαλατα-φρουτο-γλυκο | Κεφτεδακια κοκκινιστα με πιλαφι ή λουκανικο χωριατικο με πατατες , Τυρι-σαλατα-φρουτο"],
    "Tuesday" : ["Κοτοσουπα , Παστιτσιο η κοτοπουλο με πατάτες , σαλατα-φρουτο | Κριθαροτο μανιταριων η φασολακια λαδερα με πατατες , σαλατα - φρουτο - κρεμα"] ,
    "Wednesday" : ["Ζυμαροπιτα ,φασολια φουρνου πλακι η φακες , σαλατα - πικλες | Μοσχαρακι γιουβετσι ή σουφλε ζυμαρικων με τυρια και μπέικον , σαλατα-γλυκο-φροτο"],
    "Thursday" : ["Χορτοσουπα , σπαγγετι με κιμα ή μπιφτεκι με πατατες , σαλατα-φρουτο  | Μπριαμ ή Αρακας καροτο λαδερος , σαλατα-τυρι-φρουτο"],
    "Friday" : ["Φαβα ,  κριθαροτο με γαριδες και καλαμαρι η ψαρι φουρνου λαδολεμονο με ριζοτο , σαλατα - φρουτο | ομελετα με λαχανικα και τυρια η βιδες με σαλτσα εποχης , φρουτο γαλα"],
    "Saturday" : ["Μανιταροσουποα , αρνακι γιουβετσι ή Σοφριτο με πουρε τυρι , σαλατα - φρουτο | Μπριζολα χοιρινη κρασατη με πιλφαι ή Σνιτσελ κοτοπουλο με πατατες , σαλατα-γιαουρτι-φρουτο"],
    "Sunday":["Σουπα του σεφ , χοιρινο λεμονατο η κοτοπουλο με πιλαφι , σαλατα-φρουτο | ψαρι πανε με πατατοσαλατα η σουτζουκακια σμυρναιικα με πουρε , σαλατα - φρουτο - γλυκο"]

}
week2 = {
    "Monday" : ["Λαχανικα αναμικτα", "σπαγγετι καρμποναρα η πεννες στον φουρνο με τυρια" , "σαλατα τυρι φρουτο" ," Μπιφτεκι με πουρε και σαλτσα μανιταριων" , "ομελετα με λαχανικα και τυρια", "σαλατα φρουτο γαλα"] ,
    "Tuesday" : ["Μανιταροπιτα , Μουσακας η κοτοπουλο μπιφτεκι με πατατες , ρυζογαλο σαλατα φρουτο | κεφτεδακια κοκκινιστα με πιλαφι ή σουφλε λαχανικων , σαλατα φρουτο , γλυκο"] , 
    "Wednesday" : ["Πουρε με μπεικον , φασολαδα η αρακας αναμικτος , σαλατα φρουτο , ταραμοσταλατα | σουπια με σπανακι η λαζανακι με σλατσα αλα κρεμ μανιταρια , σαλατα φρουτο ζελε"] ,
    "Thursday":["κοτοσουπα , κοτοπουλο ψητο με πατατες η χοιρινο με πιπερις και πιλαφι , σαλατα φρουτο γλυκο | σπανακορυζο ή μπριαμ , σαλατα φρουτο τυρι"],
    "Friday":["Μινεστρονε , σαρδελαα ψητη με πατατες φουρνο η κριθαροτο μανιταριων , σαλατα - φρουτο - χαλβα | γεμιστα λαδερα ή μακαρονια με κιμα , σαλατα - φρουτο - τυρι "],
    "Saturday":["Σουπα λαχανικων , μοσχαρακι κοκκινιστο με σπαγγετι η μπριζολα χοιρινη κρασατη με πιλαφι , σαλατα - φρουτο - τυρι | Λουκανικο με πατατες ή σνιτσελ κοτοπουλο με πουρε , σαλατα - φρουτο - τυρι"],
    "Sunday":["Ντοματοσουπα , σοτζουκακια με πουρε η χειρινο λεμονατο με πιλαφι , σαλατα φρουτο γαλα | πιτσα ή σπετσοφαι , σαλατα κρεμα φρουτο"]
}

week3 = {
    "Monday" : ["Βιδες με σαλτσα μεξικεν η σπαγγετι καρμποναρα , σαλατα - φρουτο - γλυκο | κοτοπουλο με κριθαρακι η μπιφτεκι με πατατεσ , τυρι - σαλατα - φρουτο"] ,
    "Tuesday" : ["Χορτοσουπα , γιοβαρλακια αυγολεμονο η πατατες ογκρατεν με τυρια και μπεικον , σαλατα-φρουτο-γαλα | ομελετα με πατατες πιπεριες αλλαντικα και τυρια ή ριγκατονι με σαλτσα τυριων , σαλατα φρουτο κρεμα"] , 
    "Wednesday" : ["ψαροσουπα , ριζοτο θαλασσινων η ψαρι φιλετο αλλα σπετσιωτα με πατατες , σαλατα χαλβα φρουτο | σπαγγετι με σαλτσα μεσογειο η αγγιναρες με αρακα καροτο και πατατα , σαλατα φρουτο κρεμα "] ,
    "Thursday":["Μινεστρονε , μπιφτεκι κοτοπουλο με γιουβετσι η χοιρινο ριγανατο και πιλαφι , σαλατα - φρουτο - γαλα , | μπαμιες η φασολακια με πατατες , σαλατα φρουτο τυρι"],
    "Friday":["πικλες , γιγαντες με χορτα η φακες , ταραμοσαλατα - ελιες σαλατα - φρουτο , κεφτεδακια δυοσμου με πουρε η πεννες με σαλτσαντοματασ και τυρι τριμμενο , σαλατα γαλα φρουτο  "],
    "Saturday":["Σουπα του σεφ", "χοιρινο ψητο με πουρε"," σοτζουκακια με πιλαφι" ," σαλατα φρουτο κομποστα" ,"||||","μελιτζανες παπουτσακι" ,"μακαρονια με κιμα" , "σαλατα φρουτο τυρι"],
    "Sunday":["Κρεατοσουπα , μοσχαρι γιουβετσι η μπριζολα χοιρινη με πατατες , σαλατα - φρουτο - ρυζογαλο | χταποδι κοφτο μακαρονακι η λουκανικο με πατατες , σαλατα - φρουτο γλυκο"]
}

week4 = {
    "Monday" : ["Κέικ",
            "Φρυγανιές",
            "Γάλα",
            "Τσάι",
            "Κολοκυθοπατάτες",
            "Βίδες με σάλτσα Μεσογείου",
            "Φιογκάκια με σάλτσα Αματριτσιάνα",
            "Σαλάτα εποχής",
            "Φρούτο",
            "Γλυκό",
            "Κεφτεδάκια κοκκινιστά με πουρέ",
            "Γιουβερλάκια αυγολέμονο",
            "Τυρί",
            "Σαλάτα εποχής",
            "Φρούτο"] ,
    "Tuesday" : ["Κέικ",
            "Φρυγανιές",
            "Γάλα",
            "Τσάι",
            "Σούπα του Σεφ",
            "Μπιφτέκι κοτόπουλο με πατάτες",
            "Χοιρινό λεμονάτο με πιλάφι",
            "Σαλάτα εποχής",
            "Φρούτο",
            "Γλυκό",
            "Κεφτεδάκια κοκκινιστά με πουρέ",
            "Γιουβερλάκια αυγολέμονο",
            "Τυρί",
            "Σαλάτα εποχής",
            "Φρούτο"] , 
    "Wednesday" : [
            "Κέικ",
            "Φρυγανιές",
            "Γάλα",
            "Τσάι",
            "Ντοματόσουπα",
            "Παστίτσιο μανιταριών",
            "Βακαλάος σκορδαλιά",
            "Σαλάτα εποχής",
            "Φρούτο",
            "Γάλα",
            "Λαχανοντολμάδες",
            "Σουφλέ ζυμαρικών με τυριά και αλλαντικά",
            "Σαλάτα εποχής",
            "Γιαούρτι",
            "Φρούτο"] ,
    "Thursday":["Κέικ",
            "Φρυγανιές",
            "Γάλα",
            "Τσάι",
            "Κοτόσουπα",
            "Μακαρόνια με Κιμά",
            "Κοτόπουλο με πιλάφι",
            "Σαλάτα εποχής",
            "Φρούτο",
            "Γάλα",
            "Σουτζουκάκια με πουρέ",
            "Πατάτες ογκρατέν"],
    "Friday":[ "Κέικ",
            "Φρυγανιές",
            "Γάλα",
            "Τσάι",
            "Πουρέ με μπέικον",
            "Ρεβύθια σούπα",
            "Φακές",
            "Σαλάτα εποχής",
            "Γιαούρτι",
            "Φρούτο",
            "Γάλα",
            "Καλαμαράκια γιαχνί με πιλάφι",
            "Λαζανάκι με σάλτσα ντομάτας και τυρί τριμμένο",
            "Σαλάτα εποχής",
            "Γιαούρτι",
            "Φρούτο"],
    "Saturday":[ "Κέικ",
            "Φρυγανιές",
            "Γάλα",
            "Τσάι",
            "Κρεατόσουπα",
            "Μοσχαράκι λεμονάτο με πιλάφι",
            "Μπριζόλα χοιρινή με πατάτες",
            "Σαλάτα εποχής",
            "Φρούτο",
            "Ρώσικη",
            "Ομελέτα με λαχανικά και τυριά",
            "Σνίτσελ κοτόπουλο με πουρέ",
            "Σαλάτα εποχής",
            "Φρούτο",
            "Τυρί"],
    "Sunday":["Κέικ",
            "Φρυγανιές",
            "Γάλα",
            "Τσάι",
            "Μινεστόνε",
            "Χοιρινό Κρητικό πιλάφι",
            "Γαλοπούλα με σάλτσα μουστάρδα και πουρέ",
            "Σαλάτα εποχής",
            "Φρούτο",
            "Κρέμα",
            "Πίτσα",
            "Λουκάνικο με πατάτες",
            "Σαλάτα εποχής",
            "Φρούτο",
            "Κρέμα"]
}





global week_number



def get_current_day_and_week(arg):
    
    
    global week_number
  
    
    choice = arg
    
    current_date = datetime.now()
    #week_number = (current_date.day - 1) // 7 + 1 #Current_week_number
    

    day  = str(current_date.day)
    month = str(current_date.month)
    final = day+"/"+month
    
    day_of_week = current_date.weekday() # Day of week
    
    days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    
  
    
    #print(f'Today is {days_of_week[day_of_week]}. It is week no:{week_number} of the month.')
    
    

    #Today's food
    
           
           
          
    if choice == "today":
           
        if week_number == 1:
            return(f"Food for {days_of_week[day_of_week]} [{final}] : {week1[days_of_week[day_of_week]]}")

        elif week_number == 2:
            return(f"Food for {days_of_week[day_of_week]} [{final}] : {week2[days_of_week[day_of_week]]}")
                        
        elif week_number == 3:
            return (f"Food for {days_of_week[day_of_week]} [{final}] : {week3[days_of_week[day_of_week]]}")
                     
        else:      
             return(f"Food for {days_of_week[day_of_week]} [{final}] : {week4[days_of_week[day_of_week]]}")
            
    #ebdomadiaio 
    
    if choice == "weekly":
           if week_number == 1:
               return(f"Food for Week 1  : {week1}")

           elif week_number == 2:
                return(f"Food for Week 2  : {week2}")
                
           elif week_number == 3:
               return (f"Food for Week 3  : {week3}\n")
             
           else:
                
               return(f"Food for Week 4 : {week4}")
    
    #Mera trexousas ebdomadas
    
    if choice in days_of_week:
        if week_number == 1:
            return(f"Food for {choice}  : {week1[choice]}")

        elif week_number == 2:
            return(f"Food for {choice}  : {week2[choice]}")
            
        elif week_number == 3:
            return(f"Food for {choice}  : {week3[choice]}")
         
        else:
            
            return(f"Food for {choice}  : {week4[choice]}")

    
    
    #fai gia thn epomenh mera
    if choice == "tomorrow":

       
        day_of_week = 0 if day_of_week == 6 else day_of_week + 1
        
        day  = str(current_date.day + 1)
        month = str(current_date.month)
        final = day+"/"+month
    
        
        
        if week_number == 1:
            return(f"Food for {days_of_week[day_of_week]} [{final}] : {week1[days_of_week[day_of_week]]}")

        elif week_number == 2:
            return(f"Food for {days_of_week[day_of_week]} [{final}] : {week2[days_of_week[day_of_week]]}")
                        
        elif week_number == 3:
            return (f"Food for {days_of_week[day_of_week]} [{final}] : {week3[days_of_week[day_of_week]]}")
                     
        else:      
             return(f"Food for {days_of_week[day_of_week]} [{final}] : {week4[days_of_week[day_of_week]]}")
        
    if choice == "schedule":
        allowed_time_ranges = [
                (time(7, 0), time(9, 0)),       
                (time(12, 30), time(16, 0)),     
                (time(18, 0), time(20, 0))       
            ]
        current_datetime = datetime.now()
        current_time = current_datetime.time()
            
        for start_time, end_time in allowed_time_ranges:
             if start_time <= current_time <= end_time:
                        return("sitish anoixth")
             else:
                     return("sitish kleisth")
           
def changeweek(opt):

    
    global week_number
     
    
    if opt =="reset":
        current_date = datetime.now()
        week_number = (current_date.day - 1) // 7 + 1 #Current_week_number
    
    
    
    if opt == "+":
        week_number += 1
   
    if opt == "-":
        week_number -= 1
 
        
    if week_number > 4 or week_number <1:
        return ("reset the week because currently its :",week_number)
          
#changeweek("reset"); #debugging
#get_current_day_and_week("today") #debugging
#changeweek("reset"); debugging

