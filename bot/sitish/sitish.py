
from datetime import datetime,time



week1 = {
    "Monday" : ["Πρωινό : Κέικ , Φρυγανιές , Γάλα , Τσάι","Μεσημεριανό: Σπανακορυζο , Ριγκατονι με σαλτσα τυριων , Πενες με σαλτσα Αμαριτσιανα , Σαλατα , φρουτο ,γλυκο", "Δείπνο: Κεφτεδακια κοκκινιστα με πιλαφι , λουκανικο χωριατικο με πατατες , Τυρι , σαλατα ,φρουτο"],
    "Tuesday" : ["Πρωινό : Κέικ , Φρυγανιές , Γάλα , Τσάι","Μεσημεριανό: Κοτοσουπα , Παστιτσιο , κοτοπουλο με πατάτες , σαλατα , φρουτο", "Δείπνο: Κριθαροτο μανιταριων η φασολακια λαδερα με πατατες , σαλατα , φρουτο , κρεμα"] ,
    "Wednesday" : ["Πρωινό : Κέικ , Φρυγανιές , Γάλα , Τσάι","Μεσημεριανό: Ζυμαροπιτα ,φασολια φουρνου πλακι , φακες , σαλατα , πικλες", "Δείπνο: Μοσχαρακι γιουβετσι , σουφλε ζυμαρικων με τυρια και μπέικον , σαλατα-γλυκο-φροτο"],
    "Thursday" : ["Πρωινό : Κέικ , Φρυγανιές , Γάλα , Τσάι","Μεσημεριανό: Χορτοσουπα , σπαγγετι με κιμα , μπιφτεκι με πατατες , σαλατα ,φρουτο", "Δείπνο: Μπριαμ , Αρακας καροτο λαδερος , σαλατα-τυρι-φρουτο"],
    "Friday" : ["Πρωινό : Κέικ , Φρυγανιές , Γάλα , Τσάι","Μεσημεριανό: Φαβα ,  κριθαροτο με γαριδες και καλαμαρι , ψαρι φουρνου λαδολεμονο με ριζοτο", "Δείπνο: ομελετα με λαχανικα και τυρια η βιδες με σαλτσα εποχης , φρουτο γαλα"],
    "Saturday" : ["Πρωινό : Κέικ , Φρυγανιές , Γάλα , Τσάι","Μεσημεριανό: Μανιταροσουποα , αρνακι γιουβετσι , Σοφριτο με πουρε τυρι", "Δείπνο: Μπριζολα χοιρινη κρασατη με πιλφαι , Σνιτσελ κοτοπουλο με πατατες , σαλατα ,γιαουρτι , φρουτο"],
    "Sunday":["Πρωινό : Κέικ , Φρυγανιές , Γάλα , Τσάι","Μεσημεριανό: Σουπα του σεφ , χοιρινο λεμονατο , κοτοπουλο με πιλαφι , σαλατα ,φρουτο", "Δείπνο: ψαρι πανε με πατατοσαλατα η σουτζουκακια σμυρναιικα με πουρε , σαλατα , φρουτο , γλυκο"]
}

