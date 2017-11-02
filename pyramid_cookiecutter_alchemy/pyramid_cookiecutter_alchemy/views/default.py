"""."""

from pyramid.response import Response
import os
import io

CURRPATH = os.path.dirname(__file__)


def list_view(request):
    """."""
    path = os.path.join(CURRPATH, '../templates/index.html')
    with io.open(path) as file:
        return Response(file.read())


def detail_view(request):
    """."""
    path = os.path.join(CURRPATH, '../templates/detail.html')
    with io.open(path) as file:
        return Response(file.read())


def create_view(request):
    """."""
    path = os.path.join(CURRPATH, '../templates/create.html')
    with io.open(path) as file:
        return Response(file.read())


def update_view(request):
    """."""
    path = os.path.join(CURRPATH, '../templates/update.html')
