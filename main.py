import flet as ft
import database 

def main(page: ft.Page):
    page.title = 'Cold Store Management System'
    page.window_max_height=500
    page.window_max_width=500

    main_color = ft.colors.AMBER_600
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
            database.add_to_inventory(data)
        # except Exception as e:
        #     print(e)
        
    def view_inventory_click(e):
        data = database.extract_inventory()
        page.go('/view')

    login_phone_field = ft.TextField(label='Phone Number', border_color=ft.colors.AMBER_200)
    login_password_field = ft.TextField(label='Password', password=True, can_reveal_password=True, border_color=ft.colors.AMBER_200)
    login_login_button = ft.ElevatedButton("Login", bgcolor=main_color, on_click=login_click, color=ft.colors.BLACK, )
    login_signup_button = ft.ElevatedButton("Sign Up", on_click=lambda _: page.go("/signup"), bgcolor=main_color, color=ft.colors.BLACK)

    signup_name_field = ft.TextField(label='Name', border_color=ft.colors.AMBER_200)
    signup_phone_field = ft.TextField(label='Phone Number', border_color=ft.colors.AMBER_200)
    signup_password_field = ft.TextField(label='Password', password=True, can_reveal_password=True, border_color=ft.colors.AMBER_200)
    signup_signup_button = ft.ElevatedButton("Sign Up", bgcolor=main_color, on_click=signup_click, color='black')

    add_phone_field = ft.TextField(label='Phone Number', read_only=True, border_color=ft.colors.AMBER_200)
    add_potato_variety_radio = ft.RadioGroup(
        ft.Column([
            ft.Radio(value="pukhraj", label="Pukhraj"),
            ft.Radio(value="jyoti", label='Jyoti'),
            ft.Radio(value='seed', label='Seed')
        ])
    )
    add_quantity_field = ft.TextField(label='Quantity', border_color=ft.colors.AMBER_200)

    login_view = [
                    ft.AppBar(title=ft.Text("Welcome to Cold Store Management System", text_align='center', size=24, weight=ft.FontWeight.W_600), bgcolor=main_color, color=ft.colors.BLACK),
                    ft.Row([ft.Text(value='Login', size=40, color=main_color, text_align='center', weight=ft.FontWeight.W_900)], alignment='center'),
                    login_phone_field,
                    login_password_field,
                    ft.Container(
                        ft.Row(
                        [
                    login_login_button,
                    login_signup_button,
                        ], spacing=15, alignment='center', scale=1.3, 
                    ), margin=ft.margin.only(top=20)
                    )
                    
                ]
    signup_view = [
                        ft.AppBar(title=ft.Row([ft.Text("Sign Up As A New User", weight=ft.FontWeight.W_700, color='black', size=24),], alignment='center'), bgcolor=main_color),
                        signup_name_field,
                        signup_phone_field,
                        signup_password_field,
                        ft.Container(
                        ft.Row(
                            [
                        signup_signup_button
                            ], alignment='center',
                        ), margin=ft.margin.only(top=20)
                        )

                    ]
    
    home_view = [
                        ft.AppBar(title=ft.Row([ft.Text("Home Page", size=35, weight=ft.FontWeight.W_600)], alignment='center'), bgcolor=main_color, color='black'),
                        ft.Row([ft.Text('Welcome User', size=30, color=main_color,weight=ft.FontWeight.W_500)], alignment='center'),
                        ft.Container(
                            ft.Column([
                                ft.ElevatedButton(text='Add to Inventory', bgcolor=main_color, on_click=lambda _: page.go('/add'), color='black', scale=1.6),
                                ft.ElevatedButton(text='View Inventory', bgcolor=main_color, on_click=view_inventory_click, color='black', scale=1.6),
                            ], spacing=40), alignment=ft.alignment.center, margin=ft.margin.only(top=80)
                        )

                    ]
    
    add_to_inventory_view = [
        ft.AppBar(title=ft.Row([ft.Text('Add Your Crop To Inventory', color='black', weight=ft.FontWeight.W_600)],alignment='center' ), bgcolor=main_color),
        add_phone_field,
        ft.Text("Select the Variety of Potato"),
        add_potato_variety_radio,
        add_quantity_field,
        ft.Row([
        ft.ElevatedButton(text='Add', on_click=add_inventory_click, bgcolor=main_color, color='black', scale=1.2)
    
        ], alignment='center')
        
    ]

    def route_change(route):
        page.views.clear()
        page.views.append(
            ft.View(
                "/",
                login_view
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
            add_phone_field.value = database.get_current_instance()
            page.views.append(
                ft.View(
                    '/add',
                    add_to_inventory_view
                )
            )
        elif page.route =='/view':
            data = database.extract_inventory()
            page.views.append(
                ft.View(
                    '/view',
                    [
                        ft.AppBar(title=ft.Row([ft.Text('My Inventory', color='black', size=35, weight=ft.FontWeight.W_600)], alignment='center'), bgcolor=main_color, color='black'),
                        ft.Container(
                            ft.Column([ft.Text(f'Phone: {data[0]}', size=25, color=main_color),
                        ft.Text(f'Pukhraj: {data[1]}', size=25, color=main_color),
                        ft.Text(f'Jyoti: {data[2]}', size=25, color=main_color),
                        ft.Text(f'Seed: {data[3]}', size=25, color=main_color)], alignment='center'), alignment=ft.alignment.center, margin=ft.margin.only(top=60)
                        )
]
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