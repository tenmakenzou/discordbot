
from datetime import datetime,time



week1 = {
    "Monday" : ["Μεσημεριανό: Σπανακορυζο , Ριγκατονι με σαλτσα τυριων ή Πενες με σαλτσα Αμαριτσιανα , Σαλατα-φρουτο-γλυκο", "Δείπνο: Κεφτεδακια κοκκινιστα με πιλαφι ή λουκανικο χωριατικο με πατατες , Τυρι-σαλατα-φρουτο"],
    "Tuesday" : ["Μεσημεριανό: Κοτοσουπα , Παστιτσιο η κοτοπουλο με πατάτες , σαλατα-φρουτο", "Δείπνο: Κριθαροτο μανιταριων η φασολακια λαδερα με πατατες , σαλατα - φρουτο - κρεμα"] ,
    "Wednesday" : ["Μεσημεριανό: Ζυμαροπιτα ,φασολια φουρνου πλακι η φακες , σαλατα - πικλες", "Δείπνο: Μοσχαρακι γιουβετσι ή σουφλε ζυμαρικων με τυρια και μπέικον , σαλατα-γλυκο-φροτο"],
    "Thursday" : ["Μεσημεριανό: Χορτοσουπα , σπαγγετι με κιμα ή μπιφτεκι με πατατες , σαλατα-φρουτο", "Δείπνο: Μπριαμ ή Αρακας καροτο λαδερος , σαλατα-τυρι-φρουτο"],
    "Friday" : ["Μεσημεριανό: Φαβα ,  κριθαροτο με γαριδες και καλαμαρι η ψαρι φουρνου λαδολεμονο με ριζοτο", "Δείπνο: ομελετα με λαχανικα και τυρια η βιδες με σαλτσα εποχης , φρουτο γαλα"],
    "Saturday" : ["Μεσημεριανό: Μανιταροσουποα , αρνακι γιουβετσι ή Σοφριτο με πουρε τυρι", "Δείπνο: Μπριζολα χοιρινη κρασατη με πιλφαι ή Σνιτσελ κοτοπουλο με πατατες , σαλατα-γιαουρτι-φρουτο"],
    "Sunday":["Μεσημεριανό: Σουπα του σεφ , χοιρινο λεμονατο η κοτοπουλο με πιλαφι , σαλατα-φρουτο", "Δείπνο: ψαρι πανε με πατατοσαλατα η σουτζουκακια σμυρναιικα με πουρε , σαλατα - φρουτο - γλυκο"]
}

week2 = {
    "Monday" : ["Μεσημεριανό: Λαχανικα αναμικτα, σπαγγετι καρμποναρα η πεννες στον φουρνο με τυρια, σαλατα τυρι φρουτο", "Δείπνο: Μπιφτεκι με πουρε και σαλτσα μανιταριων" , "ομελετα με λαχανικα και τυρια", "σαλατα φρουτο γαλα"] ,
    "Tuesday" : ["Μεσημεριανό: Μανιταροπιτα , Μουσακας η κοτοπουλο μπιφτεκι με πατατες , ρυζογαλο σαλατα φρουτο", "Δείπνο: κεφτεδακια κοκκινιστα με πιλαφι ή σουφλε λαχανικων , σαλατα φρουτο , γλυκο"] , 
    "Wednesday" : ["Μεσημεριανό: Πουρε με μπεικον , φασολαδα η αρακας αναμικτος , σαλατα φρουτο , ταραμοσταλατα", "Δείπνο: σουπια με σπανακι η λαζανακι με σλατσα αλα κρεμ μανιταρια , σαλατα φρουτο ζελε"] ,
    "Thursday":["Μεσημεριανό : κοτοσουπα , κοτοπουλο ψητο με πατατες η χοιρινο με πιπεριες και πιλαφι , σαλατα φρουτο γλυκο", "Δείπνο: σπανακορυζο ή μπριαμ , σαλατα φρουτο τυρι"],
    "Friday":["Μεσημεριανό: Μινεστρονε , σαρδελαα ψητη με πατατες φουρνο η κριθαροτο μανιταριων , σαλατα - φρουτο - χαλβα", "Δείπνο: γεμιστα λαδερα ή μακαρονια με κιμα , σαλατα - φρουτο - τυρι "],
    "Saturday":["Μεσημεριανό: Σουπα λαχανικων , μοσχαρακι κοκκινιστο με σπαγγετι η μπριζολα χοιρινη κρασατη με πιλαφι , σαλατα - φρουτο - τυρι", "Δείπνο: Λουκανικο με πατατες ή σνιτσελ κοτοπουλο με πουρε , σαλατα - φρουτο - τυρι"],
    "Sunday":["Μεσημεριανό: Ντοματοσουπα , σοτζουκακια με πουρε η χειρινο λεμονατο με πιλαφι , σαλατα φρουτο γαλα", "Δείπνο: πιτσα ή σπετσοφαι , σαλατα κρεμα φρουτο"]
}

