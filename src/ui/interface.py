import tkinter as tk
import os
from PIL import Image, ImageTk, ImageDraw
from utils.helpers import load_image, get_image_filenames
from utils.xmp_utils import get_image_rating, get_image_label
from dotenv import load_dotenv


class UserInterface:
    def __init__(self, folder):
        self.folder = folder
        self.root = tk.Tk()
        self.root.title("Instagram Post Viewer")
        
        # Create a canvas to display images
        self.canvas = tk.Canvas(self.root, width=800, height=600, bg="white")
        self.canvas.pack()

        # Store references to original and displayed images
        self.original_images = []  # Store Pillow Image objects
        self.displayed_images = []  # Store PhotoImage objects for Tkinter
        self.image_ratings = []  # Store ratings for each image
        self.image_filenames = []  # Store filenames for each image

        # Create buttons for categories
        button_frame = tk.Frame(self.root)
        button_frame.pack()

        # Define categories and their corresponding ratings
        categories = {
            "Sisters": 1,
            "Female Pose": 2,
            "Sexy Female Pose": 3,
            "Couple": 4,
            "Male Pose": 5
        }

        # Create a button for each category
        for category, rating in categories.items():
            button = tk.Button(button_frame, text=category, command=lambda r=rating: self.add_image_by_rating(r))
            button.pack(side=tk.LEFT, padx=5, pady=5)

        # Add a button for "Accessoire"
        accessoire_button = tk.Button(button_frame, text="Accessoire", command=self.add_image_by_label)
        accessoire_button.pack(side=tk.LEFT, padx=5, pady=5)

        # Add a reset button
        reset_button = tk.Button(button_frame, text="Reset", command=self.reset_canvas)
        reset_button.pack(side=tk.LEFT, padx=5, pady=5)

        # Add a save button
        save_button = tk.Button(button_frame, text="Save Canvas", command=self.save_canvas)
        save_button.pack(side=tk.LEFT, padx=5, pady=5)

        # Add an exit button
        exit_button = tk.Button(button_frame, text="Exit", command=self.root.destroy)
        exit_button.pack(side=tk.LEFT, padx=5, pady=5)

        # Bind click events to the canvas
        self.canvas.bind("<Button-1>", self.on_thumbnail_click)

        # Initialize the "X" button for enlarged view
        self.x_button = None

    def add_image_by_rating(self, rating):
        import random
        
        # Get all images in the folder
        images = get_image_filenames(self.folder)
        
        if not images:
            print("No images found in the folder.")
            return
        
        # Randomly pick images until one matches the rating
        while images:
            selected_image = random.choice(images)
            image_path = os.path.join(self.folder, selected_image)
            
            # Check the rating of the selected image
            if get_image_rating(image_path) == rating:
                try:
                    # Load the image
                    pil_image = load_image(image_path)
                    if pil_image:
                        # Add the image and its rating to the lists
                        self.original_images.append(pil_image)
                        self.image_ratings.append(rating)
                        self.image_filenames.append(selected_image)
                        self.update_canvas()
                        return
                except Exception as e:
                    print(f"Error displaying image {image_path}: {e}")
            
            # Remove the image from the list to avoid re-checking
            images.remove(selected_image)
        
        # If no matching image is found
        print(f"No images found with rating {rating}")

    def add_image_by_label(self):
        import random
        
        # Get all images in the folder
        images = get_image_filenames(self.folder)
        
        if not images:
            print("No images found in the folder.")
            return
        
        # Randomly pick images until one matches the label "Green"
        while images:
            selected_image = random.choice(images)
            image_path = os.path.join(self.folder, selected_image)
            
            # Check the label of the selected image
            if get_image_label(image_path) == "Green":  # "Green" corresponds to Accessoires
                try:
                    # Load the image
                    pil_image = load_image(image_path)
                    if pil_image:
                        # Add the image and its label to the lists
                        self.original_images.append(pil_image)
                        self.image_ratings.append("Accessoire")  # Use "Accessoire" as the label
                        self.image_filenames.append(selected_image)
                        self.update_canvas()
                        return
                except Exception as e:
                    print(f"Error displaying image {image_path}: {e}")
            
            # Remove the image from the list to avoid re-checking
            images.remove(selected_image)
        
        # If no matching image is found
        print("No images found with label 'Green'")

    def update_canvas(self):
        # Clear the canvas
        self.canvas.delete("all")
        
        # Define categories and their corresponding ratings
        categories = {
            1: "Sisters",
            2: "Female Pose",
            3: "Sexy Female Pose",
            4: "Couple",
            5: "Male Pose",
            "Accessoire": "Accessoire"  # For the Accessoire button
        }
        
        # Calculate the number of rows and columns needed
        num_images = len(self.original_images)
        if num_images == 0:
            return
        
        canvas_width = 800
        canvas_height = 600
        max_columns = 3  # Maximum number of images per row
        column_width = canvas_width // max_columns
        row_height = canvas_height // ((num_images + max_columns - 1) // max_columns)
        
        # Resize and position each image
        self.displayed_images = []  # Clear the displayed images list
        self.thumbnail_positions = []  # Store bounding boxes of thumbnails for click detection
        for index, pil_image in enumerate(self.original_images):
            # Resize the image to fit within the calculated cell size
            resized_image = pil_image.copy()  # Create a copy of the Pillow Image object
            resized_image.thumbnail((column_width - 10, row_height - 40))  # Leave space for the category text
            tk_image = ImageTk.PhotoImage(resized_image)
            
            # Calculate the position
            row = index // max_columns
            col = index % max_columns
            x = col * column_width + column_width // 2
            y = row * row_height + row_height // 2
            
            # Add the image to the canvas
            self.canvas.create_image(x, y, image=tk_image, anchor=tk.CENTER)
            self.displayed_images.append(tk_image)  # Keep a reference to avoid garbage collection
            
            # Add the category text just above the image
            category = categories.get(self.image_ratings[index], "Unknown")
            self.canvas.create_text(x, y - resized_image.height // 2 - 10, text=category, fill="black", font=("Arial", 12))
            
            # Store the bounding box of the thumbnail
            self.thumbnail_positions.append((x - column_width // 2, y - row_height // 2, x + column_width // 2, y + row_height // 2, index))

        # Hide the "X" button if it exists
        if self.x_button:
            self.x_button.place_forget()

    def on_thumbnail_click(self, event):
        # Detect which thumbnail was clicked
        for x1, y1, x2, y2, index in self.thumbnail_positions:
            if x1 <= event.x <= x2 and y1 <= event.y <= y2:  # Check if click is within thumbnail bounds
                self.display_single_image(index)
                break

    def display_single_image(self, index):
        # Change the canvas background to light gray
        self.canvas.config(bg="#dfdfdf")  # Very light gray
        
        # Clear the canvas
        self.canvas.delete("all")
        
        # Disable thumbnail click functionality in the enlarged view
        self.canvas.unbind("<Button-1>")
        
        # Get the selected image and filename
        pil_image = self.original_images[index]
        filename = self.image_filenames[index]
        
        # Resize the image to fit the canvas
        resized_image = pil_image.copy()
        resized_image.thumbnail((800, 500))  # Leave space for the caption and border
        tk_image = ImageTk.PhotoImage(resized_image)
        
        # Calculate the position for the border and image
        image_x, image_y = 400, 275  # Slightly lower center of the canvas
        border_thickness = 30  # Thickness of the white border
        bottom_extension = 40  # Additional space at the bottom for the filename
        
        # Draw the white border around the image
        self.canvas.create_rectangle(
            image_x - resized_image.width // 2 - border_thickness,
            image_y - resized_image.height // 2 - border_thickness,
            image_x + resized_image.width // 2 + border_thickness,
            image_y + resized_image.height // 2 + border_thickness + bottom_extension,
            fill="white",
            outline=""
        )
        
        # Display the image
        self.canvas.create_image(image_x, image_y, image=tk_image, anchor=tk.CENTER)
        self.displayed_images = [tk_image]  # Update displayed images
        
        # Display the filename as a caption below the image
        self.canvas.create_text(image_x, image_y + resized_image.height // 2 + 30, text=filename, fill="black", font=("Arial", 14))
        
        # Add an "X" button to return to the overview
        self.x_button = tk.Button(self.root, text="X", command=self.return_to_overview)
        self.x_button.place(x=750, y=10)

    def return_to_overview(self):
        # Change the canvas background back to white
        self.canvas.config(bg="white")
        
        # Remove the "X" button
        if self.x_button:
            self.x_button.destroy()
            self.x_button = None
        
        # Re-enable thumbnail click functionality
        self.canvas.bind("<Button-1>", self.on_thumbnail_click)
        
        # Clear the canvas and return to the overview
        self.update_canvas()

    def reset_canvas(self):
        # Clear the canvas and reset the images lists
        self.canvas.delete("all")
        self.original_images = []
        self.displayed_images = []
        self.image_ratings = []
        self.image_filenames = []

    def save_canvas(self):
        # Load environment variables from .env file
        load_dotenv()
        
        # Define categories and their corresponding ratings
        categories = {
            1: "Sisters",
            2: "Female Pose",
            3: "Sexy Female Pose",
            4: "Couple",
            5: "Male Pose",
            "Accessoire": "Accessoire"  # For the Accessoire button
        }

        # Calculate the number of rows and columns needed
        max_columns = 3
        num_images = len(self.original_images)
        if num_images == 0:
            print("No images to save.")
            return
        
        # Define high-resolution dimensions for each image
        short_side = 700  # Short side of each image in the saved canvas
        horizontal_padding = 20  # Padding between images and edges
        vertical_padding = 50  # Padding above and below images
        text_space = 100  # Space for category and filename text
        filename_space = 40  # Constant space between the image and the filename
        category_space = 30  # Constant space between the category and the top of the image

        # Calculate canvas dimensions
        num_rows = (num_images + max_columns - 1) // max_columns
        num_columns = min(num_images, max_columns)
        canvas_width = num_columns * (short_side + horizontal_padding)
        canvas_height = num_rows * (short_side + text_space + vertical_padding + filename_space)

        # Create a high-resolution canvas
        output_image = Image.new("RGB", (canvas_width, canvas_height), "white")
        draw = ImageDraw.Draw(output_image)

        # Define font sizes
        from PIL import ImageFont
        try:
            font_category = ImageFont.truetype("arial.ttf", 36)  # Larger font for categories
            font_filename = ImageFont.truetype("arial.ttf", 28)  # Slightly smaller font for filenames
        except IOError:
            # Fallback to default font if "arial.ttf" is not available
            font_category = None
            font_filename = None

        # Draw each image, its category, and filename onto the output image
        for index, pil_image in enumerate(self.original_images):
            # Resize the image to high resolution
            resized_image = pil_image.copy()
            resized_image.thumbnail((short_side, short_side))
            image_width, image_height = resized_image.size
            
            # Calculate the position
            row = index // max_columns
            col = index % max_columns
            x = col * (short_side + horizontal_padding) + horizontal_padding // 2
            y = row * (short_side + text_space + vertical_padding + filename_space) + vertical_padding
            
            # Center the image horizontally
            image_x = x + (short_side - image_width) // 2
            image_y = y + text_space
            
            # Paste the image onto the output image
            output_image.paste(resized_image, (image_x, image_y))
            
            # Draw the category text close to the top of the image, horizontally centered
            category = categories.get(self.image_ratings[index], "Unknown")
            category_x = x + short_side // 2
            category_y = image_y - category_space
            draw.text((category_x, category_y), category, fill="black", font=font_category, anchor="mm")
            
            # Draw the filename as a caption below the image, horizontally centered
            filename = self.image_filenames[index]
            filename_x = x + short_side // 2
            filename_y = image_y + image_height + filename_space // 2
            draw.text((filename_x, filename_y), filename, fill="black", font=font_filename, anchor="mm")

        # Get the destination path from the environment variable
        destination_path = os.getenv("DESTINATION_PATH", self.folder)  # Default to self.folder if not set

        # Ensure the destination directory exists
        os.makedirs(destination_path, exist_ok=True)

        # Save the output image
        output_path = os.path.join(destination_path, "canvas_output.jpg")
        output_image.save(output_path)
        print(f"High-resolution canvas saved as {output_path}")

    def run(self):
        self.root.mainloop()