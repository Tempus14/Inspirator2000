import os
import random
class PostSelector:
    def __init__(self, image_folder):
        self.image_folder = image_folder
        self.posts = self.load_posts()

    def load_posts(self):
        return [f for f in os.listdir(self.image_folder) if f.endswith(('.png', '.jpg', '.jpeg'))]

    def select_random_posts(self, count):
        return random.sample(self.posts, min(count, len(self.posts)))