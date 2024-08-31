# Problem 1
# -------------------------------
import time
import csv
print("\-"*25)
print("PROBLEM 1")
print("-/"*25)
print("\n")
lambda_f = lambda x: x**3 if x >= 0 else 0

def def_f(x):
    if x >= 0:
        return x**3
    else:
        return 0

x_vals = range(-10000, 10000+1)

start_lambda = time.time()
results_lambda = [lambda_f(x) for x in x_vals]
end_lambda = time.time()

start_def = time.time()
results_def = [def_f(x) for x in x_vals]
end_def = time.time()

print(f"Lambda Time: {end_lambda - start_lambda} s ")
print(f"Def Time: {end_def - start_def} s")

        
# Problem 2
print("\n")
print("\-"*25)
print("PROBLEM 2")
print("-/"*25)
print("\n")
# ------------------------
a = [1, 2, 3, 4, 5]

#method 1
print("METHOD 1")
print("-"*25)
print("\n")
b = []
for val in a:
    b.append(val)

print("b:")
print(b)
b[0] = 7
print("new b:")
print(b)
print("a")
print(a)

#method 2
print("\n")
print("METHOD 2")
print("-"*25)
print("\n")

b = list(a)

print("b:")
print(b)
b[0] = 7
print("new b:")
print(b)
print("a")
print(a)


# Problem 3
print("\n")
print("\-"*25)
print("PROBLEM 3")
print("-/"*25)
print("\n")
stock_data = {}

with open('MAT 5712/homework/hw1/pbm3.csv', mode='r') as file:

    csv_reader = csv.reader(file)
    
    next(csv_reader)

    for row in csv_reader:

        symbol = row[0]
        m_cap = row[1]
        
        stock_data[symbol] = m_cap

print(stock_data)