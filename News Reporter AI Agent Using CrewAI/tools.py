## https://serper.dev/

from dotenv import load_dotenv
import os
from crewai_tools import SerperDevTool

# Load environment variables
load_dotenv()

# Check API key
SERPER_API_KEY = os.getenv("SERPER_API_KEY")
if not SERPER_API_KEY:
    raise ValueError("SERPER_API_KEY not found. Add it to your .env file.")

# Initialize the search tool
tool = SerperDevTool()
