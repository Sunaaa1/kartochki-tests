from playwright.sync_api import Page
from elements.base_element import BaseElement
from core.logger import Logger


class Label(BaseElement):
    def __init__(self, page: Page, locator: str, description: str = ""):
        super().__init__(page, locator, description)

    def get_text(self) -> str:
        Logger.info(f"{self._description}: get text")
        return self.element.inner_text()

    def wait_for_text(self, text: str) -> "Label":
        Logger.info(f"{self._description}: wait for text '{text}'")
        self.element.filter(has_text=text).wait_for(state="visible")
        return self