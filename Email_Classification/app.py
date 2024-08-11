from flask import Flask, render_template, request,url_for
import joblib
import re

model = joblib.load('models/multinomialnaivebayes.lb')
bow_obj = joblib.load('models/countervectorizer.lb')

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template("about.html")


@app.route("/prediction", methods=['GET', 'POST'])
def prediction():
    if request.method == "POST":
        emailContent = request.form.get('emailContent', '')
        emailContent = emailContent.lower()
        emailContent = re.sub(r'[^a-zA-Z ]', '', emailContent)

        emailContent_transformed = bow_obj.transform([emailContent])
        prediction = model.predict(emailContent_transformed)[0]

        labels = {'1': "SPAM", '0': "HAM"}
        result = labels.get(str(prediction))

        result_class = 'spam' if result == "SPAM" else 'ham'

        return render_template("output.html", output=result, result_class=result_class)
        

if __name__ == "__main__":
    app.run(debug=True)