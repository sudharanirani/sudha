from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)  # Opens browser visibly
    page = browser.new_page()
    
    # 1. Open website
    page.goto("https://exabeam.admin.com")
    
    # 2. Print page title
    print(page.title())
    
    browser.close()
