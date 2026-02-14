import re
from playwright.sync_api import expect
from pages import LandingPage

def test_open_landing_page(page, base_url):
    landing = LandingPage(page)
    landing.open()
    
    # Assert URL is correct
    expect(page).to_have_url(re.compile(rf"^{re.escape(base_url)}.*"))
