from flask import Flask, render_template


app = Flask('__name__')

@app.route('/index')
def satya():
    return render_template('index.html')

@app.route('/preview', methods=['POST'])
def preview():
    name = request.form.get('name')
    email = request.form.get('email')
    resume = request.files['resume']
    cover_letter = request.form.get('cover-letter')

    # Process the job application data as needed

    return render_template('preview.html', name=name, email=email, resume=resume, cover_letter=cover_letter)



if __name__ == "__main__":
    app.run(debug=True)