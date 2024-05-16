# Initialize an empty list to store search values
search_values = []

# Dictionary mapping human-readable table headers to corresponding database fields or internal identifiers
header_dic = {
    'Employee ID': 'emp_id',  # Maps "Employee ID" header to the 'emp_id' field
    'Name': 'name',           # Maps "Name" header to the 'name' field
    'Lastname': 'lname',      # Maps "Lastname" header to the 'lname' field
    'Age': 'age',             # Maps "Age" header to the 'age' field
    'Salary': 'salary',       # Maps "Salary" header to the 'salary' field
    'Position': 'position',   # Maps "Position" header to the 'position' field
    'Email': 'email'          # Maps "Email" header to the 'email' field
}

# Dictionary to store different categories of UI widgets
widgets = {
    'tableWidget': [],        # List to store table widgets
    'buttons': [],            # List to store button widgets
    'radiobuttons': [],       # List to store radio button widgets
    'searched_table': [],     # List to store searched table widgets
    'employee_fields': [],    # List to store employee field widgets
    'labels': [],             # List to store label widgets
    'plots': [],              # List to store plot widgets
    'logo': []                # List to store logo widgets
}

# Flag indicating whether the signal for testing is active
SIGNAL_FOR_TEST = True

# String variable to track the current page in the UI, initialized to 'Login'
CURRENT_PAGE = 'Login'

# Initialize an empty string to store the username of the current user
usr = ""

