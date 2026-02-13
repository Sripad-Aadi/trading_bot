import logging
import os

def setup_logger(log_file="logs/app.log"):

    os.makedirs("logs", exist_ok=True)
    
    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )
    
    #file handler
    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(formatter)
    
    #console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(formatter)
    
    #root logger
    root = logging.getLogger()
    root.setLevel(logging.INFO)
    
    #add handlers and avoid duplicates
    if not any(isinstance(h, logging.FileHandler) for h in root.handlers):
        root.addHandler(file_handler)
    if not any(isinstance(h, logging.StreamHandler) and h != console_handler for h in root.handlers):
        root.addHandler(console_handler)
