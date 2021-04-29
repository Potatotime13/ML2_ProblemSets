import streamlit as st
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import numpy as np
import pandas as pd
from pathlib import Path
import re

data = re.split('\n', Path('Data_1_1').read_text())
data_list = []
for d in data:
    tmp = d.split('  ')
    data_list.append([float(tmp[0]), float(tmp[1])])

st.title('ML2 Problemset 1 Task 1')
st.line_chart(data)
