from playwright.sync_api import Page


class ReservePage:

    def __init__(self, page: Page) -> None:
        self.page = page
        self.flight_43 = page.get_by_role(
            "row", name="Choose This Flight 43 Virgin"
        ).get_by_role("button")

    def reserve_flight(self) -> None:
        self.flight_43.click()
