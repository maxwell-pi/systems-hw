from notebook import app, db

with app.app_context():
    db.create_all()
app.run(debug=True)