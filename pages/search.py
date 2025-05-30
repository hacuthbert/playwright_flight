from playwright.sync_api import Page


class SearchPage:

    def __init__(self, page: Page) -> None:
        self.page = page
        self.departure_city = page.locator('select[name="fromPort"]')
        self.destination_city = page.locator('select[name="toPort"]')
        self.search_button = page.get_by_role("button", name="Find Flights")

    def load(self, URL: str) -> None:
        self.page.goto(URL)

    def search(self, departure_city: str, destination_city: str) -> None:
        self.departure_city.select_option(departure_city)
        self.destination_city.select_option(destination_city)
        self.search_button.click()
