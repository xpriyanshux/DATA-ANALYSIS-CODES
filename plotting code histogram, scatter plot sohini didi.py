#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import os

excel_file = pd.ExcelFile("C:/Users/priya/OneDrive/Desktop/test data/new dataSAM_NEGATIVE_diff1.xlsx")
save_path="C:/Users/priya/OneDrive/Desktop/test data"

pdf_path = os.path.join(save_path, 'plots.pdf')
pdf_pages = PdfPages(pdf_path)


for sheet_name in excel_file.sheet_names:
    df = excel_file.parse(sheet_name)
    x_values = df["Metabolite name"]
    y_values = df["AREA AVG"]
    fig, ax = plt.subplots(figsize=(10,10))
    ax.hist(y_values)
    ax.set_xlabel("Metabolite name")
    ax.set_ylabel("Area")
    ax.set_title(f'Histogram Plot - {sheet_name}')
    
    pdf_pages.savefig(fig)
    
    plt.show()
    
pdf_pages.close()
print(f'Saved all plots as {pdf_path}')

output_dir = 'output'
if not os.path.exists(output_dir):
    os.makedirs("C:/Users/priya/OneDrive/Desktop/test data")



# In[4]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[ ]:


import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import os

excel_file = pd.ExcelFile("C:/Users/priya/OneDrive/Desktop/test data/new dataSAM_NEGATIVE_diff1.xlsx")

for sheet_name in excel_file.sheet_names:
    df = excel_file.parse(sheet_name)
    x_values = df["Metabolite name"]
    y_values = df["AREA AVG"]
    fig, ax = plt.subplots(figsize=(10,10))
    ax.scatter(x_values, y_values)
    ax.set_xlabel("Metabolite")
    ax.set_ylabel('Area')
    ax.set_title(f'Scatter Plot - {sheet_name}')

        # Enable interactive mode
    plt.ion()

        # Show the plot and allow for interaction
    plt.show()


# In[ ]:




