from playwright.sync_api import Page, Locator
from core.logger import Logger


class BaseElement:
    def __init__(self, page: Page, locator: str, description: str = ""):
        self._page = page
        self._locator = locator
        self._description = description

    @property
    def element(self) -> Locator:
        return self._page.locator(self._locator)

    def is_visible(self) -> bool:
        Logger.info(f"{self._description}: check is visible")
        return self.element.is_visible()

    def is_enabled(self) -> bool:
        Logger.info(f"{self._description}: check is enabled")
        return self.element.is_enabled()

    def wait_for_visible(self) -> "BaseElement":
        Logger.info(f"{self._description}: wait for visible")
        self.element.wait_for(state="visible")
        return self

    def wait_for_hidden(self) -> "BaseElement":
        Logger.info(f"{self._description}: wait for hidden")
        self.element.wait_for(state="hidden")
        return self

    def get_text(self) -> str:
        Logger.info(f"{self._description}: get text")
        return self.element.inner_text()

    def get_attribute(self, attribute: str) -> str:
        Logger.info(f"{self._description}: get attribute '{attribute}'")
        return self.element.get_attribute(attribute)

    def wait_for(self, state: str = "visible") -> "BaseElement":
        Logger.info(f"{self._description}: wait for state '{state}'")
        self.element.wait_for(state=state)
        return self

    def __str__(self) -> str:
        return f"{self.__class__.__name__}[{self._locator}] — {self._description}"