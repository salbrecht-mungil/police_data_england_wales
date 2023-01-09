from flask import Flask, render_template
# from core import df_year_22_validation
# import matplotlib.pyplot as plt
# import seaborn as sns

# Setting the dimensions of the plot


app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run()

