from flask import Flask, render_template, request, redirect, url_for
import getpass
from prettytable import PrettyTable

app = Flask(__name__)
game = None
users = {}


class DiceGame:
    def __init__(self):
        self.users = {'admin': 'admin123'}
        self.players = {}
        self.player_choices = {'Play': {}, 'Quit': {}}

    # ... (Keep the existing DiceGame class as it is)

@app.route('/')
def home():
    return render_template('home.html')

# ... (Previous code remains the same)

@app.route('/admin', methods=['GET', 'POST'])
def admin():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == 'admin' and password == game.users['admin']:
            return redirect(url_for('admin_menu'))
        else:
            return render_template('admin_login.html', message="Invalid credentials. Please try again.")
    return render_template('admin_login.html', message="")

@app.route('/admin/menu', methods=['GET', 'POST'])
def admin_menu():
    if request.method == 'POST':
        choice = request.form['choice']

        if choice == 'view_all_players':
            return redirect(url_for('view_all_players'))
        elif choice == 'add_player':
            return redirect(url_for('add_player'))
        elif choice == 'delete_player':
            return redirect(url_for('delete_player'))
        elif choice == 'update_player':
            return redirect(url_for('update_player'))
        elif choice == 'logout':
            return redirect(url_for('home'))

    return render_template('admin_menu.html', players=game.players, choices=game.player_choices)

# ... (Previous code remains the same)
# ... (Previous code remains the same)

@app.route('/admin/view_all_players')
def view_all_players():
    return render_template('view_all_players.html', players=game.players, choices=game.player_choices)

@app.route('/admin/add_player', methods=['GET', 'POST'])
def add_player():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        game.players[username] = password
        return redirect(url_for('view_all_players'))
    return render_template('add_player.html')

@app.route('/admin/delete_player', methods=['GET', 'POST'])
def delete_player():
    if request.method == 'POST':
        username = request.form['username']
        if username in game.players:
            del game.players[username]
        return redirect(url_for('view_all_players'))
    return render_template('delete_player.html')

@app.route('/admin/update_player', methods=['GET', 'POST'])
def update_player():
    if request.method == 'POST':
        username = request.form['username']
        new_password = request.form['new_password']
        if username in game.players:
            game.players[username] = new_password
        return redirect(url_for('view_all_players'))
    return render_template('update_player.html')

@app.route('/admin/logout')
def logout():
    return redirect(url_for('home'))

# ... (Previous code remains the same)


# Add more routes for other pages as needed
# ... (Previous code remains the same)

@app.route('/player', methods=['GET', 'POST'])
def player():
    if request.method == 'POST':
        player_choice = request.form['player_choice']
        if player_choice == 'sign_up':
            return redirect(url_for('sign_up'))
        elif player_choice == 'login':
            return redirect(url_for('login'))
        else:
            return render_template('player.html', message="Invalid choice. Please try again.")
    return render_template('player.html', message="")

@app.route('/player/sign_up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        confirm_password = request.form['confirm_password']

        if password == confirm_password:
            game.players[username] = password
            return render_template('player.html', message="Sign up successful! Now you can log in.")
        else:
            return render_template('sign_up.html', message="Passwords do not match. Please try again.")
    return render_template('sign_up.html', message="")

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Process login form data
        username = request.form.get('username')
        password = request.form.get('password')
        
        # Your authentication logic here...

        # Redirect to gameplay page with the username
        return redirect(url_for('gameplay', username=username))

    # Render the login page for GET requests
    return render_template('login.html')

@app.route('/gameplay', methods=['GET', 'POST'])
def gameplay():
    if request.method == 'POST':
        game_option = request.form.get('game_option')

        # Placeholder for gameplay logic
        if game_option == 'play':
            # Do something when the user chooses to play
            pass
        elif game_option == 'quit':
            # Do something when the user chooses to quit
            pass
        
    # Render the gameplay page for GET requests
    return render_template('gameplay.html', username=request.args.get('username'))


if __name__ == '__main__':
    game = DiceGame()
    app.run(debug=True)



