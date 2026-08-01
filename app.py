from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object("config.Config")

db = SQLAlchemy(app)

# Import routes
from routes import auth, accounts, transactions, community
app.register_blueprint(auth.bp)
app.register_blueprint(accounts.bp)
app.register_blueprint(transactions.bp)
app.register_blueprint(community.bp)

if __name__ == "__main__":
    app.run(debug=True)
