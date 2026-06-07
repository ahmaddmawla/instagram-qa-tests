from playwright.sync_api import Page

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.url = "https://the-internet.herokuapp.com/login"
        self.username_field = "#username"
        self.password_field = "#password"
        self.login_button = "button[type='submit']"
        self.success_message = ".flash.success"
        self.error_message = ".flash.error"
    
    def go_to(self):
        self.page.goto(self.url)
    
    def login(self, username, password):
        self.page.fill(self.username_field, username)
        self.page.fill(self.password_field, password)
        self.page.click(self.login_button)