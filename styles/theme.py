from styles import neon, corporate, light, hacker

def apply_theme(theme_name):

    if theme_name == "Neon Cyber":
        neon.apply()

    elif theme_name == "Corporate":
        corporate.apply()

    elif theme_name == "Light":
        light.apply()

    elif theme_name == "Hacker":
        hacker.apply()