week2 = {
    "Monday" : ["Πρωινό : Κέικ , Φρυγανιές , Γάλα , Τσάι","Μεσημεριανό: Λαχανικα αναμικτα, σπαγγετι καρμποναρα η πεννες στον φουρνο με τυρια, σαλατα τυρι φρουτο", "Δείπνο: Μπιφτεκι με πουρε και σαλτσα μανιταριων" , "ομελετα με λαχανικα και τυρια", "σαλατα , φρουτο , γαλα"] ,
    "Tuesday" : ["Πρωινό : Κέικ , Φρυγανιές , Γάλα , Τσάι","Μεσημεριανό: Μανιταροπιτα , Μουσακας , κοτοπουλο μπιφτεκι με πατατες , ρυζογαλο , σαλατα , φρουτο", "Δείπνο: κεφτεδακια κοκκινιστα με πιλαφι , σουφλε λαχανικων , σαλατα , φρουτο , γλυκο"] , 
    "Wednesday" : ["Πρωινό : Κέικ , Φρυγανιές , Γάλα , Τσάι","Μεσημεριανό: Πουρε με μπεικον , φασολαδα , αρακας αναμικτος , σαλατα φρουτο , ταραμοσταλατα", "Δείπνο: σουπια με σπανακι η λαζανακι με σλατσα αλα κρεμ μανιταρια , σαλατα , φρουτο , ζελε"] ,
    "Thursday":["Πρωινό : Κέικ , Φρυγανιές , Γάλα , Τσάι","Μεσημεριανό : κοτοσουπα , κοτοπουλο ψητο με πατατες η χοιρινο με πιπεριες και πιλαφι , σαλατα φρουτο γλυκο", "Δείπνο: σπανακορυζο , μπριαμ , σαλατα , φρουτο , τυρι"],
    "Friday":["Πρωινό : Κέικ , Φρυγανιές , Γάλα , Τσάι","Μεσημεριανό: Μινεστρονε , σαρδελαα ψητη με πατατες φουρνο , κριθαροτο μανιταριων , σαλατα , φρουτο , χαλβα", "Δείπνο: γεμιστα λαδερα , μακαρονια με κιμα , σαλατα , φρουτο , τυρι "],
    "Saturday":["Πρωινό : Κέικ , Φρυγανιές , Γάλα , Τσάι","Μεσημεριανό: Σουπα λαχανικων , μοσχαρακι κοκκινιστο με σπαγγετι , μπριζολα χοιρινη κρασατη με πιλαφι , σαλατα , φρουτο , τυρι", "Δείπνο: Λουκανικο με πατατες , σνιτσελ κοτοπουλο με πουρε , σαλατα - φρουτο - τυρι"],
    "Sunday":["Πρωινό : Κέικ , Φρυγανιές , Γάλα , Τσάι","Μεσημεριανό: Ντοματοσουπα , σοτζουκακια με πουρε , χειρινο λεμονατο με πιλαφι , σαλατα , φρουτο , γαλα", "Δείπνο: πιτσα , σπετσοφαι , σαλατα , κρεμα , φρουτο"]
}

