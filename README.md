# UI tests (Playwright + Pytest)

End-to-end UI tests using Playwright (Python) with Pytest.

## Prerequisites
- Python 3.8+ installed.
- Create and use a virtual environment.
- Account created with 2FA (TOTP SECRET is required)

## Project setup (first time)

### 1) Create and activate a virtual environment
#### macOS / Linux:
python -m venv .venv
source .venv/bin/activate

#### Windows (PowerShell):
python -m venv .venv
.\.venv\Scripts\Activate.ps1

### 2) Install Python packages
python -m pip install --upgrade pip
pip install -r requirements-dev.txt

### 3) Install Playwright browsers
playwright install

### 4) Copy YAML config and edit it
cp config.example.yaml config.yaml

### 5) Create a .env file with secrets
LOGIN_PASSWORD=...
TOTP_SECRET=...

## Important: first run (auth state)
Production environment may treat Playwright runs as a new device and trigger device verification.
To reduce repeated verification prompts, run the state setup test first in headed mode:

pytest -v --headed tests/save_state.py

When the test pauses:
1) Open the verification email and approve the new device.
2) Log out.
3) Resume/finish the test by clicking "Play" in the Playwright inspector.

## Running tests
### Headless
pytest tests/test*.py 

### Headed
pytest --headed tests/test*.py

## Limitations / Improvements
### Limitations
Headless mode may be blocked by Cloudflare “Verify you are human” challenges in production,
so it may fail before reaching the application UI. By default firefox is the browser selected because
headless works with it.

### Improvements
1) Locators could be improved
2) Figure out a solution to chromium headless mode limitation
3) Report
4) Make the 2FA requirement optional. However flow is not always the same in this case
5) Add retries for CI/CD. Sometimes the page does not fully load, which requires a refresh
