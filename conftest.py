import os, re, pytest, yaml
from dotenv import load_dotenv
from pathlib import Path

load_dotenv()

AUTH_STATE = Path(".auth/state.json")
CONFIG_PATH = Path("config.yaml")

@pytest.fixture(scope="session")
def config():
    if not CONFIG_PATH.exists():
        return {}
    return yaml.safe_load(CONFIG_PATH.read_text(encoding="utf-8")) or {}

@pytest.fixture(scope="session")
def base_url(config):
    return (config.get("app") or {}).get("base_url") or os.environ["BASE_URL"]

@pytest.fixture(scope="session")
def login_domain(config):
    return (config.get("app") or {}).get("auth_domain") or os.environ["LOGIN_DOMAIN"]

@pytest.fixture(scope="session")
def login_username(config):
    return (config.get("account") or {}).get("username") or os.environ["LOGIN_USERNAME"]

@pytest.fixture(scope="session")
def login_password() -> str:
    return os.environ["LOGIN_PASSWORD"]

@pytest.fixture(scope="session")
def totp_secret() -> str:
    raw = os.environ["TOTP_SECRET"]

    # Remove whitespace + dashes, uppercase
    secret = re.sub(r"[\s-]+", "", raw).upper()

    if not re.fullmatch(r"[A-Z2-7]+=*", secret):
        raise ValueError(f"Invalid base32 TOTP_SECRET: {raw!r} -> {secret!r}")

    return secret

@pytest.fixture(scope="session")
def browser_context_args(browser_context_args, base_url):
    args = {**browser_context_args, "base_url": base_url}
    if AUTH_STATE.exists():
        args["storage_state"] = str(AUTH_STATE)
    return args
