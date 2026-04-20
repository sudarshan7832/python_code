import logging
from selenium import webdriver

# Configure logging (show all levels)
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)


def launch_browser():
    logging.debug("Debug: Starting browser setup")

    try:
        logging.info("Info: Launching Chrome browser")

        driver = webdriver.Chrome()

        logging.warning("Warning: Browser launched, ensure driver version is correct")

        driver.get("https://www.google.com")
        logging.info("Info: Opened Google website")

        logging.debug("Debug: Maximizing window")
        driver.maximize_window()

        logging.info("Info: Browser actions completed successfully")

        driver.quit()
        logging.info("Info: Browser closed")

    except Exception as e:
        logging.error(f"Error: {e}")
        logging.critical("Critical: Browser launch failed")


launch_browser()