from flask import Flask,render_template,url_for
app = Flask(__name__)

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from database_setup import Base,Alldata

engine = create_engine('sqlite:///newsdata.db')
Base.metadata.create_all(engine)

DBSession = sessionmaker(bind = engine)
session = DBSession()


@app.route('/')
@app.route('/business-politics-news')
def businessNews():
    row = session.query(Alldata).filter_by(category='Business and Politics').all()
    return render_template('index.html', row=row)

@app.route('/environment-news')
def environmentNews():
    row = session.query(Alldata).filter_by(category='Environment').all()
    return render_template('environment.html', row=row)

@app.route('/entertainment-news')
def entertainmentNews():
    row = session.query(Alldata).filter_by(category='Entertainment').all()
    return render_template('entertainment.html', row=row)

@app.route('/health-lifestyle-news')
def healthNews():
    row = session.query(Alldata).filter_by(category='Health and Lifestyle').all()
    return render_template('health.html',row=row)

@app.route('/technology-news')
def techNews():
    row = session.query(Alldata).filter_by(category='Science and Technology').all()
    return render_template('technology.html', row=row)
   
    
    
    
    
if __name__ == '__main__':
    app.run(debug=True)
    
