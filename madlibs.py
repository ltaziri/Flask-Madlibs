from random import choice

from flask import Flask, render_template, request


# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza', 'oh-so-not-meh',
    'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful', 'smashing', 'lovely']

VERBS_PAST_TENSE = [
    'ran', 'fell', 'ate', 'slipped', 'shouted', 'sat', 'danced', 'slept']

ADVERBS = [
    'fast', 'sloppily', 'merrily', 'angrily', 'awkwardly', 'wildly', 'enormously', 'nervously']

@app.route('/')
def start_here():
    """Homepage."""

    return "Hi! This is the home page."


@app.route('/hello')
def say_hello():
    """Save hello to user."""

    return render_template("hello.html")


@app.route('/greet', methods=["POST"])
def greet_person():
    """Greet user."""

    player = request.form.get("person")
    compliment = choice(AWESOMENESS)

    return render_template("compliment.html",
                           person=player,
                           compliment=compliment)

@app.route('/game', methods=["POST"])
def show_game_form():
    """Play game with user"""

    user_response = request.form.get("game")

    if user_response == "yes":
        return render_template("game.html")
    else:
        return render_template("goodbye.html") 

@app.route('/madlib')
def show_madlib():
    """Show madlib to user"""

    color_input = request.args.get("color")

    noun_input = request.args.get("noun")
    nountwo_input = request.args.get("noun_two")
    nountthree_input = request.args.get("noun_three")

    adjective_input = request.args.get("adjective")
    adjectivetwo_input = request.args.get("adjective_two")
    adjectivethree_input = request.args.get("adjective_three")
    adjectivefour_input = request.args.get("adjective_four")
    
    past_verb_input = choice(VERBS_PAST_TENSE)
    past_verbtwo_input = choice(VERBS_PAST_TENSE)

    adverb_input = choice(ADVERBS)
    adverbtwo_input = choice(ADVERBS)

    verb_input = request.args.get("verb")

    name_input = request.args.get("name")

    weather_input = request.args.getlist("weather")

    weather_string = " ".join(weather_input)
    templates = ["madlib.html","madlibtwo.html"]
    template_choice = choice(templates)    

    print weather_string
    return render_template(template_choice, 
                            game_color=color_input, 
                            game_noun=noun_input,
                            game_noun_two=nountwo_input,
                            game_noun_three=nountthree_input, 
                            game_adjective=adjective_input,
                            game_adjective_two=adjectivetwo_input,
                            game_adjective_three=adjectivethree_input,
                            game_adjective_four=adjectivefour_input,
                            game_past_verb=past_verb_input,
                            game_past_verb_two=past_verbtwo_input,
                            game_adverb=adverb_input,
                            game_adverb_two=adverbtwo_input,
                            game_verb=verb_input,
                            game_person=name_input,
                            game_weather=weather_string)

if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads" our web app
    # if we change the code.
    app.run(debug=True)
