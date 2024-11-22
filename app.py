from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# A list to store tasks 
tasks = []

@app.route("/")
def home():
    """Display the home page with the task list."""
    return render_template("index.html", tasks=tasks)
    
@app.route("/add", methods=["POST"])
def add_task():
    """Add a task to the list."""
    task = request.form.get("task")
    if task:
        
        tasks.append(task)
    return redirect(url_for("home"))       

@app.route("/delete/<int:task_index>")
def delete_task(task_index):
    """Remove a task from the list."""
    if 0 <= task_index < len(tasks):
        tasks.pop(task_index)
    return redirect(url_for("home"))   

if __name__ == "__main__":
    app.run(debug=True) 

    