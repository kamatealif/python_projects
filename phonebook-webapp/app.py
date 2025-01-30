from flask import Flask,render_template,request, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# configure database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///contacts.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Contact model (database Table)
class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100),unique=True, nullable=True)
    address = db.Column(db.String(100), nullable=True)

# create the database
with app.app_context():
    db.create_all()

@app.route('/')
@app.route('/home')
def home():
    contacts = Contact.query.all()
    return render_template('home.html', contacts=contacts, title='Home')

@app.route('/add', methods=['GET','POST'])
def add_contact():
    if request.method == 'POST':
        name = request.form['name']
        phone = request.form['phone']
        email = request.form['email']
        address = request.form['address']

        new_contact = Contact(name=name, phone=phone, email=email, address=address)

        db.session.add(new_contact)
        db.session.commit()
        return redirect(url_for('home'))

    return render_template('add.html')  

@app.route('/edit/<int:id>', methods=['GET','POST'] )
def edit_contact(id):
    contact = Contact.query.get_or_404(id)

    if request.method == 'POST':
        contact.name = request.form['name']
        contact.phone = request.form['phone']
        contact.email = request.form.get('email', '')
        contact.address = request.form.get('address', '')

        db.session.commit()

        return redirect(url_for('home'))

    return render_template('edit.html', contact=contact)

@app.route('/delete/<int:id>', methods=['GET'])
def delete_contact(id):
    contact = Contact.query.get_or_404(id)
    db.session.delete(contact)
    db.session.commit()
    
    return redirect(url_for('home'))

@app.route('/search', methods=['POST'])
def search_contact():
    query = request.form['query']
    results = Contact.query.filter(
        (Contact.name.ilike(f"%{query}%")) | 
        (Contact.phone.ilike(f"%{query}%")) |
        (Contact.email.ilike(f"%{query}%"))
    ).all()

    # Return results as JSON for AJAX
    return jsonify([{'id': c.id, 'name': c.name, 'phone': c.phone} for c in results])

@app.route('/view/<int:id>')
def view_contact(id):
    contact = Contact.query.get_or_404(id)
    return render_template('view.html', contact=contact)


if __name__ == "__main__":
    app.run(debug=True)