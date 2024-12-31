Web Automation Framework
📋 Project Overview
This project is a web automation framework built using Python, Playwright, and Pytest. The framework is designed to automate and test web application workflows, including user creation and class booking processes.

📂 Project Structure
data/: Stores test data (JSON and CSV).
page_objects/: Contains page-specific interactions using the Page Object Model (POM).
tests/: Includes test scripts for different functionalities.
reports/: Generated HTML reports of test results.
requirements.txt: Lists required dependencies.
pytest.ini: Configuration file for Pytest.


⚙️ Setup
1.Install dependencies:
pip install -r requirements.txt

2.Install Playwright browsers:
playwright install


Here’s a simplified version of the README.md:

Web Automation Framework
📋 Overview
This is a web automation framework built with Python, Playwright, and Pytest. It automates workflows like user creation and class booking for web applications.

📂 Project Structure
data/: Stores test data (JSON and CSV).
page_objects/: Contains page-specific interactions using the Page Object Model (POM).
tests/: Includes test scripts for different functionalities.
reports/: Generated HTML reports of test results.
requirements.txt: Lists required dependencies.
pytest.ini: Configuration file for Pytest.
⚙️ Setup
Install dependencies:

pip install -r requirements.txt
Install Playwright browsers:

🚀 How to Run Tests

Run all tests:
pytest

Run specific test:
pytest tests/test_user_creation.py

Generate HTML report:
pytest --html=reports/test_report.html

🧾 Features
Page Object Model for better maintainability.
Data-Driven Testing with JSON and CSV files.
HTML Test Reports for execution results.






