def some_function():
    print("Funcion in module")

print(__name__)
if __name__ == "__main__":
    print("This is the main script in module")
    some_function()
