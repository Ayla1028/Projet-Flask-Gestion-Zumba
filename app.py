from flask import Flask, request, render_template

app = Flask(__name__)

options = ["View participants", "View details", "View participant details",
               "add participant","remove participant","clear","remove participants without subscription",
               "number of participants in each level","participants for each dance type",
               "participants for a specific dance type","exit"
               ]

@app.route("/")
def home():
    return render_template("index.html", options=options)




@app.route("/select", methods=["POST"])
def select():
    data = request.get_json() 
    option = data["option"]
    if option == options[0]:
        message = "Participant 1, 2, 3."
    elif option==options[1]:
        message = "participants 1,2,3"
    elif option == options[2]:
        message = "participants 1,2,3,"
    elif option == options[3]:
        message = "add a participant"
        print(message)
        # ADDED BY CLAUDIA
        show_add_form = True
        return {
        "message": message,
        "show_text_field": False,
        "show_add_form": show_add_form
        
        }
        # ADDED BY CLAUDIA
    elif option == options[4]:
        message = "remove a participant"
    elif option == options[5]:
        message =  "clear"
    elif option == options[6]:
        message = "remove participants without subscription"
    elif option == options[7]:
        message = "number of participants in each level"
    elif option == options[8]:
           message = "participants for each dance type"
    elif option == options[9]:
        message = "participants for a specific dance type"
    elif option == options[10]:
        message = "exit"
    else:
        message = "please select an option"
    return {"message":message,"show_text_field": show_text_field}

    
@app.route("/submit", methods=["POST"])
def submit():
    name = request.form.get("name")
    email = request.form.get("email")
    return f"Name: {name}<br>Email: {email}"

app.run(debug=True)
