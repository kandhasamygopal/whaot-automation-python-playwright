from playwright.sync_api import sync_playwright

def test_example():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto("https://example.com")
        
        # Test interactions
        page.click("button")
        page.fill("input", "test data")
        assert page.text_content("h1") == "Expected Title"
        
        browser.close()
