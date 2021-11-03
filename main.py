"""

"""
import json
import time


# Clean User Input - Str
def clean_str_input(string):
    string = string.strip()
    return string


# Read in json data into Python Dictionary
def read_in_data(path):
    with open(path) as f:
        data = json.load(f)
    return data


# Calculate Credit Spend
def calc_credit_spend(data, size, time):
    for row in data:
        if row['Size'] == size:
            credit_spend = row['C_SEC'] * time
            credit_spend = round(credit_spend, 6)
            return credit_spend


# Make Decision
def make_decision(c_size, n_size, c_spend, n_spend):
    if c_spend <= n_spend:
        print(f"The Current Size of {c_size} is optimal by {n_spend - c_spend} credits.")
    else:
        print(f"The New Size of {n_size} is optimal by {c_spend - n_spend} credits, make the change!")


if __name__ == "__main__":
    print("Welcome to the Snowflake WH Decision Maker - type exit to leave")
    time.sleep(.2)
    while 1:
        # Read in SF Data
        sf_data = read_in_data('sf_wh_data.json')
        # Enter in Current Stats - WH Size
        c_wh_size = str(input("Enter Current WH Size: "))
        c_wh_size = clean_str_input(c_wh_size)
        # Validate the WH SIZE
        # TODO
        # Enter in Current Stats - Time
        c_time = float(input("Enter Current Time in Seconds: "))
        print(c_time)


'''

# Get input from person about current wh size and time
c_wh_size = 'X-Small'
c_time = 0.5
# Get input from person about new wh size and time
n_wh_size = 'Small'
n_time = 1.0

c_credit_spend = calc_credit_spend(sf_data, c_wh_size, c_time)
n_credit_spend = calc_credit_spend(sf_data, n_wh_size, n_time)

print(c_credit_spend)
print(n_credit_spend)

make_decision(c_wh_size, n_wh_size, c_credit_spend, n_credit_spend)

'''