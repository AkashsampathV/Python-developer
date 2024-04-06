from flask import *
obj=Flask(__name__)
@obj.route("/")
def f1():
    return render_template("index.html")
@obj.route("/display/<value1>")
def f2(value1):
    return render_template("INDIA.html",score=value1,wicket=3,over=5.5,target=150)
@obj.route("/nextpage/<value2>")
def f3(value2):
    return render_template("about.html",Winrate=value2)
@obj.route("/home")
def f4():
    score=67
    wicket=7
    over=7.4
    target=180
    return render_template("akash.html",d={"score":score,"wicket":wicket,"over":over,"target":target})
  #  return render_template("akash.html",l=[score,wicket,over,target])
@obj.route("/mychoice")
def f5():
    return redirect(url_for("f1"))
@obj.route("/finalmatch")
def f6():
    match1="india"
    match2="pakistan"
    match3="newzland"
    return render_template("final.html",d1={"match1":match1,"match2":match2,"match3":match3})
@obj.route("/finale")
def f7():
    return redirect(url_for("f6"))
if __name__ == "__main__":
    obj.run(debug=True)
