import requests
import logging


class ProductService:
    BASE_URL = "https://dummyjson.com/products"

    @staticmethod
    def get_all_products(limit=200):
        url = f'{ProductService.BASE_URL}?limit={limit}'
        response = requests.get(url)
        ProductService.log_response(response)
        return response

    @staticmethod
    def calculate_final_price(product):
        price = product['price']
        discount = product['discountPercentage']
        final_price = price - (price * discount / 100)
        return round(final_price, 2)

    @staticmethod
    def log_response(response):
        if response.status_code != 200:
            logging.error(f'Failed to fetch data: {response.status_code} - {response.text}')
        else:
            logging.info(f'Successfully fetched data: {response.status_code}')
