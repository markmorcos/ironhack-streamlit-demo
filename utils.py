import random

# Lists of sample data that can be used for random generation
COLORS = [
    "Crimson", "Azure", "Emerald", "Golden", "Violet", 
    "Sapphire", "Silver", "Obsidian", "Ruby", "Jade"
]

ANIMALS = [
    "Dragon", "Phoenix", "Griffin", "Lion", "Eagle",
    "Wolf", "Tiger", "Panther", "Falcon", "Bear"
]

SUPERPOWERS = [
    "Flying", "Invisibility", "Super Strength", "Telekinesis",
    "Time Control", "Mind Reading", "Energy Blasts", "Healing",
    "Shape Shifting", "Elemental Control"
]

MOTTOS = [
    "Justice never sleeps!",
    "Evil fears my name!",
    "With great power comes great responsibility!",
    "I am the night!",
    "Truth and justice prevail!",
    "Fear not, citizens!",
    "Evil's worst nightmare!",
    "Defender of the innocent!",
    "Hope never dies!",
    "For honor and glory!"
]

def generate_random_name():
    """Generate a random superhero name using the format: The [Color] [Animal] of [Number]"""
    color = random.choice(COLORS)
    animal = random.choice(ANIMALS)
    number = random.randint(1, 100)
    return f"The {color} {animal} of {number}"

def get_random_motto():
    """Return a random motto from the predefined list"""
    return random.choice(MOTTOS)

def generate_hero_profile(color=None, animal=None, number=None, power=None):
    """
    Generate a complete hero profile with optional parameters.
    If any parameter is None, it will be randomly generated.
    """
    hero_profile = {
        "color": color or random.choice(COLORS),
        "animal": animal or random.choice(ANIMALS),
        "number": number or random.randint(1, 100),
        "power": power or random.choice(SUPERPOWERS),
        "motto": get_random_motto()
    }
    
    hero_profile["name"] = f"The {hero_profile['color']} {hero_profile['animal']} of {hero_profile['number']}"
    return hero_profile

def get_power_description(power):
    """Return a description for each superpower"""
    descriptions = {
        "Flying": "Soar through the skies with incredible speed and agility",
        "Invisibility": "Become completely unseen at will",
        "Super Strength": "Possess the power to lift incredible weights and overcome any physical challenge",
        "Telekinesis": "Move objects with the power of your mind",
        "Time Control": "Manipulate the flow of time itself",
        "Mind Reading": "Perceive the thoughts and intentions of others",
        "Energy Blasts": "Project powerful beams of pure energy",
        "Healing": "Cure injuries and ailments with a touch",
        "Shape Shifting": "Transform your appearance at will",
        "Elemental Control": "Command the forces of nature"
    }
    return descriptions.get(power, "A mysterious and powerful ability") 