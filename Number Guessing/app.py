from flask import Flask, render_template, request

import random

app = Flask(__name__)

number_to_guess = random.randint(1, 100)
number_of_attempts = 0
game_over = False

@app.route('/')
def index():
    global number_of_attempts
    number_of_attempts = 0  # Reset attempts on each visit to index page
    return render_template('index.html', number_of_attempts=number_of_attempts)

@app.route('/guess', methods=['POST'])
def guess():
    global number_of_attempts, game_over

    if game_over:
        return render_template('game_over.html', number_of_attempts=number_of_attempts)

    player_guess = int(request.form['guess'])
    number_of_attempts += 1

    if player_guess < number_to_guess:
        feedback = "Too low! Try again."
    elif player_guess > number_to_guess:
        feedback = "Too high! Try again."
    else:
        feedback = f"Congratulations! You've guessed the number {number_to_guess} in {number_of_attempts} attempts."
        game_over = True

    return render_template('index.html', feedback=feedback, number_of_attempts=number_of_attempts)

if __name__ == '__main__':
    app.run(debug=True)
