import shutil
import os
from dotenv import load_dotenv

load_dotenv()

FILENAME = os.getenv('API_TARGET_FILENAME')
DESTINATION = os.getenv('API_TARGET_DESTINATION')

FILENAMEPUB = os.getenv('API_TARGET_FILENAME_PUB')
DESTINATIONPUB = os.getenv('API_TARGET_DESTINATION_PUB')

shutil.copy2(FILENAME, DESTINATION)
shutil.copy2(FILENAMEPUB, DESTINATIONPUB)
