#-----------------------------------
#Author: Hasan Ahmad 
#Date: 6/10/2023
#Class: CSC5991
#-----------------------------------
from flask import Flask, jsonify, request, url_for, render_template_string
import random

app = Flask(__name__)

jokeArchive = [
    "What's a skeleton's favorite musical instrument? The trom-bone.",
    "How much did the pirate's new earrings cost him? A buccaneer!",
    "When is the best time to go to the dentist? Tooth-hurty!",
    "What's the difference between America and a memory stick? One's USA and the other's USB.",
    "What has four wheels and flies? A garbage truck.",
    "What comes down, but never comes up? Rain.",
    "What did the triangle say to the circle? You're pointless.",
    "What is a cheerleader's favorite drink? Root beer.",
    "What did one eye say to the other eye? Don't look now, but something between us smells.",
    "How do you know when the moon has had enough to eat? When it's full.",
    "What did the big chimney say to the little chimney? You're too young to smoke.",
    "What did the baby corn say to the mama corn? Where's pop corn?",
    "Where do Volkswagens go when they get old? The old Volks home.",
    "The inventor of the throat lozenge has died. There will be no coffin at his funeral.",
    "How do you know when the moon has had enough to eat? When it's full.",
    "What do you call a boat with a hole in the bottom? A sink.",
    "What did one penny say to another penny? We make cents.",
    "What kind of lion never roars? A dande-lion!",
    "Why do moon rocks taste better than earth rocks? Because they're meteor.",
    "Why did the mobile phone need glasses? It lost all its contacts.",
    "When does Friday come before Thursday? In the dictionary.",
    "What do prisoners use to call each other? Cell phones.",
    "What has a bed that you can't sleep in? A river.",
    "How long does it take to make butter? An echurnity!",
    "Why couldn't the pony sing? Because she was a little hoarse.",
    "Why did the bicycle fall over? Because it was two tired.",
    "What do you call it when you help a lemon that's in trouble? Lemon-aid.",
    "I used to have a job collecting leaves. I was raking it in.",
    "I drew up plans for Duckingham Palace, but I can’t find them. So I guess we’ll just have to ‘wing’ it.",
    "Sorry, I was all up in your grill about cooking yesterday."
]


@app.route('/jokes', methods=['GET'])
def get_random_jokes():
    num_jokes = int(request.args.get('num', 1))
    random_jokes = random.sample(jokeArchive, num_jokes)
    return jsonify({'jokes': random_jokes})

if __name__ == '__main__':
    app.run(host='0.0.0.0')
