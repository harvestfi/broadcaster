from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 

import requests

from src.utils import format_currency, format_number, format_date

class InfographicGenerator:

    def generate_strategies_infographic(self, hardwork_summary, ps_summary, vaults_summary, from_date, to_date):
        img = Image.open("assets/background.jpg")
        farmlogo = Image.open('assets/farm.png')

        draw = ImageDraw.Draw(img)
        header = ImageFont.truetype("assets/font/D-DIN-Bold.otf", 68)
        dates = ImageFont.truetype("assets/font/D-DIN.otf", 38)
        font = ImageFont.truetype("assets/font/D-DIN.otf", 50)
        metric = ImageFont.truetype("assets/font/D-DIN-Bold.otf", 50)

        draw.text((240, 60),f"Harvest.Finance key metrics",(249,32,105),font=header)

        draw.text((430, 130),format_date(from_date) + " - " + format_date(to_date),(255,255,255),font=dates)

        text_height = 135

        text_height+=75
        draw.text((200, text_height),f"$FARM buyback",(255,255,255),font=font)
        draw.text((800, text_height),f"{format_number(hardwork_summary['farm_buybacks'])}",(207,20,135),font=metric)
        area = (1000, text_height)  
        img.paste(farmlogo, area, farmlogo)

        text_height+=75
        draw.text((200, text_height),f"Income for Farmers",(255,255,255),font=font)
        draw.text((800, text_height),f"{format_currency(hardwork_summary['total_income'])}",(207,20,135),font=metric)

        text_height+=75
        draw.text((200, text_height),f"Saved in gas fees",(255,255,255),font=font)
        draw.text((800, text_height),f"{format_currency(hardwork_summary['gas_saved'])}",(207,20,135),font=metric)

        # text_height+=75
        # draw.text((200, text_height),f"Deployed Strategies",(255,255,255),font=font)
        # draw.text((800, text_height),f"{format_number(vaults_summary['quantity'])}",(207,20,135),font=metric)

        img.save('strategies_infographic.jpg', quality=100, subsampling=0)

    def generate_users_infographic(self, hardwork_summary, ps_summary, vaults_summary, from_date, to_date):
        img = Image.open("assets/background.jpg")
        farmlogo = Image.open('assets/farm.png')

        draw = ImageDraw.Draw(img)
        header = ImageFont.truetype("assets/font/D-DIN-Bold.otf", 68)
        dates = ImageFont.truetype("assets/font/D-DIN.otf", 38)
        font = ImageFont.truetype("assets/font/D-DIN.otf", 50)
        metric = ImageFont.truetype("assets/font/D-DIN-Bold.otf", 50)

        draw.text((240, 60),f"Harvest.Finance users metrics",(249,32,105),font=header)

        draw.text((430, 130),format_date(from_date) + " - " + format_date(to_date),(255,255,255),font=dates)

        text_height = 135

        text_height+=75
        draw.text((200, text_height),f"$FARM buyback",(255,255,255),font=font)
        draw.text((800, text_height),f"{format_number(hardwork_summary['farm_buybacks'])}",(207,20,135),font=metric)
        area = (1000, text_height)  
        img.paste(farmlogo, area, farmlogo)

        text_height+=75
        draw.text((200, text_height),f"Income for Farmers",(255,255,255),font=font)
        draw.text((800, text_height),f"{format_currency(hardwork_summary['total_income'])}",(207,20,135),font=metric)

        text_height+=75
        draw.text((200, text_height),f"Saved in gas fees",(255,255,255),font=font)
        draw.text((800, text_height),f"{format_currency(hardwork_summary['gas_saved'])}",(207,20,135),font=metric)

        # text_height+=75
        # draw.text((200, text_height),f"Deployed Strategies",(255,255,255),font=font)
        # draw.text((800, text_height),f"{format_number(vaults_summary['quantity'])}",(207,20,135),font=metric)

        img.save('users_infographic.jpg', quality=100, subsampling=0)