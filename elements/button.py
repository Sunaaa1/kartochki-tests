from playwright.sync_api import Page
from elements.base_element import BaseElement
from core.logger import Logger


class Button(BaseElement):
    def __init__(self, page: Page, locator: str, description: str = ""):
        super().__init__(page, locator, description)

    def click(self) -> "Button":
        Logger.info(f"{self._description}: click")
        self.element.click()
        return self

    def is_active(self) -> bool:
        Logger.info(f"{self._description}: check is active")
        return not self.element.is_disabled()