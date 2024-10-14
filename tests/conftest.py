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
def base_response(base_url):
    """Returns response from base url"""
    return requests.get(f"{base_url}/posts")


@pytest.fixture(scope="session")
def total_posts():
    """Returns default number of posts"""
    return os.getenv('DEFAULT_POSTS_RETURN')
