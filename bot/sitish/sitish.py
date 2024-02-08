
from datetime import datetime,time



week1 = {
    "Monday" : ["Πρωινό: Κέικ , Φρυγανιές , Γάλα , Τσάι","Μεσημεριανό: Σπανακορυζο , Ριγκατονι με σαλτσα τυριων , Πενες με σαλτσα Αμαριτσιανα , Σαλατα , φρουτο ,γλυκο", "Δείπνο: Κεφτεδακια κοκκινιστα με πιλαφι , λουκανικο χωριατικο με πατατες , Τυρι , σαλατα ,φρουτο"],
    "Tuesday" : ["Πρωινό: Κέικ , Φρυγανιές , Γάλα , Τσάι","Μεσημεριανό: Κοτοσουπα , Παστιτσιο , κοτοπουλο με πατάτες , σαλατα , φρουτο", "Δείπνο: Κριθαροτο μανιταριων η φασολακια λαδερα με πατατες , σαλατα , φρουτο , κρεμα"] ,
    "Wednesday" : ["Πρωινό: Κέικ , Φρυγανιές , Γάλα , Τσάι","Μεσημεριανό: Ζυμαροπιτα ,φασολια φουρνου πλακι , φακες , σαλατα , πικλες", "Δείπνο: Μοσχαρακι γιουβετσι , σουφλε ζυμαρικων με τυρια και μπέικον , σαλατα-γλυκο-φροτο"],
    "Thursday" : ["Πρωινό: Κέικ , Φρυγανιές , Γάλα , Τσάι","Μεσημεριανό: Χορτοσουπα , σπαγγετι με κιμα , μπιφτεκι με πατατες , σαλατα ,φρουτο", "Δείπνο: Μπριαμ , Αρακας καροτο λαδερος , σαλατα-τυρι-φρουτο"],
    "Friday" : ["Πρωινό: Κέικ , Φρυγανιές , Γάλα , Τσάι","Μεσημεριανό: Φαβα ,  κριθαροτο με γαριδες και καλαμαρι , ψαρι φουρνου λαδολεμονο με ριζοτο", "Δείπνο: ομελετα με λαχανικα και τυρια η βιδες με σαλτσα εποχης , φρουτο γαλα"],
    "Saturday" : ["Πρωινό: Κέικ , Φρυγανιές , Γάλα , Τσάι","Μεσημεριανό: Μανιταροσουποα , αρνακι γιουβετσι , Σοφριτο με πουρε τυρι", "Δείπνο: Μπριζολα χοιρινη κρασατη με πιλφαι , Σνιτσελ κοτοπουλο με πατατες , σαλατα ,γιαουρτι , φρουτο"],
    "Sunday":["Πρωινό: Κέικ , Φρυγανιές , Γάλα , Τσάι","Μεσημεριανό: Σουπα του σεφ , χοιρινο λεμονατο , κοτοπουλο με πιλαφι , σαλατα ,φρουτο", "Δείπνο: ψαρι πανε με πατατοσαλατα η σουτζουκακια σμυρναιικα με πουρε , σαλατα , φρουτο , γλυκο"]
}

