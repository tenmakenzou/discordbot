import openpyxl
from datetime import datetime


def run():

    wb = openpyxl.load_workbook('menu.xlsx')
    sheet = wb['Φύλλο1'] 

    target_date = datetime.now()  # datetime of the current day
    def get_row():
        for row in sheet.iter_rows():
            for cell in row:
                if isinstance(cell.value, datetime):  
                    if cell.value.date() == target_date.date():  
                     
                        return cell.coordinate

    x = get_row()
    
    lista = ['Δευτέρα-Monday','Τρίτη-Tuesday','Τετάρτη-Wednesday','Πέμπτη-Thursday','Παρασκευή-Friday','Σάββατο-Saturday','Κυριακή-Sunday',None," ",""] # list of objects to avoid printing


    def get_date(x):
        count = 0
        result = ""  
        
        for cell in sheet[x[0]][int(x[1]+x[2]):]: #column[x[0]] and column number x[1],[2]
            if not isinstance(cell.value, datetime) and cell.value not in lista:
               if count == 0:
                                        
                    result += "\n***Πρωινό***\n"  
                    result += '- Γάλα φρέσκο ζεστό ή κρύο, Τσάι σε διάφορες γεύσεις, μαρμελάδες σε διάφορες γεύσεις, Μαργαρίνη, Μέλι, Φρυγανιές σίτου, Ψωμί, Κέικ-Fresh milk hot or cold, Tea in various flavors, jams in various flavors, Margarine, Honey, Wheat toast, Bread, Cake\n'
                    result += "\n***Μεσημεριανό***\n"  
                                    
               if count == 3:
                    result += "\n***Δείπνο***\n"  
                                    
               result += f"- {cell.value}\n"  
               count += 1
               if count == 5:
                  break
        
        return result  


    return get_date(x)
