from app import create_app, db
from app.models import User, Department, Employee, Asset
from datetime import datetime, timedelta

app = create_app()

with app.app_context():
    print("Creating database tables...")
    db.create_all()
    
    print("Checking for existing data...")
    if User.query.first():
        print("Database already has data. Skipping seed.")
    else:
        print("Seeding database...")
        
        admin = User(
            username='admin',
            email='admin@example.com',
            full_name='System Administrator',
            role='admin',
            is_active=True
        )
        admin.set_password('admin123')
        db.session.add(admin)
        
        staff = User(
            username='staff',
            email='staff@example.com',
            full_name='IT Staff Member',
            role='staff',
            is_active=True
        )
        staff.set_password('staff123')
        db.session.add(staff)
        
        viewer = User(
            username='viewer',
            email='viewer@example.com',
            full_name='Guest Viewer',
            role='viewer',
            is_active=True
        )
        viewer.set_password('viewer123')
        db.session.add(viewer)
        
        departments = [
            Department(name_en='IT Department', name_ar='قسم تكنولوجيا المعلومات', description_en='Information Technology', description_ar='تكنولوجيا المعلومات'),
            Department(name_en='Finance', name_ar='المالية', description_en='Finance Department', description_ar='قسم المالية'),
            Department(name_en='HR', name_ar='الموارد البشرية', description_en='Human Resources', description_ar='الموارد البشرية'),
            Department(name_en='Marketing', name_ar='التسويق', description_en='Marketing Department', description_ar='قسم التسويق'),
            Department(name_en='Operations', name_ar='العمليات', description_en='Operations Department', description_ar='قسم العمليات'),
        ]
        for dept in departments:
            db.session.add(dept)
        
        db.session.commit()
        
        employees = [
            Employee(employee_id='EMP001', name_en='Ahmed Ali', name_ar='أحمد علي', job_title_en='IT Manager', job_title_ar='مدير تكنولوجيا المعلومات', department_id=1, email='ahmed@example.com', phone='+966501234567'),
            Employee(employee_id='EMP002', name_en='Sara Mohammed', name_ar='سارة محمد', job_title_en='System Administrator', job_title_ar='مسؤول نظام', department_id=1, email='sara@example.com', phone='+966501234568'),
            Employee(employee_id='EMP003', name_en='Omar Hassan', name_ar='عمر حسن', job_title_en='Network Engineer', job_title_ar='مهندس شبكات', department_id=1, email='omar@example.com', phone='+966501234569'),
            Employee(employee_id='EMP004', name_en='Fatima Abdullah', name_ar='فاطمة عبدالله', job_title_en='Accountant', job_title_ar='محاسبة', department_id=2, email='fatima@example.com', phone='+966501234570'),
            Employee(employee_id='EMP005', name_en='Khalid Salem', name_ar='خالد سالم', job_title_en='HR Specialist', job_title_ar='أخصائي موارد بشرية', department_id=3, email='khalid@example.com', phone='+966501234571'),
        ]
        for emp in employees:
            db.session.add(emp)
        
        db.session.commit()
        
        assets = [
            Asset(asset_id='COMP001', asset_type='computer', brand='Dell', model='OptiPlex 7090', serial_number='SN1234567890', status='in_use', purchase_date=datetime.now().date() - timedelta(days=365), warranty_expiry=datetime.now().date() + timedelta(days=365), location='Office 201', department_id=1, assigned_to=1),
            Asset(asset_id='COMP002', asset_type='computer', brand='HP', model='EliteDesk 800 G6', serial_number='SN1234567891', status='in_use', purchase_date=datetime.now().date() - timedelta(days=300), warranty_expiry=datetime.now().date() + timedelta(days=400), location='Office 202', department_id=1, assigned_to=2),
            Asset(asset_id='COMP003', asset_type='computer', brand='Lenovo', model='ThinkCentre M720', serial_number='SN1234567892', status='available', purchase_date=datetime.now().date() - timedelta(days=200), warranty_expiry=datetime.now().date() + timedelta(days=500), location='IT Storage'),
            Asset(asset_id='MON001', asset_type='monitor', brand='Dell', model='P2422H 24"', serial_number='SN2234567890', status='in_use', purchase_date=datetime.now().date() - timedelta(days=365), warranty_expiry=datetime.now().date() + timedelta(days=365), location='Office 201', department_id=1, assigned_to=1),
            Asset(asset_id='MON002', asset_type='monitor', brand='LG', model='27UK850 27"', serial_number='SN2234567891', status='in_use', purchase_date=datetime.now().date() - timedelta(days=300), warranty_expiry=datetime.now().date() + timedelta(days=400), location='Office 202', department_id=1, assigned_to=2),
            Asset(asset_id='PRINT001', asset_type='printer', brand='HP', model='LaserJet Pro M404dn', serial_number='SN3234567890', status='in_use', purchase_date=datetime.now().date() - timedelta(days=400), warranty_expiry=datetime.now().date() + timedelta(days=300), location='Floor 2 Common Area', department_id=1),
            Asset(asset_id='PRINT002', asset_type='printer', brand='Canon', model='imageCLASS MF445dw', serial_number='SN3234567891', status='under_repair', purchase_date=datetime.now().date() - timedelta(days=500), warranty_expiry=datetime.now().date() + timedelta(days=200), location='Floor 3 Common Area', department_id=2),
            Asset(asset_id='SCAN001', asset_type='scanner', brand='Epson', model='WorkForce DS-530', serial_number='SN4234567890', status='in_use', purchase_date=datetime.now().date() - timedelta(days=250), warranty_expiry=datetime.now().date() + timedelta(days=450), location='Office 205', department_id=2, assigned_to=4),
            Asset(asset_id='NET001', asset_type='network', brand='Cisco', model='Catalyst 2960-X', serial_number='SN5234567890', status='in_use', purchase_date=datetime.now().date() - timedelta(days=600), warranty_expiry=datetime.now().date() + timedelta(days=100), location='Server Room', department_id=1),
            Asset(asset_id='NET002', asset_type='network', brand='Ubiquiti', model='UniFi Dream Machine Pro', serial_number='SN5234567891', status='in_use', purchase_date=datetime.now().date() - timedelta(days=180), warranty_expiry=datetime.now().date() + timedelta(days=550), location='Server Room', department_id=1),
        ]
        for asset in assets:
            db.session.add(asset)
        
        db.session.commit()
        
        print("✓ Database seeded successfully!")
        print("\nDefault login credentials:")
        print("Admin - Username: admin, Password: admin123")
        print("Staff - Username: staff, Password: staff123")
        print("Viewer - Username: viewer, Password: viewer123")
