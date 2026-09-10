# 🧮 Python Calculator App
**DevOps Lab Project 2 | Python Flask | Jenkins Pipeline**

## 🎯 Aim
Build a web-based calculator using Python Flask that performs basic arithmetic, and deploy it automatically using a Jenkins CI/CD pipeline.

---

## 📋 Prerequisites
- Python 3.x installed
- pip installed
- Git installed
- Jenkins installed

---

## 📁 Project Code

### `app.py`
```python
from flask import Flask, request, render_template_string
app = Flask(__name__)

HTML = """
<!DOCTYPE html><html><body style="font-family:Arial;max-width:400px;margin:50px auto">
<h2>Calculator</h2>
<form method="POST">
  <input name="a" type="number" step="any" placeholder="Number 1" required />
  <select name="op">
    <option>+</option><option>-</option><option>*</option><option>/</option>
  </select>
  <input name="b" type="number" step="any" placeholder="Number 2" required />
  <button type="submit">Calculate</button>
</form>
{% if result is not none %}<h3>Result: {{ result }}</h3>{% endif %}
</body></html>
"""

@app.route("/", methods=["GET","POST"])
def calc():
    result = None
    if request.method == "POST":
        a = float(request.form["a"])
        b = float(request.form["b"])
        op = request.form["op"]
        if op == "+": result = a + b
        elif op == "-": result = a - b
        elif op == "*": result = a * b
        elif op == "/": result = a / b if b != 0 else "Error"
    return render_template_string(HTML, result=result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
```

### `requirements.txt`
```
flask
```

---

## 🚀 How to Run Locally
```bash
pip install flask
python app.py
# Open browser: http://localhost:5000
```

---

## 🐙 GitHub Setup Commands
```bash
git init
git add app.py requirements.txt
git commit -m "Add Python Calculator"
git remote add origin https://github.com/BARATH-KUMAR-V/python-calculator.git
git push -u origin main
```

---

## 🔧 Jenkins Pipeline Setup (Step by Step)

### Step 1: Create Jenkinsfile in project root
```groovy
pipeline {
  agent any
  stages {
    stage('Checkout') {
      steps { git 'https://github.com/BARATH-KUMAR-V/python-calculator.git' }
    }
    stage('Install') {
      steps { sh 'pip install -r requirements.txt' }
    }
    stage('Deploy') {
      steps {
        sh 'pkill -f app.py || true'
        sh 'nohup python app.py > app.log 2>&1 &'
        sh 'echo "Calculator deployed on port 5000"'
      }
    }
  }
}
```

### Step 2: Push Jenkinsfile
```bash
git add Jenkinsfile
git commit -m "Add Jenkinsfile"
git push
```

### Step 3: Create Jenkins Pipeline Job
- Open Jenkins → **New Item**
- Name: `PythonCalculator` → Select **Pipeline** → **OK**

### Step 4: Configure Pipeline
- Under **Pipeline** section → Definition: **Pipeline script from SCM**
- SCM: **Git**
- Repository URL: `https://github.com/BARATH-KUMAR-V/python-calculator.git`
- Script Path: `Jenkinsfile`

### Step 5: Build Trigger
- Check **GitHub hook trigger for GITScm polling**

### Step 6: Save and Build
- Click **Save** → **Build Now**
- View **Console Output**

---

## ✅ Expected Output
- App runs at `http://your-server:5000`
- Every `git push` triggers Jenkins pipeline automatically
