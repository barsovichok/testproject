from http import HTTPStatus

from models.Posts import Post


def test_status_code(base_response):
    """Checks that response status code is OK"""
    assert base_response.status_code == HTTPStatus.OK


def test_json_format(base_response):
    """Checks that response status code is OK"""
    assert 'application/json' in base_response.headers['Content-Type']


def test_field_validation(base_response):
    """Checks that all fields are valid"""
    base_response = base_response.json()
    for response in base_response:
        Post.model_validate(response)


def test_response_headers(base_response):
    """Checks that response headers are present"""
    assert 'Cache-Control' in base_response.headers


def test_header_value(base_response):
    """Checks that headers are valid"""
    assert base_response.headers['Cache-Control'] == 'max-age=43200'


def test_unique_ids(base_response):
    """Checks that all ids are unique"""
    ids = [post['id'] for post in base_response.json()]
    assert len(ids) == len(set(ids))


def test_posts_amount(base_response, total_posts):
    """Checks that posts amount is the same as the total_posts"""
    assert len(base_response.json()) == total_posts
