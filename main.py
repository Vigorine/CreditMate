import json
from utils import clear, print_dict, update_json

def reset(msg):
	clear()
	print(msg)
	login()

customer_data = {}
with open("customer_data.json") as f:
	customer_data = json.load(f)

employee_data = {}
with open("employee_data.json") as f:
	employee_data = json.load(f)


def login():
	valid = ""
	while valid.lower() != "employee" and valid.lower() != "customer":
		clear()
		valid = input("Are you trying to login as an 'employee' or 'customer'? ")
	valid = valid.lower()

	if valid == "employee":
		id = input("Enter your employee ID: ")

		if id in employee_data:
			password = input("Enter password: ")

			if password == employee_data[id]["password"]:
				name = employee_data[id]["name"]

				clear()
				print(f"Welcome {name} to the employee page!")
				employee_menu(id)

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


def employee_menu(id):
	if employee_data[id]["role"] == "manager":
		print("\nCustomers that are 20% or less within their credit limit:\n")
		for i in customer_data:
			customer = customer_data[i]
			if customer["credit_limit"] * 0.8 <= customer["current_credit_usage"]:
				print_dict(customer)

		signup_employee = ""
		while signup_employee.lower() != "yes" and signup_employee.lower() != "no":
			signup_employee = input("Do you wish to register an employee? ")
		signup_employee = signup_employee.lower()
			
		if signup_employee == "yes":
			setup_employee()
		clear()
		
	signup_customer = ""
	while signup_customer.lower() != "register" and signup_customer.lower() != "update" and signup_customer.lower() != "neither":
		signup_customer = input("Do you wish to register or update a customer or neither? ")
	signup_customer = signup_customer.lower()

	if signup_customer == "register":
		setup_customer()
	elif signup_customer == "update":
		update_customer()
	clear()
			
def customer_menu():
	pass


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
			"credit_limit": (monthly_income*12)*0.4,
			"current_credit_usage": 0,
			"withdrawals": [],
			"deposits": [],
			"fine": 0
		}
	}
	
	update_json("customer_data.json", customer_data, new_customer)


def setup_employee():
	employee_id = input("Enter employee's ID: ")
	name = input("Enter employee's name: ")
	role = input("Enter employee's role: ")
	password = input("Enter employee's password: ")
	new_employee = {
		employee_id: {
			"name": name,
			"role": role,
			"password": password
		}
	}
	
	update_json("employee_data.json", employee_data, new_employee)


def update_customer():
	pass


def update_employee():
	pass


def withdrawal():
	pass


def deposit():
	pass


login()
