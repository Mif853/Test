import pytest
from services.api_services import ProductService


@pytest.fixture(scope="module")
def product_service():
    return ProductService()


def test_fetch_all_products(product_service):
    response = product_service.get_all_products()
    products = response.json()['products']
    assert len(products) > 0, "API should return at least one product"
    assert len(products) <= 200, "API should not return more than 200 products"


def test_product_price_calculation(product_service):
    response = product_service.get_all_products()
    products = response.json()['products']
    for product in products:
        calculated_price = ProductService.calculate_final_price(product)
        expected_price = product['price'] - (product['price'] * product['discountPercentage'] / 100)
        assert calculated_price == round(expected_price, 2), "Final price calculation is incorrect"


def test_invalid_limit(product_service):
    response = product_service.get_all_products(limit=-1)
    products = response.json()['products']
    assert products, "API should ignore invalid limit and return a full list of products"


def test_response_status(product_service):
    response = product_service.get_all_products()
    assert response.status_code == 200, "API did not return a successful status code"
