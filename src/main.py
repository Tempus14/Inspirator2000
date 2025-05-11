import os
from dotenv import load_dotenv
from ui.interface import UserInterface

def main():
    # Load environment variables from .env file
    load_dotenv()

    # Get the image folder path from the environment variable
    folder = os.getenv("IMAGE_FOLDER_PATH")
    if not folder:
        print("Error: IMAGE_FOLDER_PATH is not set in the .env file.")
        return

    # Initialize and run the user interface
    ui = UserInterface(folder)
    ui.run()

if __name__ == "__main__":
    main()