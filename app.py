from flask import Flask, render_template

@app.route('/test')
def test():
    local_name = 'test_name'
    return render_template("test.html", name=local_name)
