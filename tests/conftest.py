import os
import dotenv
import pytest
import requests


@pytest.fixture(autouse=True, scope="session")
def env():
    """Returns environment variables"""
    dotenv.load_dotenv()


@pytest.fixture(scope="session")
def base_url():
    """Returns application URL from environment variables."""
    return os.getenv('BASE_URL')


@pytest.fixture(scope="session")
def last_response_date(base_url):
    response = requests.get(f"{base_url}/posts")
    return response.headers['Date']


@pytest.fixture(scope="session")
def base_response(base_url, last_response_date):
    """Returns response from base url"""
    headers = {
        'If-None-Match': 'W/"6b80-Ybsq/K6GwwqrYkAsFxqDXGC7Do0',
        'If-Modified-Since': last_response_date,
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
                      ' AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/58.0.3029.110 Safari/537.3',
    }
    return requests.get(f"{base_url}/posts", headers=headers)


@pytest.fixture(scope="session")
def total_posts():
    """Returns default number of posts"""
    return os.getenv('DEFAULT_POSTS_RETURN')
