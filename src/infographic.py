from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 

import requests

from src.utils import format_currency, format_number, format_date

class InfographicGenerator:

    def generate_infographic(self, hardwork_summary, ps_summary, from_date, to_date):
        img = Image.open("assets/background.jpg")
        draw = ImageDraw.Draw(img)
        header = ImageFont.truetype("assets/font/D-DIN-Bold.otf", 68)
        dates = ImageFont.truetype("assets/font/D-DIN.otf", 38)
        font = ImageFont.truetype("assets/font/D-DIN.otf", 50)
        metric = ImageFont.truetype("assets/font/D-DIN-Bold.otf", 50)

        draw.text((240, 60),f"Harvest.Finance key metrics",(219,131,201),font=header)

        draw.text((430, 130),format_date(from_date) + " - " + format_date(to_date),(255,255,255),font=dates)

        draw.text((200, 210),f"FARM buyback",(255,255,255),font=font)
        draw.text((800, 210),f"{format_number(hardwork_summary['farm_buybacks'])}",(207,20,135),font=metric)

        draw.text((200, 285),f"Income for Farmers",(255,255,255),font=font)
        draw.text((800, 285),f"{format_currency(hardwork_summary['total_income'])}",(207,20,135),font=metric)

        draw.text((200, 360),f"Saved in gas fees",(255,255,255),font=font)
        draw.text((800, 360),f"{format_currency(hardwork_summary['gas_saved'])}",(207,20,135),font=metric)

        draw.text((200, 435),f"Emissions",(255,255,255),font=font)
        draw.text((800, 435),f"{format_number(ps_summary['emissions'])}",(207,20,135),font=metric)

        img.save('out.jpg', quality=100, subsampling=0)