# ---------- TASK 1: FILE WRITE ----------
# we will create a text file to store some notes about Python programming. We will write multiple lines to the file, then read it back and print the contents. We will also implement a simple keyword search to find lines containing a specific word.
# writing initial notes
f = open("python_notes.txt", "w", encoding="utf-8")

f.write("Topic 1: Variables store data. Python is dynamically typed.\n")
f.write("Topic 2: Lists are ordered and mutable.\n")
f.write("Topic 3: Dictionaries store key-value pairs.\n")
f.write("Topic 4: Loops automate repetitive tasks.\n")
f.write("Topic 5: Exception handling prevents crashes.\n")

# closing the file after writing
f.close()
print("File written successfully")

# appending some extra lines (added on my own)
f = open("python_notes.txt", "a", encoding="utf-8")
# appending some extra lines (added on my own)
f.write("Topic 6: Functions help reuse code.\n")
f.write("Topic 7: APIs allow communication between systems.\n")

f.close()
print("Extra lines appended")

# ---------- TASK 1: FILE READ ----------
# reading the file and printing contents

f = open("python_notes.txt", "r", encoding="utf-8")
lines = f.readlines()
f.close()

# printing line by line with numbering
count = 1
for line in lines:
    print(str(count) + ". " + line.strip())
    count += 1

print("Total lines:", len(lines))
# we can also print the total lines using len function on the list of lines.
# keyword search
key = input("Enter keyword to search: ").lower()

found = False
# we will search for the keyword in each line and print the matching lines. We will also keep track of whether we found any matches to print a message if no matches are found.
for line in lines:
    if key in line.lower():
        print(line.strip())
        found = True

if not found:
    print("No matching lines found")

# -------- API REQUEST --------
import requests

print("\n--- Fetching Products ---")
# we will fetch a list of products from the dummyjson API and print their details in a formatted way. We will also handle potential errors that may occur during the request, such as connection issues or timeouts.
try:
    url = "https://dummyjson.com/products?limit=20"
    res = requests.get(url, timeout=5)
    
    data = res.json()
    products = data["products"]
    
    print("ID | Title | Category | Price | Rating")
    print("-"*60)
    
    for p in products:
        print(p["id"], "|", p["title"], "|", p["category"], "|", p["price"], "|", p["rating"])

except requests.exceptions.ConnectionError:
    print("Connection failed. Check internet")
except requests.exceptions.Timeout:
    print("Request timed out")
except Exception as e:
    print("Error:", e)


# -------- FILTER + SORT --------
# we will filter the products to only include those with a rating of 4.5 or higher. Then we will sort the filtered products by price in descending order and print their titles, prices, and ratings.
high_rating = []
# filtering products with rating >= 4.5
for p in products:
    if p["rating"] >= 4.5:
        high_rating.append(p)

# sorting manually (keeping it simple instead of lambda)
high_rating.sort(key=lambda x: x["price"], reverse=True)

print("\nFiltered (rating >= 4.5):")
# printing title, price, and rating of the filtered and sorted products
for p in high_rating:
    print(p["title"], p["price"], p["rating"])



# -------- CATEGORY SEARCH --------
# we will make a request to fetch products in the "laptops" category and print their titles and prices. We will also handle potential errors that may occur during the request.
print("\n--- Laptops Category ---")

try:
    res = requests.get("https://dummyjson.com/products/category/laptops", timeout=5)
    data = res.json()
    
    for p in data["products"]:
        print(p["title"], "-", p["price"])

except Exception as e:
    print("Error:", e)
# we can also implement a search function that takes a keyword and searches for products with that keyword in the title. We will make a request to the API with the search query and print the matching products.

# -------- POST REQUEST --------
# we will create a new product by sending a POST request to the dummyjson API. We will include the product details in the request body as JSON. We will also handle potential errors that may occur during the request.
print("\n--- Sending POST ---")

