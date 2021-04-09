from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 

import requests

from src.utils import format_currency, format_number

class InfographicGenerator:

    def generate_infographic(self, hardwork_summary):
        img = Image.open("assets/background.jpg")
        draw = ImageDraw.Draw(img)
        # font = ImageFont.truetype(<font-file>, <font-size>)
        font = ImageFont.truetype("assets/font/coolvetica rg.ttf", 24)
        # draw.text((x, y),"Sample Text",(r,g,b))
        draw.text((60, 60),f"Saved in gas fees {format_currency(hardwork_summary['gas_saved'])}$",(0,0,0),font=font)
        draw.text((60, 100),f"FARM buyback {format_number(hardwork_summary['farm_buybacks'])}",(0,0,0),font=font)
        draw.text((60, 140),f"Total income {format_currency(hardwork_summary['total_income'])}$",(0,0,0),font=font)

        img.save('out.jpg', quality=100, subsampling=0)