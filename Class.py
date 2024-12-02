# Base class for Smartphone
class Smartphone:
    def __init__(self, brand, model, color):
        self.brand = brand
        self.model = model
        self.color = color
    
    def turn_on(self):
        return f"{self.brand} {self.model} is now turned on."
    
    def turn_off(self):
        return f"{self.brand} {self.model} is now turned off."
    
    def make_call(self, phone_number):
        return f"Calling {phone_number} using {self.brand} {self.model}."
    
    def get_info(self):
        return f"Brand: {self.brand}, Model: {self.model}, Color: {self.color}"


# Inherited class for Smartphone with Camera
class SmartphoneWithCamera(Smartphone):
    def __init__(self, brand, model, color, camera_resolution):
        # Call to the base class constructor
        super().__init__(brand, model, color)
        self.camera_resolution = camera_resolution  # New attribute for camera
    
    def take_picture(self):
        return f"Taking a picture with {self.camera_resolution} MP camera on {self.brand} {self.model}."
    
    def get_info(self):
        # Overriding the base class get_info method to include camera information
        base_info = super().get_info()
        return f"{base_info}, Camera Resolution: {self.camera_resolution} MP"
    

# Example of using the classes
smartphone1 = Smartphone("Apple", "iPhone 15", "Space Gray")
smartphone_with_camera = SmartphoneWithCamera("Samsung", "Galaxy S24", "Phantom Black", 108)

print(smartphone1.get_info())  #
