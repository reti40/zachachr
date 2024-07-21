from flask import Flask, render_template, request

app = Flask("__name__")

# about page

@app.route("/")
def index():
    return render_template("about.html")

# About page

@app.route("/about")
def about():
    return render_template("about.html")

# CV and other news

@app.route("/cv")
def cv():
    return render_template("cv.html")

# Scores page

@app.route("/scores")
def scores():
    return render_template("scores.html")

# List of Scores

# Reflections

@app.route("/reflections")
def reflections():
    return render_template("reflections.html")

# Reflections Prework

@app.route("/reflections_prework")
def reflections_prework():
    return render_template("reflections_prework.html")

# Lying Down

@app.route("/lying_down")
def lyding_down():
    return render_template("lying_down.html")

# Lying Down Prework

@app.route("/lyingdown_prework")
def lydingdown_prework():
    return render_template("lyingdown_prework.html")

@app.route("/boaw")
def boaw():
    return render_template("boaw.html")

@app.route("/nautilus")
def nautilu():
    return render_template("nautilus.html")

@app.route("/dtrh")
def dtrh():
    return render_template("dtrh.html")

@app.route("/still_sky")
def still_sky():
    return render_template("still_sky.html")

@app.route("/waking_up")
def waking_up():
    return render_template("waking_up.html")

# Redfin

@app.route("/redfin")
def redfin():
    return render_template("Redfin.html")

# Redfin Prework

@app.route("/redfin_prework")
def redfin_prework():
    return render_template("redfin_prework.html")

@app.route("/jabberwocky")
def jabberwocky():
    return render_template("jabberwocky.html")

@app.route("/ngcs")
def ngcs():
    return render_template("ngcs.html")

@app.route("/noir")
def noir():
    return render_template("noir.html")

@app.route("/maxwell")
def maxwell():
    return render_template("maxwell.html")

# Chamber page

@app.route("/chamber")
def chamber():
    return render_template("chamber.html")

# Orchestra Page

@app.route("/orchestra")
def orchestra():
    return render_template("orchestral.html")

# Jazz page

@app.route("/jazz")
def jazz():
    return render_template("jazz.html")

# Bird on a wire

@app.route("/bird_on_a_wire")
def bird():
    return render_template("bird_on_a_wire.html")

# In flux

@app.route("/In_Flux")
def Flux():
    return render_template("InFlux.html")

# run website

if __name__ == "__main__":
    app.run(debug=True)