week3 = {
    "Monday" : ["Πρωινό : Κέικ , Φρυγανιές , Γάλα , Τσάι","Μεσημεριανό: Βίδες με σάλτσα μεξικάνικη, σπαγγέτι καρμπονάρα , σαλάτα , φρούτο , γλυκό", "Δείπνο: κοτόπουλο με κριθαράκι , μπιφτέκι με πατάτες, τυρί , σαλάτα , φρούτο"] ,
    "Tuesday" : ["Πρωινό : Κέικ , Φρυγανιές , Γάλα , Τσάι","Μεσημεριανό: Χορτοσούπα ,γιουβαρλάκια αυγολέμονο ,πατάτες ογκρατέν με τυριά και μπέικον  σαλάτα , φρούτο ,γάλα", "Δείπνο: ομελέτα με πατάτες πιπεριές αλλαντικά και τυριά,  ριγκατόνι με σάλτσα τυριών, σαλάτα , φρούτο , κρέμα"] , 
    "Wednesday" : ["Πρωινό : Κέικ , Φρυγανιές , Γάλα , Τσάι","Μεσημεριανό: ψαροσούπα , ριζότο θαλασσινών, ψάρι φιλέτο αλλά σπετσιώτα με πατάτες , σαλάτα χαλβά φρούτο", "Δείπνο: σπαγγέτι με σάλτσα μεσογείου ,αγκινάρες με αρακά καρότο και πατάτα , σαλάτα , φρούτο , κρέμα "] ,
    "Thursday":["Πρωινό : Κέικ , Φρυγανιές , Γάλα , Τσάι","Μεσημεριανό: Μινεστρόνε , μπιφτέκι κοτόπουλο με γιουβέτσι , χοιρινό ριγανάτο και πιλάφι , σαλάτα , φρούτο , γάλα", "Δείπνο: μπάμιες , φασολάκια με πατάτες , σαλάτα , φρούτο , τυρί"],
    "Friday":["Πρωινό : Κέικ , Φρυγανιές , Γάλα , Τσάι","Μεσημεριανό: πικλές , γίγαντες με χόρτα , φακές  ταραμοσαλάτα - ελιές , σαλάτα , φρούτο", "Δείπνο: κεφτεδάκια δυόσμου με πουρέ , πέννες με σαλτσαντομάτας και τυρί τριμμένο , σαλάτα , γάλα , φρούτο"],
    "Saturday":["Πρωινό : Κέικ , Φρυγανιές , Γάλα , Τσάι","Μεσημεριανό: Σουπα του σεφ, χοιρινό ψητό με πουρέ, σουτζουκάκια με πιλάφι , σαλάτα , φρούτο , κομπόστα", "Δείπνο: μελιτζάνες παπουτσάκι ,μακαρόνια με κιμά , σαλάτα , φρούτο , τυρί"],
    "Sunday":["Πρωινό : Κέικ , Φρυγανιές , Γάλα , Τσάι","Μεσημεριανό: Κρεατοσούπα , μοσχάρι γιουβέτσι , μπριζόλα χοιρινή με πατάτες , σαλάτα , φρούτο , ρυζόγαλο", "Δείπνο: χταπόδι κοφτό μακαρονάκι , λουκάνικο με πατάτες , σαλάτα , φρούτο γλυκό"]
}



week4 = {
    "Monday" : ["Πρωινό : Κέικ , Φρυγανιές , Γάλα , Τσάι","Μεσημεριανό: Κολοκυθοπατάτες, Βίδες με σάλτσα Μεσογείου, Φιογκάκια με σάλτσα Αματριτσιάνα, Σαλάτα εποχής, Φρούτο, Γλυκό", "Δείπνο : Κεφτεδάκια κοκκινιστά με πουρέ, Γιουβερλάκια αυγολέμονο, Τυρί, Σαλάτα εποχής, Φρούτο"] ,
    "Tuesday" : ["Πρωινό : Κέικ , Φρυγανιές , Γάλα , Τσάι","Μεσημεριανό: Σούπα του Σεφ, Μπιφτέκι κοτόπουλο με πατάτες, Χοιρινό λεμονάτο με πιλάφι, Σαλάτα εποχής, Φρούτο, Γλυκό","Δείπνο: Κεφτεδάκια κοκκινιστά με πουρέ, Γιουβερλάκια αυγολέμονο, Τυρί, Σαλάτα εποχής, Φρούτο"] , 
    "Wednesday" : ["Πρωινό : Κέικ , Φρυγανιές , Γάλα , Τσάι","Μεσημεριανό: Ντοματόσουπα, Παστίτσιο μανιταριών, Βακαλάος σκορδαλιά, Σαλάτα εποχής, Φρούτο, Γάλα, Λαχανοντολμάδες, Σουφλέ ζυμαρικών με τυριά και αλλαντικά, Σαλάτα εποχής, Γιαούρτι, Φρούτο"] ,
    "Thursday":["Πρωινό: Κέικ , Φρυγανιές , Γάλα , Τσάι","Μεσημεριανό: Κοτόσουπα, Μακαρόνια με Κιμά, Κοτόπουλο με πιλάφι, Σαλάτα εποχής, Φρούτο, Γάλα","Δείπνο : Σουτζουκάκια με πουρέ, Πατάτες ογκρατέν"] ,
    "Friday": ["Πρωινό : Κέικ , Φρυγανιές , Γάλα , Τσάι","Μεσημεριανό: Πουρέ με μπέικον, Ρεβύθια σούπα, Φακές, Σαλάτα εποχής, Γιαούρτι, Φρούτο, Γάλα","Δείπνο :Καλαμαράκια γιαχνί με πιλάφι, Λαζανάκι με σάλτσα ντομάτας και τυρί τριμμένο, Σαλάτα εποχής, Γιαούρτι, Φρούτο"] ,
    "Saturday": ["Πρωινό : Κέικ , Φρυγανιές , Γάλα , Τσάι","Μεσημεριανό: Κρεατόσουπα, Μοσχαράκι λεμονάτο με πιλάφι, Μπριζόλα χοιρινή με πατάτες, Σαλάτα εποχής, Φρούτο, Ρώσικη, Ομελέτα με λαχανικά και τυριά","Δείπνο: Σνίτσελ κοτόπουλο με πουρέ, Σαλάτα εποχής, Φρούτο, Τυρί"] ,
    "Sunday": ["Πρωινό : Κέικ , Φρυγανιές , Γάλα , Τσάι", "Μεσημεριανό: Μινεστόνε, Χοιρινό Κρητικό πιλάφι, Γαλοπούλα με σάλτσα μουστάρδα και πουρέ, Σαλάτα εποχής, Φρούτο, Κρέμα, Πίτσα", "Δείπνο: Λουκάνικο με πατάτες, Σαλάτα εποχής, Φρούτο, Κρέμα"]
}




