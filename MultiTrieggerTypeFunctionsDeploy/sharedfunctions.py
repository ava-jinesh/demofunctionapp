# Function for setting up a simple logger
def setup_logger(name: str) -> logging.Logger:
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    handler = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    if not logger.handlers:
        logger.addHandler(handler)
    return logger

# Function to format a greeting message
def format_greeting(name: str) -> str:
    return f"Hello, {name}! Welcome to Azure Functions."

# Function to calculate time difference in minutes between two timestamps
def calculate_time_difference(start_time: datetime.datetime, end_time: datetime.datetime) -> float:
    return (end_time - start_time).total_seconds() / 60.0

# Example of using a default parameter
def extract_json_value(data: Dict[str, Any], key: str, default: Optional[str] = None) -> Optional[Any]:
    """Safely extracts a value from a JSON dictionary, returning a default if key is missing."""
    return data.get(key, default)
