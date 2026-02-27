from datetime import datetime

class ScreenshotUtility:


   @staticmethod
   def captureSS(driver, test_name):
       # Current date & time
       current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

       # Screenshot file name
       screenshot_path = f".\\Screenshots\\{test_name}_{current_time}.png"

       driver.save_screenshot(screenshot_path)
