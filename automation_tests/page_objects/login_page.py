from playwright.sync_api import sync_playwright

def login(page, username: str, password: str):
    """Reusable login function"""
    page.goto("https://example.com/login")
    page.fill("input[name='username']", username)
    page.fill("input[name='password']", password)
    page.click("button[type='submit']")
    page.wait_for_url("**/dashboard")   # wait until redirected
    print("✅ Login successful")

def run_test():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # set True for CI
        page = browser.new_page()

        # Call the reusable function
        login(page, "testuser", "secret123")

        # Do something after login
        page.click("text=Profile")
        page.screenshot(path="profile.png")

        browser.close()

if __name__ == "__main__":
    run_test()
