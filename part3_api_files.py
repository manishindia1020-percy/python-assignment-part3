# ---------- TASK 1: FILE WRITE ----------

# writing initial notes
f = open("python_notes.txt", "w", encoding="utf-8")

f.write("Topic 1: Variables store data. Python is dynamically typed.\n")
f.write("Topic 2: Lists are ordered and mutable.\n")
f.write("Topic 3: Dictionaries store key-value pairs.\n")
f.write("Topic 4: Loops automate repetitive tasks.\n")
f.write("Topic 5: Exception handling prevents crashes.\n")

f.close()
print("File written successfully")

# appending some extra lines (added on my own)
f = open("python_notes.txt", "a", encoding="utf-8")

f.write("Topic 6: Functions help reuse code.\n")
f.write("Topic 7: APIs allow communication between systems.\n")

f.close()
print("Extra lines appended")

# ---------- TASK 1: FILE READ ----------

f = open("python_notes.txt", "r", encoding="utf-8")
lines = f.readlines()
f.close()

# printing line by line with numbering
count = 1
for line in lines:
    print(str(count) + ". " + line.strip())
    count += 1

print("Total lines:", len(lines))

# keyword search
key = input("Enter keyword to search: ").lower()

found = False

for line in lines:
    if key in line.lower():
        print(line.strip())
        found = True

if not found:
    print("No matching lines found")


import requests

print("\n--- Fetching Products ---")

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

high_rating = []

for p in products:
    if p["rating"] >= 4.5:
        high_rating.append(p)

# sorting manually (keeping it simple instead of lambda)
high_rating.sort(key=lambda x: x["price"], reverse=True)

print("\nFiltered (rating >= 4.5):")

for p in high_rating:
    print(p["title"], p["price"], p["rating"])



# -------- CATEGORY SEARCH --------

print("\n--- Laptops Category ---")

try:
    res = requests.get("https://dummyjson.com/products/category/laptops", timeout=5)
    data = res.json()
    
    for p in data["products"]:
        print(p["title"], "-", p["price"])

except Exception as e:
    print("Error:", e)


# -------- POST REQUEST --------

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

except Exception as e:
    print("Error:", e)


# -------- SAFE DIVIDE --------

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


# -------- SAFE FILE READ --------

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

