from portfolio import create_app
import dbSetup

app = create_app()
app.cli.add_command(dbSetup.init_db)

if __name__ == "__main__":
    app.run(port=5000, debug=True)