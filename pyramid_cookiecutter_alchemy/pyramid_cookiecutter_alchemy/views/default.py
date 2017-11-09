"""Contains class JournalViews that serves files."""

from pyramid.view import view_config
from pyramid.view import view_defaults
from ..models.mymodel import Entries


@view_defaults(renderer='layout.jinja2')
class JournalViews:
    """Class that contains functions for views."""

    def __init__(self, request):
        """Create instance of class."""
        self.request = request

    @view_config(route_name='home', renderer='../templates/index.jinja2')
    def list_view(self):
        """Serve up the list view."""
        journals = self.request.dbsession.query(Entries).all()
        return {
            'Journals': journals
        }

    @view_config(route_name='detail', renderer='../templates/detail.jinja2')
    def detail_view(self):
        """Serve up the detail view."""
        journal_num = self.request.matchdict['id']
        journal = self.request.dbsession.query(Entries).get(journal_num)
        return {
            'Journal': journal
        }

    @view_config(route_name='create', renderer='../templates/create.jinja2')
    def create_view(self, request):
        """Serve up the create view."""
        return {

        }

    @view_config(route_name='update', renderer='../templates/update.jinja2')
    def update_view(self, request):
        """Serve up the update view."""
        return {

        }
