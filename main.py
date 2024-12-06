from taipy import Gui

# Define the page
page = """
# Welcome to My Taipy App

This is a sample Taipy application.
"""

# Instantiate the Gui
gui = Gui(page)

if __name__ == "__main__":
    gui.run(use_reloader=True)