try:
    new_product = {
        "title": "My Custom Product",
        "price": 999,
        "category": "electronics",
        "description": "A product I created via API"
    }
    
    res = requests.post("https://dummyjson.com/products/add", json=new_product, timeout=5)
    
    print("Response:", res.json())
# we can also implement a function to update an existing product by sending a PUT request with the updated details. We will handle potential errors as well.
except Exception as e:
    print("Error:", e)


# -------- SAFE DIVIDE --------
# we will implement a safe division function that takes two numbers and returns their division result. We will handle potential errors such as division by zero and invalid input types, and return appropriate error messages instead of crashing the program.
def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: Cannot divide by zero"
    except TypeError:
        return "Error: Invalid input types"


print(safe_divide(10, 2))
print(safe_divide(10, 0))
print(safe_divide("ten", 2))
# we can also implement a safe file read function that attempts to read a file and returns its contents. If the file does not exist, it should return an error message instead of crashing the program. We will also use a finally block to print a message indicating that the file operation was attempted, regardless of whether it succeeded or failed.

# -------- SAFE FILE READ --------
# we will implement a safe file read function that attempts to read a file and returns its contents. If the file does not exist, it should return an error message instead of crashing the program. We will also use a finally block to print a message indicating that the file operation was attempted, regardless of whether it succeeded or failed.
def read_file_safe(name):
    try:
        f = open(name, "r")
        data = f.read()
        f.close()
        return data
    except FileNotFoundError:
        print("Error: File", name, "not found")
    finally:
        print("File operation attempt complete")


print(read_file_safe("python_notes.txt"))
read_file_safe("ghost_file.txt")

# ---------- PRINT LOG FILE ----------
# we will attempt to read an error log file and print its contents. If the log file does not exist, we will catch the exception and print a message indicating that the log file was not found.
print("\n--- ERROR LOG CONTENT ---")

try:
    f = open("error_log.txt", "r")
    print(f.read())
    f.close()
except:
    print("Log file not found")


f = open("python_notes.txt", "w", encoding="utf-8")
f = open("python_notes.txt", "a", encoding="utf-8")
print("File written successfully")
print("Extra lines appended")

# ---------- LOGGING FIRST ----------
# we will implement a simple logging function that writes error messages to a log file with timestamps. We will then force some errors to demonstrate the logging functionality. Finally, we will read and print the contents of the log file to verify that the errors were logged correctly.
from datetime import datetime

def log_error(msg):
    f = open("error_log.txt", "a")
    f.write("[" + str(datetime.now()) + "] ERROR " + msg + "\n")
    f.close()

# force error 1
try:
    x = 10 / 0
except Exception as e:
    print("Logging division error...")
    log_error("division_error: " + str(e))

# force error 2
import requests

res = requests.get("https://dummyjson.com/products/999")

if res.status_code != 200:
    print("Logging 404 error...")
    log_error("product_lookup: 404 for ID 999")

# print log file
print("\n--- ERROR LOG ---")

f = open("error_log.txt", "r")
print(f.read())
f.close()

# -------- INPUT LOOP --------
# we will create a simple input loop that prompts the user to enter a product ID. We will make a request to the dummyjson API to fetch the product details for the entered ID and print the product title and price. The loop will continue until the user types "quit". We will also handle potential errors such as invalid input and product not found.
while True:
    user = input("Enter product ID (1–100) or quit: ")
    
    if user.lower() == "quit":
        break
    
    if not user.isdigit():
        print("Enter a valid number")
        continue
    
    pid = int(user)
    
    if pid < 1 or pid > 100:
        print("ID should be between 1 and 100")
        continue
    
    try:
        res = requests.get(f"https://dummyjson.com/products/{pid}", timeout=5)
        
        if res.status_code == 404:
            print("Product not found")
        else:
            data = res.json()
            print(data["title"], "-", data["price"])
    
    except Exception as e:
        print("Error:", e)
        
# we can also implement a safe input function that prompts the user for input and validates it. If the input is invalid, it should return an error message instead of crashing the program. We will use this function to get a valid product ID from the user before making the API request.
