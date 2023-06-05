import pandas as pd
from PIL import Image, ImageDraw, ImageFont

#df = pd.read_csv("students.csv")

df = pd.read_csv(r"D:\Codebase2023\Python\advance_python\tempate-card-generator-master\students.csv")

df
records = df.to_dict('records')

#font = ImageFont.truetype("OpenSans-Semibold.ttf", size=25)
font = ImageFont.truetype("C:/Windows/Fonts/Candara.ttf", size=25)

def generate_card(data):
  #  template = Image.open("template.png")
    template = Image.open(r"D:\Codebase2023\Python\advance_python\tempate-card-generator-master\template.png")
    
    
    # pic = Image.open(f"photos/{data['id']}.jpg").resize((165, 190), Image.ANTIALIAS)
    pic = Image.open(rf"D:\Codebase2023\Python\advance_python\tempate-card-generator-master\photos\{data['id']}.jpg").resize((165, 190), Image.LANCZOS)
    
    template.paste(pic, (25, 75, 190, 265))
    draw = ImageDraw.Draw(template)
    draw.text((315, 80), str(data['id']), font=font, fill='black')
    draw.text((315, 125), data['name'], font=font, fill='black')
    draw.text((315, 170), data['class'], font=font, fill='black')
    draw.text((315, 215), data['dob'], font=font, fill='black')
    return template

for record in records:
    card = generate_card(record)
    card.save(f"cards/{record['id']}.jpg")