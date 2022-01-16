import hashlib

# input puzzle
string = "bgvyzdsv"

# function that finds the number
def md5_number(string):
    done = 0
    while True:
        key = string + str(done)
        result = hashlib.md5(key.encode())
        if result.hexdigest()[0:6] == "000000":
            print(result.hexdigest())
            return done
            
        done += 1

# executes function
result = md5_number(string)

# prints out the number
print(result)
# print(f"The hexadecimal equivalent of hash is {result.hexdigest()}")