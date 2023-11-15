from flask import Flask, render_template, request, flash, redirect, session, url_for
import utility as u
from flask_session import Session
app = Flask(__name__)
app.secret_key = 'your_secret_key'
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)



@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email=request.form['email']
        password=request.form['password']
        role=request.form['role']
        
        if(u.checkuser(email, password, role)):
            session['logged_in'] = True
            session['email'] = email
            session['role'] = role

            flash('successfully logined','success')
            return redirect(url_for('manufacturer'))
        
        else:
            flash('Invalid Credentials','danger')
            return redirect(url_for('login'))
        
    return render_template('login.html')


        
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/Manufacturer')
def manufacturer():
    return render_template('manufacturer.html')


@app.route("/Manufacturer/adduser", methods=['GET', 'POST'])
def AddUsers():
    if request.method == 'POST':
        email=request.form['email']
        address=request.form['address']
        remarks=request.form['remarks']
        role=request.form['role']
        password=role
        if(u.createUserbyrole(email, password, role,remarks,address)):
            print("success")
            flash('successfully registered','success')
            return redirect(url_for('manufacturer'))
        else:
            print("failed")
            flash('Invalid Credentials','danger')
            return redirect(url_for('AddUsers'))
    return render_template('AddUsers.html')
    
@app.route('/customer')
def customer():
    return render_template('customer.html')

@app.route('/supplier')
def supplier():
    return render_template('supplier.html')

@app.route('/distributor')
def distributor():
    return render_template('distributor.html')

@app.route('/wholesaler')
def wholesaler():
    return render_template('wholesaler.html')

@app.route('/retailer')
def retailer():
    return render_template('retailer.html')

@app.route('/logout')
def logout():
    # logout_user()
    return redirect(url_for('index'))

@app.route('/Manufacturer/addproduct', methods=['GET', 'POST'])
def addproduct():
    if session['role'] == 'Manufacturer' and session['logged_in'] == True:
        if request.method == 'POST':
            data=request.get_json()
            product_name=data['productName']
            product_id=data['product_id']
            source='Factory'
            destination=data['destination']
            remarks=data['remarks']
            status=data['status']
            role=data['role']
            if(u.addproduct(product_name, product_id, source, destination, remarks, status, role)):
                flash('successfully registered','success')
                return redirect(url_for('addproduct'))
            else:
                flash('Sorry data not enetered..','danger')
    return render_template('addProduct.html')
        
        
@app.route('/UserLogin',methods=['GET', 'POST'])
def UserLogin():
    if request.method == 'POST':
        email=request.form['email']
        password=request.form['password']
        role=request.form['role']
        if(u.rolebased_login(email, password, role)):
            session['logged_in'] = True
            session['email'] = email
            session['role'] = role
            if role == 'supplier':
                return redirect(url_for('supplier'))
            elif role == 'distributor':
                return redirect(url_for('distributor'))
            elif role == 'wholesaler':
                return redirect(url_for('wholesaler'))
            elif role == 'retailer':
                return redirect(url_for('retailer'))
            elif role == 'customer':
                return redirect(url_for('customer'))
        else:
            flash('Invalid Credentials','danger')
            return redirect(url_for('UserLogin'))
    return render_template('usersLogin.html')

@app.route('/user/addProductByUser', methods=['GET', 'POST'])
def addProductByUser():
    if request.method == 'POST':
        data=request.get_json()
        product_name=data['productName']
        product_id=data['product_id']
        source='Factory'
        destination=data['destination']
        remarks=data['remarks']
        status=data['status']
        role=data['role']
        if(u.addproduct(product_name, product_id, source, destination, remarks, status, role)):
            flash('successfully registered','success')
            return redirect(url_for('addproduct'))
        else:
            flash('Sorry data not enetered..','danger')
    return render_template('addProductByUser.html')

@app.route("/user/addusersbyusers", methods=['GET', 'POST'])
def AddUsersByUsers():
    if request.method == 'POST':
        email=request.form['email']
        address=request.form['address']
        remarks=request.form['remarks']
        role=request.form['role']
        password=role
        if(u.createUserbyrole(email, password, role,remarks,address)):
            print("success")
            flash('successfully registered','success')
            return redirect(url_for(role))
        else:
            print("failed")
            flash('Invalid Credentials','danger')
            return redirect(url_for('AddUsers'))
    return render_template('addUsersByUsers.html')

app.run(debug=True)