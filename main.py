import flet as ft
import database 

def main(page: ft.Page):
    page.title = 'Cold Store Management System'
    # page.window_maximized = True
    page.window_max_height=600
    page.window_max_width=600

    def login_click(e):
        password = database.password_verify(phone_number=login_phone_field.value)
        if password and password==login_password_field.value:
            database.update_current_instance(login_phone_field.value)
            page.go('/home')
        else:
            print('password not correct', password)

    def signup_click(e):
        try:
            database.add_user([signup_phone_field.value, signup_name_field.value, signup_password_field.value, 0])
            print('data added')
            page.go('/home')
        except Exception as e:
            print(e)

    def add_inventory_click(e):
        # try:
            variety = add_potato_variety_radio.value
            quantity = add_quantity_field.value
            data = [add_phone_field.value]
            if variety=='pukhraj':
                data.extend([quantity, 0, 0])
            elif variety=='jyoti':
                data.extend([0, quantity, 0])
            else:
                data.extend([0, 0, quantity])
            print(data)
            database.add_to_inventory(data)
        # except Exception as e:
        #     print(e)
        

    login_phone_field = ft.TextField(label='Phone Number')
    login_password_field = ft.TextField(label='Password', password=True, can_reveal_password=True)
    login_login_button = ft.ElevatedButton("Login", bgcolor=ft.colors.RED_400, on_click=login_click)
    login_signup_button = ft.ElevatedButton("Sign Up", on_click=lambda _: page.go("/signup"), bgcolor=ft.colors.RED_ACCENT_400)

    signup_name_field = ft.TextField(label='Name')
    signup_phone_field = ft.TextField(label='Phone Number')
    signup_password_field = ft.TextField(label='Password', password=True, can_reveal_password=True)
    signup_signup_button = ft.ElevatedButton("Sign Up", bgcolor=ft.colors.RED_ACCENT_400, on_click=signup_click)

    add_phone_field = ft.TextField(label='Phone Number', read_only=True)
    add_potato_variety_radio = ft.RadioGroup(
        ft.Column([
            ft.Radio(value="pukhraj", label="Pukhraj"),
            ft.Radio(value="jyoti", label='Jyoti'),
            ft.Radio(value='seed', label='Seed')
        ])
    )
    add_quantity_field = ft.TextField(label='Quantity')

    login_view = [
                    ft.AppBar(title=ft.Text("Welcome to Cold Store Management System"), bgcolor=ft.colors.SURFACE_VARIANT),
                    ft.Text(value='Login'),
                    login_phone_field,
                    login_password_field,
                    ft.Row(
                        [
                    login_login_button,
                    login_signup_button,
                        ]
                    )
                ]
    signup_view = [
                        ft.AppBar(title=ft.Text("Sign Up As A New User"), bgcolor=ft.colors.SURFACE_VARIANT),
                        signup_name_field,
                        signup_phone_field,
                        signup_password_field,
                        signup_signup_button
                    ]
    
    home_view = [
                        ft.AppBar(title=ft.Text("Home Page"), bgcolor=ft.colors.SURFACE_VARIANT),
                        ft.Text('Welcome user', size=30),
                        ft.ElevatedButton(text='Add to Inventory', bgcolor=ft.colors.BLUE_500, on_click=lambda _: page.go('/add'))
                    ]
    
    add_to_inventory_view = [
        ft.AppBar(title=ft.Text('Add Your Crop To Inventory'), bgcolor=ft.colors.SURFACE_VARIANT),
        add_phone_field,
        ft.Text("Select the Variety of Potato"),
        add_potato_variety_radio,
        add_quantity_field,
        ft.ElevatedButton(text='Add', on_click=add_inventory_click)
        
    ]

    def route_change(route):
        page.views.clear()
        page.views.append(
            ft.View(
                "/",
                # home_view
                login_view
                # add_to_inventory_view
            )
        )
        if page.route == "/signup":
            page.views.append(
                ft.View(
                    "/signup",
                    signup_view
                )
            )
        elif page.route == '/home':
            page.views.append(
                ft.View(
                    '/home',
                    home_view
                )
            )
        elif page.route == '/add':
            # print(page.session.get('id'))
            add_phone_field.value = database.get_current_instance()
            page.views.append(
                ft.View(
                    '/add',
                    add_to_inventory_view
                )
            )
        
        page.update()

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)


ft.app(target=main)