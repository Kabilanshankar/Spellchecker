from spellchecker import SpellChecker
from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/')
def spellchecker():
    return render_template('index.html')

@app.route('/spell_check', methods=['GET', 'POST'])
def process_text():
    if request.method == 'POST':
        user_input = request.form['user_input']
        result = spell_check_user_input(user_input)
        return render_template('index.html', result=result)
    return render_template('index.html', result=None)

def spell_check_user_input(user_input):
    spell = SpellChecker()
    words_to_check = user_input.split()
    corrections = []

    for word in words_to_check:
        correction = spell.correction(word)
        if word != correction:
            corrections.append((word, correction))

    return corrections

if __name__ == '__main__':
    app.run(debug=True)
