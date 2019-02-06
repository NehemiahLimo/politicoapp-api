from flask import Blueprint


parties=Blueprint('parties', __name__)

parties.route('/parties', methods={['GET'], ['POST']})