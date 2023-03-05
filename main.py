import json, time
from utils import clear, print_dict, update_json

def reset():
	clear()
	menu()

customer_data = {}
with open("customer_data.json") as f:
	customer_data = json.load(f)

employee_data = {}
with open("employee_data.json") as f:
	employee_data = json.load(f)

def menu():
	valid = ""
	while valid.lower() != "employee" and valid.lower() != "customer":
		clear()
		valid = input("Are you trying to login as an 'employee' or 'customer'? ")
	valid = valid.lower()
	login(valid)


def login(valid):

	if valid == "employee":
		id = input("Enter your employee ID: ")

		if id in employee_data:
			password = input("Enter password: ")

			if password == employee_data[id]["password"]:
				name = employee_data[id]["name"]

				clear()
				print(f"Welcome {name} to the employee page!")
				employee_menu(id)
		time.sleep(2)
		reset()

	elif valid == "customer":
		user = input("Enter username of account: ")
		verif = False
		index = ""
		for i in customer_data:
			if user == customer_data[i]["username"]:
				verif = True
				index = i
		if verif:
			password = input("Enter password: ")
			if customer_data[index]["password"] == password:
				clear()
				print(f"Welcome {index} to the customer page!")
				customer_menu()
		time.sleep(2)
		reset()


def employee_menu(id):
	if employee_data[id]["role"] == "manager":
		print("\nCustomers that are 20% or less within their credit limit:\n")
		count = 0
		for i in customer_data:
			customer = customer_data[i]
			if customer["credit_limit"] * 0.8 <= customer["current_credit_usage"]:
				count += 1
				print_dict(customer)
		if count == 0:
			print("There are no customers that are 20% or less within their credit limit.\n")

		signup_employee = ""
		while signup_employee.lower() != "register" and signup_employee.lower() != "update" and signup_employee.lower() != "neither":
			signup_employee = input("Do you wish to register or update a employee or neither? ")
		signup_employee = signup_employee.lower()

		if signup_employee == "register":
			setup_employee()
		elif signup_employee == "update":
			update_employee()
		clear()
		
	signup_customer = ""
	while signup_customer.lower() != "register" and signup_customer.lower() != "update" and signup_customer.lower() != "neither":
		signup_customer = input("Do you wish to register or update a customer or neither? ")
	signup_customer = signup_customer.lower()

	if signup_customer == "register":
		setup_customer()
	elif signup_customer == "update":
		update_customer()
	reset()

def setup_customer():
	name = input("Enter customer's name: ")
	username = input("Enter customer's username: ")
	password = input("Enter customer's password: ")
	address = input("Enter customer's address: ")
	phone_no = input("Enter customer's phone number: ")
	monthly_income = int(input("Enter customer's monthly income: "))

	if monthly_income < 600:
		reset("Monthly income is too low!")
		return
	
	new_customer = {
		name: {
			"username": username,
			"password": password,
			"address": address,
			"phone_no": phone_no,
			"monthly_income": monthly_income,
			"credit_limit": round((monthly_income*12)*0.4),
			"current_credit_usage": 0,
			"withdrawals": [],
			"deposits": [],
			"fine": 0
		}
	}
	customer_data.update(new_customer)
	update_json("customer_data.json", customer_data)


def setup_employee():
	employee_id = input("Enter employee's ID: ")
	name = input("Enter employee's name: ")
	role = ""
	while role.lower() != "manager" and role.lower() != "employee":
		role = input("Enter employee's role: ")
	password = input("Enter employee's password: ")
	new_employee = {
		employee_id: {
			"name": name,
			"role": role,
			"password": password
		}
	}
	employee_data.update(new_employee)
	update_json("employee_data.json", employee_data)


def update_customer():
	customer_name = input("Enter customer's name: ")
	if customer_name in customer_data:
		key = input("Enter key to change: ")
		change = input("Enter new value: ")
		customer_data[customer_name][key] = change
		update_json("customer_data.json", customer_data)

def update_employee():
	employee_id = input("Enter employee's ID: ")
	if employee_id in employee_data:
		key = input("Enter key to change: ")
		change = input("Enter new value: ")
		employee_data[employee_id][key] = change
		update_json("employee_data.json", employee_data)



def customer_menu():
	pass


def withdrawal():
	pass


def deposit():
	pass


menu()