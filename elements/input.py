from playwright.sync_api import Page
from elements.base_element import BaseElement
from core.logger import Logger


class Input(BaseElement):
    def __init__(self, page: Page, locator: str, description: str = ""):
        super().__init__(page, locator, description)

    def fill(self, text: str) -> "Input":
        Logger.info(f"{self._description}: fill '{text}'")
        self.element.fill(text)
        return self

    def clear(self) -> "Input":
        Logger.info(f"{self._description}: clear")
        self.element.clear()
        return self

    def get_value(self) -> str:
        Logger.info(f"{self._description}: get value")
        return self.element.input_value()