week3 = {
    "Monday" : ["Μεσημεριανό: Βιδες με σαλτσα μεξικεν, σπαγγετι καρμποναρ , σαλατα - φρουτο - γλυκο", "Δείπνο: κοτοπουλο με κριθαρακι η μπιφτεκι με πατατεσ, τυρι - σαλατα - φρουτο"] ,
    "Tuesday" : ["Μεσημεριανό: Χορτοσουπα ,γιοβαρλακια αυγολεμονο ,πατατες ογκρατεν με τυρια και μπεικον  σαλατα-φρουτο-γαλα", "Δείπνο: ομελετα με πατατες πιπεριες αλλαντικα και τυρια,  ριγκατονι με σαλτσα τυριων, σαλατα φρουτο κρεμα"] , 
    "Wednesday" : ["Μεσημεριανό: ψαροσουπα , ριζοτο θαλασσινων, ψαρι φιλετο αλλα σπετσιωτα με πατατες , σαλατα χαλβα φρουτο", "Δείπνο: σπαγγετι με σαλτσα μεσογειο ,αγγιναρες με αρακα καροτο και πατατα , σαλατα φρουτο κρεμα "] ,
    "Thursday":["Μεσημεριανό: Μινεστρονε , μπιφτεκι κοτοπουλο με γιουβετσι , χοιρινο ριγανατο και πιλαφι , σαλατα - φρουτο - γαλα", "Δείπνο: μπαμιες , φασολακια με πατατες , σαλατα φρουτο τυρι"],
    "Friday":["Μεσημεριανό: πικλες , γιγαντες με χορτα , φακες  ταραμοσαλατα - ελιες σαλατα - φρουτο", "Δείπνο: κεφτεδακια δυοσμου με πουρε , πεννες με σαλτσαντοματας και τυρι τριμμενο , σαλατα γαλα φρουτο"],
    "Saturday":["Μεσημεριανό: Σουπα του σεφ, χοιρινο ψητο με πουρε, σουτζουκακια με πιλαφι , σαλατα φρουτο κομποστα", "Δείπνο: μελιτζανες παπουτσακι ,μακαρονια με κιμα , σαλατα φρουτο τυρι"],
    "Sunday":["Μεσημεριανό: Κρεατοσουπα , μοσχαρι γιουβετσι η μπριζολα χοιρινη με πατατες , σαλατα - φρουτο - ρυζογαλο", "Δείπνο: χταποδι κοφτο μακαρονακι η λουκανικο με πατατες , σαλατα - φρουτο γλυκο"]
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
               return("week1.jpg")

           elif week_number == 2:
                return("week2.jpg")
                
           elif week_number == 3:
               return("week3.jpg")
             
           else:
                
               return("week4.jpg")
    
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
           
         
        current_hour = current_date.hour
        current_time = float(current_date.strftime("%H.%M"))

        if ((7.30 <= current_time <= 9.0) or (12.30 <= current_time <= 15.40) or (18.00 <= current_time <= 20.30)):
            return("Η σιτίση ειναι ανοιχτή")
            
        else:
            if current_time < 7.30 or current_time >20.30:
                next_opening_time = "7:30"
            elif current_time < 12.30:
                next_opening_time = "12:30"
            elif current_time < 18.00:
                next_opening_time = "18:00"
            return( "Η σιτίση είναι κλείστη και ανοίγει στις: " + next_opening_time)
    
def changeweek(opt):

    global week_number
    
    
    if opt == 0:
        current_date = datetime.now()
        week_number = (current_date.day - 1) // 7 + 1 #Current_week_number
        
        return ("Current week has been reset")
    
    
    if opt <= 4 and opt >= 1 :
        week_number = opt
        return ("Current week has been changed to :",week_number)
 
