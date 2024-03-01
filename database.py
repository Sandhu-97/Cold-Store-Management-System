import gspread

gc = gspread.service_account(filename='credentials.json')

csms_sheet = gc.open('CSMS')
users_sheet = csms_sheet.worksheet('users')
inventory_sheet = csms_sheet.worksheet('inventory')


def add_to_inventory(data:list):
    # try:
        if data[0] not in inventory_sheet.col_values(1):
            inventory_sheet.append_row(data)
        else:
            row = inventory_sheet.find(data[0], in_column=1).row
            col=2
            while col<=4:
                value = int(inventory_sheet.cell(row, col).value)
                value += int(data[col-1])
                inventory_sheet.update_cell(row, col, value)
                print(value)
                col+=1

    # except Exception as e:
    #     print(e) 

def add_user(data:list):
    try:
        users_sheet.append_row(data)
    except Exception as e:
        print(e)

def password_verify(phone_number):
    row =  users_sheet.find(str(phone_number), in_column=1).row
    if row:
        password = users_sheet.cell(row, col=3).value
        return password
    return None

def get_current_instance():
    return users_sheet.acell('H1').value

def update_current_instance(phone_number):
    # users_sheet.acell('H1').value = phone_number   
    users_sheet.update('H1', phone_number)
    print('instance updated', phone_number)
