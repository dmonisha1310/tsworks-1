from flask import Flask, request
import mysql.connector

app = Flask(__name__)

# Connect to the database
cnx = mysql.connector.connect(user='user', password='password',
                              host='host', database='database')
cursor = cnx.cursor()

# Get all companies' stock data for a given date
@app.route('/stockdata/date/<date>', methods=['GET'])
def get_all_companies_data_by_date(date):
    query = "SELECT * FROM stock_data WHERE date=%s"
    cursor.execute(query, (date,))
    result = cursor.fetchall()
    return result

# Get all stock data for a given company for a given date
@app.route('/stockdata/<company>/date/<date>', methods=['GET'])
def get_company_data_by_date(company, date):
    query = "SELECT * FROM stock_data WHERE company=%s AND date=%s"
    cursor.execute(query, (company, date))
    result = cursor.fetchone()
    return result

# Get all stock data for a given company
@app.route('/stockdata/<company>', methods=['GET'])
def get_company_data(company):
    query = "SELECT * FROM stock_data WHERE company=%s"
    cursor.execute(query, (company,))
    result = cursor.fetchall()
    return result

# Update stock data for a company by date
@app.route('/stockdata', methods=['POST', 'PATCH'])
def update_data():
    data = request.get_json()
    date = data['date']
    company = data['company']
    close = data['close']
    volume = data['volume']
    query = "UPDATE stock_data SET close=%s, volume=%s WHERE date=%s AND company=%s"
    cursor.execute(query, (close, volume, date, company))
    cnx.commit()
    return "Data updated successfully"

# Close the connection
cnx.close()

if __name__ == '__main__':
    app.run()
