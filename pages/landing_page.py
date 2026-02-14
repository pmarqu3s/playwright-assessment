import re
from playwright.sync_api import Page


class LandingPage:
    # --- Locators ---
    def __init__(self, page: Page):
        self.page = page
        self.login_button = page.get_by_role("link",name=re.compile(r"^log\s*in$", re.IGNORECASE),)
        self.portfolio_value = page.locator("[data-testid='portfolio-value'] span[role='status']")
        self.avatar_icon = page.locator("[class*='Avatar-module_container']")

    # --- Actions / Methods ---
    def open(self) -> None:
        self.page.goto("/", wait_until="domcontentloaded")
        self.page.wait_for_load_state("load")

    def click_login(self) -> None:
        self.login_button.click()
