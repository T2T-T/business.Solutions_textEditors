# Install Playwright first:
# pip install playwright
# playwright install

from playwright.sync_api import sync_playwright
import time

with sync_playwright() as p:
    # Launch browser
    browser = p.chromium.launch(headless=False)

    # Create page
    page = browser.new_page()

    # 1) Go to the link
    page.goto("https://www.pokemon.com/us", wait_until="domcontentloaded")

    # 2) Wait 2 seconds for page to load
    time.sleep(2)

    # 3) Hover over the “Pokedex” link in the Navigation Bar
    page.hover("text=Pokedex")

    # 4) Click on “Pokedex Hot List”
    page.click("text=Pokedex Hot List")

    # Wait for page to load
    page.wait_for_load_state("domcontentloaded")

    # Hover over white search bar under name and number
    search_box = page.locator(
        'input[type="search"], input[placeholder*="Name"], #searchInput'
    )

    search_box.hover()

    # Type "Rayquaza"
    search_box.fill("Rayquaza")

    # Click on "Rayquaza"
    page.click("text=Rayquaza")

    # Wait 2 seconds
    time.sleep(2)

    # 5) On the "Rayquaza" page, click "Rayquaza"
    page.click("text=Rayquaza")

    # Click "Mega Rayquaza"
    page.click("text=Mega Rayquaza")

    # Wait 2 seconds
    time.sleep(2)

    # 6) Wait 5 seconds
    time.sleep(5)

    # Close browser
    browser.close()