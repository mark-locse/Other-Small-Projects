import pandas as pd
import random
import re
from PIL import Image, ImageDraw, ImageFont


def list_extract():
    df = pd.read_csv("C:/Screenshots/Bingo Event/objectives.csv")

    easy = df["EZ"].dropna().tolist()
    medium = df["MID"].dropna().tolist()
    hard = df["TUFF"].dropna().tolist()

    card = (
        random.sample(easy,9)+
        random.sample(medium,9)+
        random.sample(hard,7)
        )
    random.shuffle(card)

    grid = [card[i:i+5] for i in range(0,25,5)]
    return grid

def wrap_text(text, font, max_width, draw):
    words = re.split(r'(?<=/)|\s+', text)
    lines = []
    current = ""

    for word in words:
        candidate = current + word if current.endswith("/") else (current + " " + word if current else word)

        bbox = draw.textbbox((0, 0), candidate, font=font)
        width = bbox[2] - bbox[0]

        if width <= max_width:
            current = candidate
        else:
            if current:
                lines.append(current)
            current = word.lstrip()

    if current:
        lines.append(current)
    return "\n".join(lines)

def bingo_card(grid, name):
    cell_size = 200
    header_height = 100
    grid_size = 5*cell_size

    img = Image.new("RGB",(grid_size, grid_size+header_height), "white")
    draw = ImageDraw.Draw(img)

    #fonts
    try:
        header_font = ImageFont.truetype("verdana.ttf", 48)
        cell_font = ImageFont.truetype("verdana.ttf", 26)
    except:
        header_font = ImageFont.load_default()
        cell_font = ImageFont.load_default()

    #header
    draw.rectangle([0,0,grid_size,header_height],fill=(30,144,255))
    header_text = name+"'s Bingo Card"
    bbox = draw.textbbox((0,0), header_text, font=header_font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]

    draw.text(((grid_size - text_width)/2, (header_height - text_height)/2),
              header_text, fill="white", font=header_font)

    #grid
    for r in range(5):
        for c in range(5):
            x0 = c*cell_size
            y0 = header_height+r*cell_size
            x1 = x0+cell_size
            y1 = y0+cell_size

            draw.rectangle([x0,y0,x1,y1],outline="black")
            text=str(grid[r][c])

            max_text_width = cell_size - 20
            wrapped = wrap_text(text, cell_font, max_text_width, draw)

            bbox=draw.multiline_textbbox((0,0), wrapped, font=cell_font, align="center")
            text_w = bbox[2]-bbox[0]
            text_h = bbox[3]-bbox[1]

            tx = x0 + (cell_size - text_w) / 2
            ty = y0 + (cell_size - text_h) / 2

            draw.multiline_text((tx,ty),wrapped,fill="black",font=cell_font,align="center")

    img.save(f"C:/Screenshots/Bingo Event/Bingo Cards/{name}.png")

bingo_card(list_extract(), input("Enter PSN ID: "))

