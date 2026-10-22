import re
from playwright.sync_api import Page, expect

def test_navigate_to_home_board(page: Page):
    # 1. Navigate to the website home board
    page.goto("https://wynnalmarjanisland.com/")
    
    # 2. Verify that the page title contains "Wynn" using a regex pattern
    expect(page).to_have_title(re.compile("Wynn"))

import re
from playwright.sync_api import Page, expect

def test_navigate_to_home_board(page: Page):
    # 1. Navigate to the website home board
    page.goto("https://wynnalmarjanisland.com/")
    
    # 2. Verify home page title
    expect(page).to_have_title(re.compile("Wynn"))

    # 3. Click "Allow All" on the cookie banner (using ID or role)
    # Option A: By element ID (from your screenshot)
    page.locator("#onetrust-accept-btn-handler").click()
    
    # Alternatively, Option B using accessible role:
    # page.get_by_role("button", name="Allow All").click()

    # 4. Click the "ROOMS & SUITES" navigation link
    page.get_by_role("link", name="Rooms & Suites").click()

    # 5. Assert navigation to rooms-and-suites URL
    expect(page).to_have_url("https://wynnalmarjanisland.com/rooms-and-suites")


import re
from playwright.sync_api import Page, expect

def test_navigate_to_home_board(page: Page):
    # 1. Navigate to the website home board
    page.goto("https://wynnalmarjanisland.com/")
    
    # 2. Verify that the home page title contains "Wynn"
    expect(page).to_have_title(re.compile("Wynn"))

    # 3. Click the "ROOMS & SUITES" navigation link
    page.get_by_role("link", name="Rooms & Suites").click()

    # 4. Assert that the URL matches https://wynnalmarjanisland.com/rooms-and-suites
    expect(page).to_have_url("https://wynnalmarjanisland.com/rooms-and-suites")
