import logging
from datetime import datetime
import os

log_dir="housing_logs"

time=f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}"

log_file=f"logs_{time}.log"

os.makedirs(log_dir,exist_ok=True)

log_file_path=os.path.join(log_dir,log_file)


logging.basicConfig(filename=log_file_path,
filemode="w",
format='[%(asctime)s] %(name)s - %(levelname)s -  %(message)s',
level=logging.INFO
)