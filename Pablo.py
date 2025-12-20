import streamlit as st
from Leke import Budget_for_me
import matplotlib.pyplot as plt
import pandas as pd

# Page Config
st.set_page_config(
    page_title="Smart Budget App",
    page_icon="💰",
    layout="centered"

)

st.title("Budgetting App")
st.balloons()

# CURRENCY SELECTION AND INCOME INPUT
currency = st.selectbox("Select your currency", ["$ USD", "€ EUR", "₦ NGN", "£ GBP", "KSh KES", "GH₵ GHS", "R ZAR", "FCFA XAF", "CFA XOF", "TSh TZS"]) 

symbol = currency.split()[0]
Total_income = st.number_input("Enter your total income for the month :", min_value=0.0, step=1000.0)


if st.button('Budget for me'):
    result = Budget_for_me(Total_income)
    st.success(f"Here's a calm budget ")

    # Cards using columns
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Needs", f"{symbol}{result['Needs']:.2f}")
        st.metric("Savings", f"{symbol}{result['Savings']:.2f}")
    with col2:
        st.metric("Investment", f"{symbol}{result['Investment']:.2f}")
        st.metric("Wants", f"{symbol}{result['Wants']:.2f}")
    with col3:
        st.metric("Emergency", f"{symbol}{result['Emergency']:.2f}")
        st.metric("Tithe", f"{symbol}{result['Tithe']:.2f}")

    # Pie Chart
    st.subheader("📊 Budget Breakdown")
    breakdown = pd.DataFrame({
        'Category': list(result.keys()),
        'Amount': list(result.values())
    })
    fig, ax = plt.subplots()
    ax.pie(breakdown['Amount'], labels=breakdown['Category'], autopct='%1.1f%%', startangle=140)
    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle
    st.pyplot(fig)


elif st.button("Leave my money"):
    st.error("Okay Greedy fool!")

st.divider()
st.caption('Created by Tofunmi! Inspired by Leke')
