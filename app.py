from flask import Flask, redirect, url_for, request, render_template

app = Flask(__name__) #Buat apk flask

@app.route('/')
def main() :
    return redirect('/login') #langsung tampil untuk login

@app.route('/success/<name>')
def success(name):
   return f'Welcome {name}' #menampilkan template index html

@app.route('/login', methods=["GET", 'POST'])
def loginGET():
    if(request.method == "POST") :
         user = request.form['nm']
         return redirect(url_for('success', name=user))
    return render_template('index.html')
#menjalankan apk flask
app.run(debug=True) 