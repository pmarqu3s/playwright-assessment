import pyotp
from playwright.sync_api import Page


class LoginPage:
    # --- Locators ---
    def __init__(self, page: Page):
        self.page = page
        self.email_input = page.locator("input[name='username']")
        self.password_input = page.locator("input[name='password']")
        self.continue_button = page.locator("button[type='submit']")
        self.tfa_input = page.locator("input[name='tfa']")
        self.enter_button = page.locator("[data-testid='TwoFactorAuthentication'] button")

    # --- Actions / Methods ----
    def fill_email(self, email: str) -> None:
        self.email_input.fill(email)

    def fill_password(self, password: str) -> None:
        self.password_input.fill(password)

    def submit(self) -> None:
        self.continue_button.click()

    def authenticate_2fa(self, totp_secret: str) -> None:
        self.tfa_input.wait_for()
        code = pyotp.TOTP(totp_secret, digits=6, interval=30).now()
        self.tfa_input.fill(code)
        self.enter_button.click()

    def login(self, email: str, password: str, totp_secret: str) -> None:
        self.fill_email(email)
        self.fill_password(password)
        self.submit()
        self.authenticate_2fa(totp_secret)
