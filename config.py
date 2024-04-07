import toml

class Config:
    def __init__(self, config_file_path):
        self.config_file_path = config_file_path
        self.coordinates = []
        self.doodle_info = []
        self.load_config()

    def load_config(self):
        try:
            with open(self.config_file_path, "r") as file:
                config_data = toml.load(file)
                self.coordinates = config_data.get("coordinates", [])
                self.doodle_info = config_data.get("doodle_info", [])
                
        except FileNotFoundError:
            print(f"Config file '{self.config_file_path}' not found.")
        except Exception as e:
            print(f"An error occurred while loading the config file: {e}")    
