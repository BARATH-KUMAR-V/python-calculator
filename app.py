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
        elif op == "/": result = a / b if b != 0 else "Error: Division by zero"
    return render_template_string(HTML, result=result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
