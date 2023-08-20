from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello world!!!"

if __name__ == "__main__":
    # Get the port from the environment variable, default to 5000
    port = int(os.environ.get("PORT", 5000))

    # Run the app with the specified settings
    app.run(debug=True, host="0.0.0.0", port=port)
