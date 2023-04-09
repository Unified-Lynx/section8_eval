import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
pd.set_option('display.max_colwidth', None)
pd.set_option('display.max_rows', None)

hud_data_property = pd.read_excel("assets/sec_8_hud_prop.xlsx")

def city_state_data():
    state_code = hud_data_property.pivot_table(index = ["state_code"], aggfunc = 'size')
    df = pd.DataFrame(state_code)
    df.plot(kind = 'bar')
    plt.grid(axis = 'y')
    plt.title('Number of units per state')
    plt.xlabel('State')
    plt.ylabel('Unit count')
    plt.show()
    return