week2 = {
    "Monday" : ["Πρωινό: Κέικ , Φρυγανιές , Γάλα , Τσάι","Μεσημεριανό: Λαχανικά αναμεικτά, σπαγγέτι καρμπονάρα ή πέννες στον φούρνο με τυριά, σαλάτα τυρί φρούτο", "Δείπνο: Μπιφτέκι με πουρέ και σάλτσα μανιταριών" , "ομελέτα με λαχανικά και τυριά", "σαλάτα , φρούτο , γάλα"] ,
    "Tuesday" : ["Πρωινό: Κέικ , Φρυγανιές , Γάλα , Τσάι","Μεσημεριανό: Μανιταρόπιτα , Μουσακάς , κοτόπουλο μπιφτέκι με πατάτες , ρυζόγαλο , σαλάτα , φρούτο", "Δείπνο: κεφτεδάκια κοκκινιστά με πιλάφι , σουφλέ λαχανικών , σαλάτα , φρούτο , γλυκό"] , 
    "Wednesday" : ["Πρωινό: Κέικ , Φρυγανιές , Γάλα , Τσάι","Μεσημεριανό: Πουρέ με μπέικον , φασολάδα , αρακάς αναμεικτός , σαλάτα φρούτο , ταραμοσαλάτα", "Δείπνο: σουπιά με σπανάκι ή λαζανάκι με σλάτσα αλά κρεμ μανιτάρια , σαλάτα , φρούτο , ζελέ"] ,
    "Thursday":["Πρωινό: Κέικ , Φρυγανιές , Γάλα , Τσάι","Μεσημεριανό: κοτόσουπα , κοτόπουλο ψητό με πατάτες ή χοιρινό με πιπεριές και πιλάφι , σαλάτα φρούτο γλυκό", "Δείπνο: σπανακόρυζο , μπριάμ , σαλάτα , φρούτο , τυρί"],
    "Friday":["Πρωινό: Κέικ , Φρυγανιές , Γάλα , Τσάι","Μεσημεριανό: Μινεστρόνε , σαρδέλα ψητή με πατάτες φούρνο , κριθαρότο μανιταριών , σαλάτα , φρούτο , χαλβά", "Δείπνο: γεμιστά λαδερά , μακαρονιά με κιμά , σαλάτα , φρούτο , τυρί "],
    "Saturday":["Πρωινό: Κέικ , Φρυγανιές , Γάλα , Τσάι","Μεσημεριανό: Σουπα λαχανικών , μοσχαράκι κοκκινιστό με σπαγγέτι , μπριζόλα χοιρινή κρασάτη με πιλάφι , σαλάτα , φρούτο , τυρί", "Δείπνο: Λουκάνικο με πατάτες , σνίτσελ κοτόπουλο με πουρέ , σαλάτα - φρούτο - τυρί"],
    "Sunday":["Πρωινό: Κέικ , Φρυγανιές , Γάλα , Τσάι","Μεσημεριανό: Ντοματοσούπα , σοτζουκάκια με πουρέ , χειρινό λεμονάτο με πιλάφι , σαλάτα , φρούτο , γάλα", "Δείπνο: πίτσα , σπετσοφαί , σαλάτα , κρέμα , φρούτο"]
}


week3 = {
    "Monday" : ["Πρωινό: Κέικ , Φρυγανιές , Γάλα , Τσάι","Μεσημεριανό: Βίδες με σάλτσα μεξικάνικη, σπαγγέτι καρμπονάρα , σαλάτα , φρούτο , γλυκό", "Δείπνο: κοτόπουλο με κριθαράκι , μπιφτέκι με πατάτες, τυρί , σαλάτα , φρούτο"] ,
    "Tuesday" : ["Πρωινό: Κέικ , Φρυγανιές , Γάλα , Τσάι","Μεσημεριανό: Χορτοσούπα ,γιουβαρλάκια αυγολέμονο ,πατάτες ογκρατέν με τυριά και μπέικον  σαλάτα , φρούτο ,γάλα", "Δείπνο: ομελέτα με πατάτες πιπεριές αλλαντικά και τυριά,  ριγκατόνι με σάλτσα τυριών, σαλάτα , φρούτο , κρέμα"] , 
    "Wednesday" : ["Πρωινό: Κέικ , Φρυγανιές , Γάλα , Τσάι","Μεσημεριανό: ψαροσούπα , ριζότο θαλασσινών, ψάρι φιλέτο αλλά σπετσιώτα με πατάτες , σαλάτα χαλβά φρούτο", "Δείπνο: σπαγγέτι με σάλτσα μεσογείου ,αγκινάρες με αρακά καρότο και πατάτα , σαλάτα , φρούτο , κρέμα "] ,
    "Thursday":["Πρωινό: Κέικ , Φρυγανιές , Γάλα , Τσάι","Μεσημεριανό: Μινεστρόνε , μπιφτέκι κοτόπουλο με γιουβέτσι , χοιρινό ριγανάτο και πιλάφι , σαλάτα , φρούτο , γάλα", "Δείπνο: μπάμιες , φασολάκια με πατάτες , σαλάτα , φρούτο , τυρί"],
    "Friday":["Πρωινό: Κέικ , Φρυγανιές , Γάλα , Τσάι","Μεσημεριανό: πικλές , γίγαντες με χόρτα , φακές  ταραμοσαλάτα - ελιές , σαλάτα , φρούτο", "Δείπνο: κεφτεδάκια δυόσμου με πουρέ , πέννες με σαλτσαντομάτας και τυρί τριμμένο , σαλάτα , γάλα , φρούτο"],
    "Saturday":["Πρωινό: Κέικ , Φρυγανιές , Γάλα , Τσάι","Μεσημεριανό: Σουπα του σεφ, χοιρινό ψητό με πουρέ, σουτζουκάκια με πιλάφι , σαλάτα , φρούτο , κομπόστα", "Δείπνο: μελιτζάνες παπουτσάκι ,μακαρόνια με κιμά , σαλάτα , φρούτο , τυρί"],
    "Sunday":["Πρωινό: Κέικ , Φρυγανιές , Γάλα , Τσάι","Μεσημεριανό: Κρεατοσούπα , μοσχάρι γιουβέτσι , μπριζόλα χοιρινή με πατάτες , σαλάτα , φρούτο , ρυζόγαλο", "Δείπνο: χταπόδι κοφτό μακαρονάκι , λουκάνικο με πατάτες , σαλάτα , φρούτο γλυκό"]
}



