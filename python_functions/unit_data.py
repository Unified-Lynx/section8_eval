import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# MF_Inspection_report = pd.read_excel("assets/sec_8_prop_inspection.xls")

hud_data_sec = pd.read_excel(
    "assets/sec_8_hud_data.xlsx")

num_of_units = hud_data_sec["assisted_units_count"]
contract_status = hud_data_sec["tracs_status_name"]
contract_length = hud_data_sec["contract_term_months_qty"]
rent_fmr_ratio = hud_data_sec["rent_to_FMR_ratio"]
zero_br_count = hud_data_sec["0BR_count"]
one_br_count = hud_data_sec["1BR_count"]
two_br_count = hud_data_sec["2BR_count"]
three_br_count = hud_data_sec["3BR_count"]
four_br_count = hud_data_sec["4BR_count"]
five_br_count = hud_data_sec["5plusBR_count"]

def unit_count():
    print(num_of_units.sum())
    return
def br_count():
    zero =  zero_br_count.sum()
    one = one_br_count.sum()
    two = two_br_count.sum()
    three = three_br_count.sum()
    four = four_br_count.sum()
    five = five_br_count.sum()
    
    x = np.array(['zero', 'one', 'two', 'three', 'four', 'five'])
    y = np.array([zero, one, two, three, four, five])
    plt.bar(x,y, color = 'green')
    for i in range(len(x)):
        plt.text(i, y[i]//2, y[i], ha = 'center',
                 )
    plt.title("Amount of units for each quanitity of beds")    
    plt.xlabel("Bedrooms per unit")
    plt.ylabel("Quantity of units")    
    plt.show()
    
    return