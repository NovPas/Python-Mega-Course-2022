from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

dictionary_df = pd.read_csv('./data/dictionary.csv')

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/api/v1/<word>')
def about(word):
    definition = dictionary_df.loc[dictionary_df['word'] == word.lower()]['definition'].squeeze()
    definition = definition if isinstance(definition, str) else 'definition not found'
    return {'definition': str(definition), 'word': word}


if __name__ == '__main__':
    app.run(debug=True)
