import re
from playwright.sync_api import expect
from pages import LandingPage, LoginPage


def test_open_login_page(page, login_domain):
    landing = LandingPage(page)

    landing.open()
    landing.click_login()

    # Asserts Login Domain is present in the URL
    expect(page).to_have_url(re.compile(".*" + re.escape(login_domain) + ".*")) 

def test_login(page, login_username, login_password, totp_secret):
    landing = LandingPage(page)
    login = LoginPage(page)

    landing.open()
    landing.click_login()
    login.login(login_username, login_password, totp_secret)
    
    # Asserts Profile Avatar is visible
    expect(landing.avatar_icon).to_be_visible()
    # Asserts Portfolio value is zero
    expect(landing.portfolio_value).to_have_text(re.compile(r"^\s*0([.,]00)?\s*$"))
