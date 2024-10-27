import os
import json

def load_directory():
    if os.path.exists('config.json'):
        with open('config.json', 'r') as f:
            config = json.load(f)
            return config.get('download_directory', '')
    return ''

def save_directory(directory):
    config = {'download_directory': directory}
    with open('config.json', 'w') as f:
        json.dump(config, f)