from flask import Flask, render_template

@app.route('/test')
def test():
    local_name = 'User'
    return render_template("test.html", name=local_name)
