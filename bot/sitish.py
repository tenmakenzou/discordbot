import openpyxl
from datetime import datetime, timedelta

def run(day):
    wb = openpyxl.load_workbook('menu.xlsx')
    sheet = wb['Φύλλο1']


    if day == "today":
        target_date = datetime.now()
    elif day == "tomorrow":
        target_date = datetime.now() + timedelta(days=1)
    
    def get_row():
        for row in sheet.iter_rows():
            for cell in row:
                if isinstance(cell.value, datetime):
                    if cell.value.date() == target_date.date():
                        return cell.coordinate  # Example: "C5"
        return None  # In case no matching date is found

    x = get_row()

    if not x:
        return f"No schedule found for {day} ({target_date.date()})"

    if len(x) < 3:  # Handling cases where week numbers are shorter
        x += " "

    lista = [
        'Δευτέρα-Monday', 'Τρίτη-Tuesday', 'Τετάρτη-Wednesday', 'Πέμπτη-Thursday', 'Παρασκευή-Friday',
        'Σάββατο-Saturday', 'Κυριακή-Sunday', None, " ", ""
    ]

    skip_text = ("Γάλα φρέσκο ζεστό ή κρύο, Τσάι σε διάφορες γεύσεις, μαρμελάδες σε διάφορες γεύσεις, Μαργαρίνη, Μέλι, Φρυγανιές σίτου, Ψωμί, Κέικ-         Fresh milk hot or cold, Tea in various flavors, jams in various flavors, Margarine, Honey, Wheat toast, Bread, Cake")

    def get_date(coord):
        count = 0
        result = ""


        col = coord[0]
        row_num = int(coord[1:])


        for i in range(row_num, sheet.max_row + 1):
            cell = sheet[f"{col}{i}"]
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