week4 = {
    "Monday" : ["Πρωινό: Κέικ , Φρυγανιές , Γάλα , Τσάι","Μεσημεριανό: Κολοκυθοπατάτες, Βίδες με σάλτσα Μεσογείου, Φιογκάκια με σάλτσα Αματριτσιάνα, Σαλάτα εποχής, Φρούτο, Γλυκό", "Δείπνο: Κεφτεδάκια κοκκινιστά με πουρέ, Γιουβερλάκια αυγολέμονο, Τυρί, Σαλάτα εποχής, Φρούτο"] ,
    "Tuesday" : ["Πρωινό: Κέικ , Φρυγανιές , Γάλα , Τσάι","Μεσημεριανό: Σούπα του Σεφ, Μπιφτέκι κοτόπουλο με πατάτες, Χοιρινό λεμονάτο με πιλάφι, Σαλάτα εποχής, Φρούτο, Γλυκό","Δείπνο: Κεφτεδάκια κοκκινιστά με πουρέ, Γιουβερλάκια αυγολέμονο, Τυρί, Σαλάτα εποχής, Φρούτο"] , 
    "Wednesday" : ["Πρωινό: Κέικ , Φρυγανιές , Γάλα , Τσάι","Μεσημεριανό: Ντοματόσουπα, Παστίτσιο μανιταριών, Βακαλάος σκορδαλιά, Σαλάτα εποχής, Φρούτο, Γάλα, Λαχανοντολμάδες, Σουφλέ ζυμαρικών με τυριά και αλλαντικά, Σαλάτα εποχής, Γιαούρτι, Φρούτο"] ,
    "Thursday":["Πρωινό: Κέικ , Φρυγανιές , Γάλα , Τσάι","Μεσημεριανό: Κοτόσουπα, Μακαρόνια με Κιμά, Κοτόπουλο με πιλάφι, Σαλάτα εποχής, Φρούτο, Γάλα","Δείπνο: Σουτζουκάκια με πουρέ, Πατάτες ογκρατέν"] ,
    "Friday": ["Πρωινό: Κέικ , Φρυγανιές , Γάλα , Τσάι","Μεσημεριανό: Πουρέ με μπέικον, Ρεβύθια σούπα, Φακές, Σαλάτα εποχής, Γιαούρτι, Φρούτο, Γάλα","Δείπνο: Καλαμαράκια γιαχνί με πιλάφι, Λαζανάκι με σάλτσα ντομάτας και τυρί τριμμένο, Σαλάτα εποχής, Γιαούρτι, Φρούτο"] ,
    "Saturday": ["Πρωινό: Κέικ , Φρυγανιές , Γάλα , Τσάι","Μεσημεριανό: Κρεατόσουπα, Μοσχαράκι λεμονάτο με πιλάφι, Μπριζόλα χοιρινή με πατάτες, Σαλάτα εποχής, Φρούτο, Ρώσικη, Ομελέτα με λαχανικά και τυριά","Δείπνο: Σνίτσελ κοτόπουλο με πουρέ, Σαλάτα εποχής, Φρούτο, Τυρί"] ,
    "Sunday": ["Πρωινό: Κέικ , Φρυγανιές , Γάλα , Τσάι", "Μεσημεριανό: Μινεστόνε, Χοιρινό Κρητικό πιλάφι, Γαλοπούλα με σάλτσα μουστάρδα και πουρέ, Σαλάτα εποχής, Φρούτο, Κρέμα, Πίτσα", "Δείπνο: Λουκάνικο με πατάτες, Σαλάτα εποχής, Φρούτο, Κρέμα"]
}




