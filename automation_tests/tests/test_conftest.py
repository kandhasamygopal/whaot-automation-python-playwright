
from playwright.sync_api import sync_playwright
import pytest
import os
from weasyprint import HTML


@pytest.fixture(scope="automation_tests")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()

@pytest.fixture(scope="automation_tests")
def page(browser):
    page = browser.new_page()
    yield page
    page.close()


    # Hook to generate PDF from HTML report
def pytest_sessionfinish(session, exitstatus):
    """Hook to convert the HTML report to PDF after the pytest session."""
    html_report_path = "reports/test_report.html"  # Path to the HTML report
    pdf_report_path = "reports/test_report.pdf"    # Path to save the PDF report

    if os.path.exists(html_report_path):
        try:
            print("Converting HTML report to PDF...")
            HTML(html_report_path).write_pdf(pdf_report_path)
            print(f"PDF report generated successfully: {pdf_report_path}")
        except Exception as e:
            print(f"Failed to generate PDF report: {e}")
    else:
        print(f"HTML report not found at {html_report_path}")
