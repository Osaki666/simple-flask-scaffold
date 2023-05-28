from flask import (
    Blueprint, flash, redirect, render_template, request, session, url_for
)

from app_name.db import get_db

bp = Blueprint('my_blue_print', __name__, url_prefix='/my_blue_print')

@bp.route('/')
def index():
    return render_template('my_blue_print/index.html')