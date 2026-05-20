from playwright.sync_api import Page
from core.logger import Logger


class BasePage:
    def __init__(self, page: Page):
        self._page = page

    def navigate(self, path: str = "") -> None:
        url = f"/{path}" if path else "/"
        Logger.info(f"{self.__class__.__name__}: navigate to '{url}'")
        self._page.goto(url)

    def get_title(self) -> str:
        return self._page.title()

    def get_current_url(self) -> str:
        return self._page.url

    def wait_for_url(self, pattern: str) -> None:
        Logger.info(f"{self.__class__.__name__}: wait for url '{pattern}'")
        self._page.wait_for_url(f"**{pattern}**")

    def take_screenshot(self, name: str) -> None:
        path = f"logs/{name}.png"
        self._page.screenshot(path=path)
        Logger.info(f"{self.__class__.__name__}: screenshot saved to '{path}'")