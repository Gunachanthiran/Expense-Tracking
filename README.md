**Room Maintenance Django Project**
This Django project helps in managing roommates, expenses, and PUB bills in a shared living space. It includes features like logging in, adding and managing roommates, tracking expenses, and calculating shared expenses.

**Clone the repository:**
git clone https://github.com/Gunachanthiran/Room-Maintenance.git
cd Room-Maintenance

**Create a virtual environment and activate it:**
python -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`

**Install the dependencies:**
pip install -r requirements.txt

**Apply the migrations:**
python manage.py migrate

**Create a superuser:**
python manage.py createsuperuser

**Start the development server:**
python manage.py runserver

**Configuration**
Ensure you have the necessary configurations in your settings.py file, such as database configurations, static files settings, etc.

**Usage**
Access the application at http://127.0.0.1:8000/ in your web browser. Log in with your superuser credentials to access the admin panel and manage the application.

**Views**
**Authentication**
Login: roommate_login(request) - Renders the login page.
Authenticate Login: login_auth(request) - Handles the login form submission, authenticates the user, and redirects to the dashboard.
Logout: roommate_logout(request) - Logs out the user and redirects to the login page.
**Dashboard**
Dashboard View: Dashboard(View) - Displays an overview of expenses and PUB bills for the selected month.
**Roommates**
Add Roommate: AddRoommateView(View) - Handles adding new roommates.
Edit Roommate: AddRoommateEdit(View) - Handles editing roommate details.
Delete Roommate: RoommateDelete(View) - Handles deleting a roommate.
**Expenses**
Add Expense: AddExpenseView(View) - Handles adding new expenses.
Edit Expense: ExpenseEdit(View) - Handles editing expense details.
Delete Expense: ExpenseDelete(View) - Handles deleting an expense.
PUB Bills
PUB Bill View: PubBill(View) - Displays and manages PUB bills.
Edit PUB Bill: PubBillEdit(View) - Handles editing PUB bill details.
Delete PUB Bill: PubBillDelete(View) - Handles deleting a PUB bill.
**Models**
AddRoommate: Stores information about roommates.
AddExpense: Stores information about expenses.
ExpensePaidAmount: Stores information about paid expenses.
PUBBillAmount: Stores information about PUB bills.
**Templates**
Ensure you have the following templates in your templates directory:
login.html
dashboard.html
addroommate.html
addexpense.html
calculate.html
pub_bill.html

**Contributing**
Contributions are welcome! Please fork the repository and submit a pull request.
