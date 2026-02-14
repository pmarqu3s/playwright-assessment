from pathlib import Path
from pages.landing_page import LandingPage
from pages.login_page import LoginPage
AUTH_STATE = Path(".auth/state.json")

# Purpose:
# - Run once (headed) to complete "new device" verification manually.
# - After device is approved finish the logout flow.
# - This test exports the browser context storage state (cookies/localStorage/IndexedDB) 
#   to .auth/state.json so other tests can reuse the same authenticated session
#
# How to run:
#   pytest --headed tests/save_state.py
#
# Manual steps when the test pauses:
# - Approve the device via the email prompt.
# - Log out
# - Click "Resume" in Playwright Inspector to let the test export the state.

def test_login(page, login_username, login_password):
    landing = LandingPage(page)
    login = LoginPage(page)
    landing.open()
    landing.click_login()
    login.login(login_username, login_password)
    
    page.pause()
    
    # Saves Sate after device approval and logout
    AUTH_STATE.parent.mkdir(parents=True, exist_ok=True)
    # Exports state.json
    page.context.storage_state(path=str(AUTH_STATE))  
