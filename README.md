# Instagram Post Viewer

This project is a simple application that randomly selects Instagram posts and displays the corresponding images. The user interface allows for displaying up to three posts at once.

## Project Structure

```
instagram-post-viewer
├── src
│   ├── main.py               # Entry point of the application
│   ├── instagram
│   │   ├── api.py           # Functions to interact with the Instagram API
│   │   ├── post_selector.py  # Class to select random posts
│   │   └── __init__.py      # Marks the instagram directory as a package
│   ├── ui
│   │   ├── interface.py      # Class for rendering the user interface
│   │   └── __init__.py      # Marks the ui directory as a package
│   └── utils
│       ├── helpers.py        # Utility functions for the application
│       └── __init__.py      # Marks the utils directory as a package
├── requirements.txt          # Lists project dependencies
├── .env                      # Environment variables
└── README.md                 # Project documentation
```

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   cd instagram-post-viewer
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   ```

3. Activate the virtual environment:
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```
     source venv/bin/activate
     ```

4. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

5. Set up your environment variables in the `.env` file.

## Usage

To run the application, execute the following command:
```
python src/main.py
```

This will initialize the application and display random Instagram posts in the user interface.

## Contributing

Feel free to submit issues or pull requests for improvements or bug fixes.