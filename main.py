"""
This is just a simple python script to help with making the decision of what warehouse size a query should be ran on
in Snowflake. Increasing warehouse sizes will increase the execution speed but also increase the credits burned.
Not all queries are affected by warehouse size.

You need your current warehouse size and time to run as well as your proposed warehouse size and time.
Data is in sf_wh_data.json
"""
import json
import time


# Clean User Input - Str
def clean_str_input(string):
    string = string.strip()
    string = string.lower()
    return string


# Validate Warehouse Size
def validate_wh_size_input(size, size_options):
    if size in size_options:
        return "Valid"
    else:
        return "Invalid"


# Force valid Warehouse Size Selection
def get_wh_size(size_options, wh_type):
    wh_status = "Invalid"
    while wh_status == "Invalid":
        # Warehouse Size
        print(f"Warehouse Size Options: {size_options}")
        size = str(input(f"Enter {wh_type} WH Size: "))
        size = clean_str_input(size)
        # Validate the WH SIZE
        wh_status = validate_wh_size_input(size, size_options)
        if wh_status == "Invalid":
            print(f"Invalid choice of: {size}")
        else:
            return size


# Read in json data into Python Dictionary
def read_in_data(path):
    with open(path) as f:
        data = json.load(f)
    return data


# Calculate Credit Spend
def calc_credit_spend(data, size, t):
    for r in data:
        if r['Size'] == size:
            credit_spend = r['C_SEC'] * t
            credit_spend = round(credit_spend, 6)
            return credit_spend


# Make Decision
def make_decision(c_size, p_size, c_spend, n_spend):
    if c_spend <= n_spend:
        print(f"The Current Size of {c_size} is optimal by {round(n_spend - c_spend, 4)} credits.\n")
    else:
        print(f"The New Size of {p_size} is optimal by {round(c_spend - n_spend, 4)} credits, make the change!\n")


if __name__ == "__main__":
    print("Welcome to the Snowflake WH Decision Maker - type exit to leave")
    print("Please get your current Warehouse size, time to run query then get the proposed warehouse and how long it "
          "takes on the new warehouse")
    time.sleep(.2)
    while 1:
        # Read in SF Data
        sf_data = read_in_data('sf_wh_data.json')
        # Get all WH Sizes
        wh_sizes = []
        for row in sf_data:
            wh_sizes.append((row['Size'].lower()))

        # Enter in Current Stats - WH Size
        c_wh_size = get_wh_size(wh_sizes, "Current")

        # Enter in Current Stats - Time
        c_time = float(input(f"Enter Current Time in Seconds {c_wh_size} WH: "))

        # Calculate Current Spend (Credits)
        c_credit_spend = calc_credit_spend(sf_data, c_wh_size, c_time)

        # Enter in Current Stats - WH Size
        p_wh_size = get_wh_size(wh_sizes, "Proposed")

        # Enter in Current Stats - Time
        p_time = float(input(f"Enter Proposed Time in Seconds {p_wh_size} WH: "))

        # Calculate Proposed Spend (Credits)
        p_credit_spend = calc_credit_spend(sf_data, p_wh_size, p_time)

        # Make the decision
        make_decision(c_wh_size, p_wh_size, c_credit_spend, p_credit_spend)
