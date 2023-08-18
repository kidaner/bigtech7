from flask import Flask, render_template, request, jsonify
import sqlite3

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    summary = segments = products = management_commentary = analyst_questions = None

    if request.method == 'POST':
        ticker = request.form['ticker']
        conn = sqlite3.connect('bigtechsev.db')
        cursor = conn.cursor()

        cursor.execute(
            "SELECT Name, Sector, Industry FROM bigtechsev WHERE Ticker=?", (ticker,))
        data = cursor.fetchone()
        if data:
            summary = [data[0], data[1], data[2]]

        cursor.execute(
            "SELECT Segments FROM bigtechsev WHERE Ticker=?", (ticker,))
        segments_data = cursor.fetchone()
        if segments_data:
            segments = [segment.strip() for segment in segments_data[0].replace(
                "[", "").replace("]", "").replace("\"", "").split(",")]

        cursor.execute(
            "SELECT Products FROM bigtechsev WHERE Ticker=?", (ticker,))
        products_data = cursor.fetchone()
        if products_data:
            products = [product.strip() for product in products_data[0].replace(
                "[", "").replace("]", "").replace("\"", "").split(",")]

        cursor.execute(
            "SELECT Management Commentary FROM bigtechsev WHERE Ticker=?", (ticker,))
        management_data = cursor.fetchone()
        if management_data:
            management_commentary = [comment.strip() for comment in management_data[0].replace(
                "[", "").replace("]", "").replace("\"", "").split(",")]

        cursor.execute(
            "SELECT Analyst Questions FROM bigtechsev WHERE Ticker=?", (ticker,))
        questions_data = cursor.fetchone()
        if questions_data:
            analyst_questions = [question.strip() for question in questions_data[0].replace(
                "[", "").replace("]", "").replace("\"", "").split(",")]
        cursor.close()
        conn.close()

    return render_template('index.html', summary=summary, segments=segments, products=products, management_commentary=management_commentary, analyst_questions=analyst_questions)


if __name__ == "__main__":
    app.run(debug=True)
