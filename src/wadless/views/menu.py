from flask import Blueprint, render_template
from flask_login import login_required, current_user

from src.wadless.models.dashboard import Menu
from src.wadless.forms.menu import MenuCreateForm


menu_bp = Blueprint('menu', __name__, url_prefix='/menus')


@menu_bp.route('/')
@login_required
def index():
    menus = Menu.query.filter_by(account_id=current_user.account.id)
    return render_template('menu/index.html', menus=menus)


@menu_bp.route('/create')
@login_required
def create():
    form = MenuCreateForm()
    return render_template('menu/create.html', form=form)