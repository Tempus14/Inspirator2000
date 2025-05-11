def load_image(image_path):
    from PIL import Image
    try:
        image = Image.open(image_path)
        return image
    except Exception as e:
        print(f"Error loading image {image_path}: {e}")
        return None

def format_post_data(post):
    formatted_data = {
        'caption': post.get('caption', ''),
        'image_url': post.get('image_url', ''),
        'timestamp': post.get('timestamp', '')
    }
    return formatted_data

def get_image_filenames(directory):
    import os
    return [f for f in os.listdir(directory) if f.endswith(('.png', '.jpg', '.jpeg'))]