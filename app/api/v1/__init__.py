
from flask import Blueprint

v1=Blueprint('v1', __name__)

from app.api.v1.views.parties import parties

#parties modules
v1.add_url_rule('/parties', )