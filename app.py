from flask import Flask, render_template
import pandas as pd
app = Flask(__name__)

@app.route('/')
def home():
    df = pd.read_excel('WHR25_Data_Figure_2.1v3.xlsx')
    df = df.query('Year == 2024').sort_values(by='Explained by: Healthy life expectancy', ascending=False).head(10)
    chart_data = {
        'labels': df['Country name'].tolist(),
        'datasets': [{
            'label': 'Healthy life expectancy',
            'data': df['Explained by: Healthy life expectancy'].tolist(),
            'backgroundColor': 'rgba(75, 192, 192, 0.2)',
            'borderColor': 'rgba(75, 192, 192, 1)',
            'borderWidth': 1
        }]
    }
    return render_template('chart.html', chart_data=chart_data)


if __name__ == '__main__':
    app.run(debug=True)