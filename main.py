import flet as ft
import database 

def main(page: ft.Page):
    page.title = 'Cold Store Management System'
    page.window_maximized = True

    def login_click(e):
        password = database.password_verify(phone_number=login_phone_field.value)
        if password and password==login_password_field.value:
            page.go('/home')
        else:
            print('password not correct', password)

    def signup_click(e):
        pass
        
            
        

    login_phone_field = ft.TextField(label='Phone Number')
    login_password_field = ft.TextField(label='Password', password=True, can_reveal_password=True)
    login_login_button = ft.ElevatedButton("Login", bgcolor=ft.colors.RED_400, on_click=login_click)
    login_signup_button = ft.ElevatedButton("Sign Up", on_click=lambda _: page.go("/signup"), bgcolor=ft.colors.RED_ACCENT_400)

    signup_name_field = ft.TextField(label='Name')
    signup_phone_field = ft.TextField(label='Phone Number')
    signup_password_field = ft.TextField(label='Password', password=True, can_reveal_password=True)
    signup_signup_button = ft.ElevatedButton("Sign Up", bgcolor=ft.colors.RED_ACCENT_400)

        
    def route_change(route):
        page.views.clear()
        page.views.append(
            ft.View(
                "/",
                [
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
                ],
            )
        )
        if page.route == "/signup":
            page.views.append(
                ft.View(
                    "/signup",
                    [
                        ft.AppBar(title=ft.Text("Sign Up As A New User"), bgcolor=ft.colors.SURFACE_VARIANT),
                        signup_name_field,
                        signup_phone_field,
                        signup_password_field,
                        signup_signup_button
                    ],
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