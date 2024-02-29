import flet as ft

def main(page: ft.Page):
    page.title = 'Cold Store Management System'
    page.window_maximized = True

    # def login_click(e):
        

    login_phone_field = ft.TextField(label='Phone Number')
    login_password_field = ft.TextField(label='Password', password=True, can_reveal_password=True)
    login_login_button = ft.ElevatedButton("Login", bgcolor=ft.colors.RED_400)
    login_signup_button = ft.ElevatedButton("Sign Up", on_click=lambda _: page.go("/signup"), bgcolor=ft.colors.RED_ACCENT_400)

        
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
                        ft.TextField(label='Name'),
                        ft.TextField(label='Phone Number'),
                        ft.TextField(label='Password', password=True, can_reveal_password=True)
                        # ft.ElevatedButton("Go Home", on_click=lambda _: page.go("/")),
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