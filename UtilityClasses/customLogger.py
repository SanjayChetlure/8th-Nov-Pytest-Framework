import logging
from datetime import datetime

class LogGen:

   @staticmethod
   def loggen():
       # Generate filename with current date & time -> convert to string
       current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
       log_filename = f".\\Logs\\SwagLabLogs{current_time}.log"
        #The f stands for formatted string literal (also called an f-string)

       logging.basicConfig(filename=log_filename,
                           format='%(asctime)s: %(levelname)s: %(message)s',
                           datefmt="%Y-%m-%d %H:%M:%S",
                           force=True)

       logger=logging.getLogger()
       logger.setLevel(logging.INFO)
       return logger
