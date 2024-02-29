import gspread

gc = gspread.service_account(filename='credentials.json')

csms_sheet = gc.open('CSMS')
users_sheet = csms_sheet.worksheet('users')

def add_user(data:list):
    users_sheet.append_row(data)

def password_verify(phone_number):
    row =  users_sheet.find(str(phone_number)).row
    if row:
        password = users_sheet.cell(row, col=3).value
        return password
    return None
# print(password_verify(97815))