# TODO: Make this into a class
DEBUG = False 


def debug_log(message: str) -> None:
    """Log debug message"""
    if DEBUG == True:
        print("Debug: " + message)
