from docx import Document
from docx.shared import Inches
import random
import os

# ------------------- CONSTANTS -------------------- #
DOC_NAME = "11th Day Together Wishes.docx"
IMAGE_WIDTH = Inches(6.5)
IMAGE_HEIGHT = Inches(4.88)
DIRECTORY_AB_PATH = r'C:\Users\Administrator\PycharmProjects\problem_solving'


# -------- GET ALL IMAGE FILES FROM A DIRECTORY ---- #
def get_all_files():
    dir_path = DIRECTORY_AB_PATH

    result = []

    for file in os.listdir(dir_path):
        if file.endswith('.jpg'):
            result.append(file)
    return result


IMAGE_FILES = get_all_files()


# ---- CREATE DOCUMENT OBJECT AND GIVE ATTRIBUTES --- #
document = Document(DOC_NAME)
paragraphs = document.paragraphs

# ----- SEARCH SIGN (**) AND REPLACE WITH IMAGE ----- #
for paragraph in paragraphs:
    if paragraph.text == "**":
        paragraph.text = ""
        image_run = paragraph.add_run()
        image_to_add = random.choice(IMAGE_FILES)
        image_run.add_picture(image_to_add, width=IMAGE_WIDTH, height=IMAGE_HEIGHT)

document.save(DOC_NAME)

# --------------------------- EXPLANATION ---------- #
# Add doc file
# read paragraphs
# iterate each paragraph
# find ** in paragraph.text
# add a run. assign it to a variable (lets call it image_run)
# use expression image_run.add_picture(FILENAME, width=, height=
