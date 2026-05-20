import json
import os

DEFAULT_PATH = "configs/config.json"


class Config:
    def __init__(self, path=DEFAULT_PATH):
        # Загружаем .env только если файл существует (локальная разработка)
        if os.path.exists(".env"):
            from dotenv import load_dotenv
            load_dotenv()

        with open(path, "r", encoding="utf-8") as f:
            self._config = json.load(f)

    @property
    def base_url(self) -> str:
        value = os.getenv("BASE_URL") or self._config.get("base_url")
        return value

    @property
    def api_url(self) -> str:
        return os.getenv("API_URL") or self._config.get("api_url")

    @property
    def timeout(self) -> int:
        return self._config.get("timeout", 60000)

    @property
    def test_user_email(self) -> str:
        return os.getenv("TEST_USER_EMAIL")

    @property
    def test_user_password(self) -> str:
        return os.getenv("TEST_USER_PASSWORD")

    @property
    def headless(self) -> bool:
        return os.getenv("HEADLESS", "false").lower() == "true"


config = Config()