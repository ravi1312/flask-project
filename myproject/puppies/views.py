from flask import Blueprint,render_template,redirect,url_for
from myproject import db
from myproject.puppies.forms import AddForm,DelForm
from myproject.models import Puppy

puppies_blueprint = Blueprint('puppies',
                              __name__,
                              template_folder='templates/puppies')

@puppies_blueprint.route('/add', methods=['GET', 'POST'])
def add():
    form = AddForm()

    if form.validate_on_submit():
        name = form.name.data

        # Add new Puppy to database
        new_pup = Puppy(name)
        db.session.add(new_pup)
        db.session.commit()

        return redirect(url_for('list_pup'))

    return render_template('add_pup.html',form=form)

@puppies_blueprint.route('/list')
def list():
    # Grab a list of puppies from database.
    puppies = Puppy.query.all()
    return render_template('list_pup.html', puppies=puppies)

@puppies_blueprint.route('/delete', methods=['GET', 'POST'])
def delete():

    form = DelForm()

    if form.validate_on_submit():
        id = form.id.data
        pup = Puppy.query.get(id)
        db.session.delete(pup)
        db.session.commit()

        return redirect(url_for('list_pup'))
    return render_template('del_pup.html',form=form)
