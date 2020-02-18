from app import db
from app.models import User, Reminders
from flask import render_template, redirect, url_for, flash, session, request
from app.forms import RegistrationForm, LoginForm, ReminderForm, UpdateReminderForm
from flask_login import login_user, logout_user, login_required
from app.blueprints.account import account


@account.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    context = {
        'form': form
    }
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is None or not user.check_password(form.password.data):
            flash("You've used the wrong email or password,\ntry again!", "danger")
            return redirect(url_for('account.login'))

        flash("You have logged in successfully!", "success")
        login_user(user)
        return redirect(url_for('account.reminders'))
    return render_template('login.html', **context)

@account.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        u = User(name=form.name.data, email=form.email.data)
        u.generate_password(form.password.data)
        db.session.add(u)
        db.session.commit()
        flash("You have registered successfully!", 'success')
        return redirect(url_for('account.login'))
  
    context = {
        'form': form
    }
    return render_template('register.html', **context)

@account.route('/createreminder', methods=['GET', 'POST'])
@login_required
def createreminder():
    form = ReminderForm()
    user_ids=session["user_id"]
    context = {
        'form': form
    }
    if form.validate_on_submit():
        r = Reminders(user_id = user_ids, name=form.name.data, email=form.email.data, repeat=form.repeat.data, enabled=form.enabled.data, amount=form.amount.data, due_on=form.due_on.data, remind_on=form.remind_on.data)
        db.session.add(r)
        db.session.commit()
        flash("You have created a reminder!", 'success')
    return render_template('createreminder.html', **context)

@account.route('/reminders', methods=['GET', 'POST'])
@login_required
def reminders(): #Passes values to remindercard.html For dynamic card creation
    user_ids=session["user_id"]
    context = {
        'reminder' : Reminders.query.filter_by(user_id=user_ids)
    }
    return render_template('reminders.html', **context)

@account.route('/reminders/update/<int:id>', methods=['GET', 'POST'])
@login_required
def updatereminder(id):
    r = Reminders.query.filter_by(reminder_id=id).first()
    r.name = request.form['remindername']
    r.email = request.form['email']
    r.due_on = request.form['duedate']
    r.remind_on = request.form['remindon']
    r.amount = request.form['amount']
    db.session.commit()
    flash('Successfully Updated!', "success")
    return redirect(url_for('account.reminders'))

@account.route('/reminders/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_reminder(id):
    user_ids=session["user_id"]
    r = Reminders.query.get(id)
    db.session.delete(r)
    db.session.commit()
    flash('Reminder Deleted!', 'info')
    return redirect(url_for('account.reminders', id=user_ids))

@account.route('/logout')
@login_required
def logout():
    logout_user()
    flash("You have logged out", "danger")
    return redirect(url_for('account.login'))