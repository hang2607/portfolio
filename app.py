from flask import Flask, render_template, jsonify

app = Flask(__name__)

PROFILE = {
    "name": "Vu Thi Phuong Hang",
    "role": "International Economics Student & Creative",
    "school": "Foreign Trade University",
    "year": "Third-year",
    "about": "I have a lot of interests and little patience.",
    "skills": ["Adobe Illustrator", "Adobe Photoshop", "Adobe Lightroom", "Photography", "Drawing"],
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/profile')
def profile():
    return jsonify(PROFILE)

@app.route('/api/health')
def health():
    return jsonify({"status": "ok", "message": "Portfolio backend is running!"})

if __name__ == '__main__':
    app.run(debug=True)
