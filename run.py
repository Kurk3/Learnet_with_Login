from src import create_app

app = create_app() #script in __init__.py

if __name__ == '__main__':
    app.run(debug=True)
