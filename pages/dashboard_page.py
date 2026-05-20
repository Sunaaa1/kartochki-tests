from playwright.sync_api import Page
from pages.base_page import BasePage
from elements.label import Label
from core.logger import Logger


class DashboardPage(BasePage):
    UNIQUE_ELEMENT_LOC = "//p[text()='Обзор работы за сегодня']"

    def __init__(self, page: Page):
        super().__init__(page)

        self.unique_element = Label(
            page,
            self.UNIQUE_ELEMENT_LOC,
            description="Dashboard page -> Unique element"
        )

    def is_open(self) -> bool:
        return self.unique_element.is_visible()