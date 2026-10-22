import re

from playwright.sync_api import Page, TimeoutError as PlaywrightTimeoutError, expect

HOME_URL = "https://wynnalmarjanisland.com/"
ROOMS_URL = "https://wynnalmarjanisland.com/rooms-and-suites"


def _dismiss_cookie_banner_if_present(page: Page) -> None:
    accept = page.locator("#onetrust-accept-btn-handler")
    try:
        accept.wait_for(state="visible", timeout=5000)
    except PlaywrightTimeoutError:
        return
    accept.click()


def test_home_page_title(page: Page):
    page.goto(HOME_URL)
    expect(page).to_have_title(re.compile("Wynn"))


def test_navigate_to_home_board(page: Page):
    page.goto(HOME_URL)
    expect(page).to_have_title(re.compile("Wynn"))

    _dismiss_cookie_banner_if_present(page)

    page.get_by_role("link", name="Rooms & Suites").click()
    expect(page).to_have_url(ROOMS_URL)
