from app import create_app, db
from app.models import User, Asset, Employee, Department, Maintenance, AssetHistory

app = create_app()

@app.shell_context_processor
def make_shell_context():
    return {
        'db': db,
        'User': User,
        'Asset': Asset,
        'Employee': Employee,
        'Department': Department,
        'Maintenance': Maintenance,
        'AssetHistory': AssetHistory
    }

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
