# Inspirator2000

This project is a simple application that randomly selects saved Instagram posts and displays the corresponding images. Images have to be categorised beforehand by rating.
<br/>
For downloading Instagram posts see: https://github.com/instaloader/instaloader <br/>
For rating the images I recommend the free version of Narrative Select: https://narrative.so/ <br/>
For python package management I recommend conda: https://www.anaconda.com/docs/getting-started/miniconda/install

## Project Structure

```
Inspirator2000
├── src
│   ├── main.py               # Entry point of the application
│   ├── instagram
│   │   ├── post_selector.py  # Class to select random posts from the folder
│   │   └── __init__.py      # Marks the instagram directory as a package
│   ├── ui
│   │   ├── interface.py      # Class for rendering the user interface
│   │   └── __init__.py      # Marks the ui directory as a package
│   └── utils
│       ├── helpers.py        # Utility functions for the application
│       ├── xmp_utils.py        # Utility functions for the metadata
│       └── __init__.py      # Marks the utils directory as a package
├── requirements.txt          # Lists project dependencies
├── .env                      # Environment variables
└── README.md                 # Project documentation
```

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   cd Inspirator2000
   ```

2. Create a virtual environment using conda:
   ```
   conda create -n insta
   ```

3. Activate the virtual environment:
   ```
   conda activate insta
   ```

4. Install the required dependencies:
   ```
   conda install --file requirements.txt
   ```

5. Set up your environment variables in the `.env` file.

## Usage

To run the application, execute the following command:
```
python src/main.py
```

This will initialize the application and let you display random saved Instagram posts in the user interface.

## Contributing

Feel free to submit issues or pull requests for improvements or bug fixes.
