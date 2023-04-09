import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
hud_data_fmr = pd.read_excel("assets/sec_8_hud_data.xlsx")


def fmr_cost():
    zero_br_fmr = hud_data_fmr["0BR_FMR"]
    one_br_fmr = hud_data_fmr["1BR_FMR"]
    two_br_fmr = hud_data_fmr["2BR_FMR"]
    three_br_fmr = hud_data_fmr["3BR_FMR"]
    four_br_fmr = hud_data_fmr["4BR_FMR"]
    
    zero_br_graph = zero_br_fmr.mean()
    one_br_graph = one_br_fmr.mean()
    two_br_graph = two_br_fmr.mean()
    three_br_graph = three_br_fmr.mean()
    four_br_graph = four_br_fmr.mean()
    
    x = np.array(['0 Bed', '1 Bed', '2 Bed', '3 Bed', '4 Bed'])
    y = np.around([zero_br_graph, one_br_graph, two_br_graph, three_br_graph, four_br_graph], decimals = 2)
    plt.bar(x,y, color = 'green')
    for i in range(len(x)):
        plt.text(i, y[i]//2, y[i], ha = 'center',
                 )
    plt.title("Average national rent per unit based on the number of bedrooms")    
    plt.xlabel("Bedrooms for each unit")
    plt.ylabel("Average Rent Cost (USD)")    
    plt.show()
        
    return