global week_number




def get_current_day_and_week(arg):
    
    
    global week_number
  
    
    choice = arg
    
    current_date = datetime.now()

    day  = str(current_date.day)
    month = str(current_date.month)
    final = day+"/"+month
    
    day_of_week = current_date.weekday() # Day of week
    
    days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    
  
    

    #Today's food
    
          
    if choice == "today":
        
        
        x = days_of_week[day_of_week]
        
        if week_number == 1:
            return(f"Food for {x} [{final}] : \n\n{week2[x][0]}\n\n{week2[x][1]}\n\n{week2[x][2]}")

        elif week_number == 2:
             return(f"Food for {x} [{final}] : \n\n{week2[x][0]}\n\n{week2[x][1]}\n\n{week2[x][2]}")
            
        elif week_number == 3:
            return(f"Food for {x} [{final}] : \n\n{week2[x][0]}\n\n{week2[x][1]}\n\n{week2[x][2]}")
                     
        else:      
            return(f"Food for {x} [{final}] : \n\n{week2[x][0]}\n\n{week2[x][1]}\n\n{week2[x][2]}")
            
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
    
        
        x = days_of_week[day_of_week]
          
        if week_number == 1:
            return(f"Food for {x} [{final}] : \n\n{week2[x][0]}\n\n{week2[x][1]}\n\n{week2[x][2]}")

        elif week_number == 2:
            return(f"Food for {x} [{final}] : \n\n{week2[x][0]}\n\n{week2[x][1]}\n\n{week2[x][2]}")
       
        elif week_number == 3:
            return(f"Food for {x} [{final}] : \n\n{week2[x][0]}\n\n{week2[x][1]}\n\n{week2[x][2]}")
                     
        else:      
             return(f"Food for {x} [{final}] : \n\n{week2[x][0]}\n\n{week2[x][1]}\n\n{week2[x][2]}")
        
    
    
   
    
    if choice == "open":
           
         
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
            return( "Η σιτίση είναι κλείστη και ανοίγει στις : " + next_opening_time)


    if choice == None:
        return("Invalid arguement")
    
def changeweek(opt):

    global week_number
    
    
    if opt == 0:
        current_date = datetime.now()
        week_number = (current_date.day - 1) // 7 + 1 #Current_week_number
        
        return ("Current week has been reset")
    
    
    if opt <= 4 and opt >= 1 :
        week_number = opt
        return ("Current week has been changed to :"+week_number)
 
