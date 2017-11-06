"""Test pyramid functions."""

from pyramid.testing import DummyRequest
import pytest


@pytest.fixture
def testsomething():
    """Create test for something, not sure what."""
    from webtest import TestApp
    from pyramid.config import Configurator

    def main():
        config = Configurator
        config.include('pyramid_jinja2')
        config.include('.routes')
        config.scan()
        return config.make_wsgi_app()

    something = main()
    return TestApp(something)
