import streamlit as st
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
import re


def main():
    st.title('ML2 Problemset 1 Task 1')
    with st.sidebar:
        st.write('Task selection')

    c_task = st.sidebar.selectbox(
        "select task",
        ("1.1 Clustering", "1.2 Test")
    )
    if c_task == "1.1 Clustering":
        task1()


def task1():
    with st.beta_expander("display code"):
        with st.echo('below'):
            def assign(x, y, m1_old, m2_old):
                c1 = [[], []]
                c2 = [[], []]
                for j in range(len(x)):
                    dist_m1 = (m1_old[0]-x[j])**2 + (m1_old[1]-y[j])**2
                    dist_m2 = (m2_old[0]-x[j])**2 + (m2_old[1]-y[j])**2
                    if dist_m1 < dist_m2:
                        c1[0].append(x[j])
                        c1[1].append(y[j])
                    else:
                        c2[0].append(x[j])
                        c2[1].append(y[j])
                return c1, c2

            def recenter(c1_old, c2_old):
                m1 = [sum(c1_old[0]) / len(c1_old[0]), sum(c1_old[1]) / len(c1_old[1])]
                m2 = [sum(c2_old[0]) / len(c2_old[0]), sum(c2_old[1]) / len(c2_old[1])]
                return m1, m2

            data = re.split('\n', Path('Data_1_1').read_text())
            x = []
            y = []
            for d in data:
                tmp = d.split('  ')
                x.append(float(tmp[0]))
                y.append(float(tmp[1]))
            min_x = min(x)
            max_x = max(x)
            min_y = min(y)
            max_y = max(y)
            pos_per = np.random.rand(2)
            m1 = [min_x + (max_x - min_x) * pos_per[0], min_y + (max_y - min_y) * pos_per[1]]
            m2 = [min_x + (max_x - min_x) * (1-pos_per[0]), min_y + (max_y - min_y) * (1-pos_per[1])]
            m1_old = m1
            m2_old = m2
            count = 0
            while True:
                count += 1
                c1, c2 = assign(x, y, m1, m2)
                m1_t, m2_t = m1, m2
                m1, m2 = recenter(c1, c2)
                if m1 == m1_t and m2 == m2_t:
                    break

    fig_start, bx = plt.subplots()
    bx.scatter(x, y, c='grey')
    bx.scatter([m1_old[0], m2_old[0]], [m1_old[1], m2_old[1]], c='black')

    fig_end, ax = plt.subplots()
    ax.scatter(c1[0], c1[1], c='#ff7f0e')
    ax.scatter(c2[0], c2[1], c='#1f77b4')
    ax.scatter([m1[0], m2[0]], [m1[1], m2[1]], c='black')
    fig_end.suptitle('loopcount: '+str(count))
    #plt.show()

    st.pyplot(fig_start)
    st.pyplot(fig_end)


if __name__ == "__main__":
    main()
