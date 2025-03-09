import openpyxl
from datetime import datetime

def run():
    wb = openpyxl.load_workbook('menu.xlsx')
    sheet = wb['Φύλλο1']

    target_date = datetime.now()  # Current date

    def get_row():
        for row in sheet.iter_rows():
            for cell in row:
                if isinstance(cell.value, datetime):
                    if cell.value.date() == target_date.date():
                        return cell.coordinate  # Example: "C5"

    x = get_row()

    if len(x) < 3:  # Handling cases where week numbers are shorter
        x += " "

    lista = [
        'Δευτέρα-Monday', 'Τρίτη-Tuesday', 'Τετάρτη-Wednesday', 'Πέμπτη-Thursday', 'Παρασκευή-Friday',
        'Σάββατο-Saturday', 'Κυριακή-Sunday', None, " ", ""
    ]

    skip_text = ("Γάλα φρέσκο ζεστό ή κρύο, Τσάι σε διάφορες γεύσεις, μαρμελάδες σε διάφορες γεύσεις, Μαργαρίνη, Μέλι, Φρυγανιές σίτου, Ψωμί, Κέικ-         Fresh milk hot or cold, Tea in various flavors, jams in various flavors, Margarine, Honey, Wheat toast, Bread, Cake")

    def get_date(x):
        count = 0
        result = ""

        for cell in sheet[x[0]][int(x[1] + x[2]):]:  # Extract meal details
            if not isinstance(cell.value, datetime) and cell.value not in lista and cell.value != skip_text:
                if count == 0:
                    result += '\n***Πρωινό***\n- ' + skip_text + '\n\n***Μεσημεριανό***\n'

                if count == 3:
                    result += "\n***Δείπνο***\n"

                result += f"- {cell.value}\n"
                count += 1

                if count == 5:
                    break

        return result.strip()
    
    return get_date(x)