global bonus 
bonus = 0




def get_current_day_and_week(choice):
    
    current_date = datetime.now()

    week_number = ((current_date.day - 1) // 7 + 1) + bonus #Current_week_number

    day  = str(current_date.day)
    month = str(current_date.month)
    final = day+"/"+month
    
    day_of_week = current_date.weekday() # Day of week
    
    days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    
  
    
    x = days_of_week[day_of_week]

    
    
    if week_number == 1:
        week = week1

    elif week_number == 2:
        week = week2
            
    elif week_number == 3:
        week = week3
         
    else:
       week = week4

          
    if choice == "today":
            return(f"Food for {x} [{final}] : \n\n{week[x][0]}\n\n{week[x][1]}\n\n{week[x][2]}")

            
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
   
    if choice in days_of_week:
        return(f"Food for {choice}  : {week[choice]}")

    

    if choice == "tomorrow":
        
        day  = str(current_date.day + 1)
        final = day+"/"+month
    
        
          
        if week_number == 1:
            return(f"Food for {x} [{final}] : \n\n{week1[x][0]}\n\n{week1[x][1]}\n\n{week1[x][2]}")

        elif week_number == 2:
            return(f"Food for {x} [{final}] : \n\n{week2[x][0]}\n\n{week2[x][1]}\n\n{week2[x][2]}")
       
        elif week_number == 3:
            return(f"Food for {x} [{final}] : \n\n{week3[x][0]}\n\n{week3[x][1]}\n\n{week3[x][2]}")
                     
        else:      
             return(f"Food for {x} [{final}] : \n\n{week4[x][0]}\n\n{week4[x][1]}\n\n{week4[x][2]}")
        
    
    
   
    
    if choice == "open":
           
         
        current_hour = current_date.hour
        current_time = float(current_date.strftime("%H.%M"))


        

        if ((7.30 <= current_time <= 9.0) or (12.30 <= current_time <= 15.40) or (18.00 <= current_time <= 20.30)):
            return("Η σιτίση ειναι ανοιχτή")
            
        else:
            if current_time < 7.30 or current_time >20.30:
                next_opening_time = "7:30"
                return (f"Η σιτίση είναι κλείστη , ανοίγει στις : {next_opening_time} και εχει :\n {week[x][0]}")
            elif current_time < 12.30:
                next_opening_time = "12:30"
                return (f"Η σιτίση είναι κλείστη , ανοίγει στις : {next_opening_time} και εχει :\n {week[x][1]}")

            elif current_time < 18.00:
                next_opening_time = "18:00"
                return (f"Η σιτίση είναι κλείστη , ανοίγει στις : {next_opening_time} και εχει :\n {week[x][2]}")


    if (not choice == "tomorrow" and not choice == "today" and not choice == "open" and not choice == "weekly"):
        return("Invalid arguement")
    
def changeweek(opt):
    
    if opt == 1:
        bonus += 1
        return ("Current week has been increased")
    
    if opt == -1:
       
        bonus -= 1
        return ("Current week has been decreased")
    
    if bonus > 4 or bonus < 1 :
        bonus = 0
 
     
    
    
