import streamlit as st

st.title("Power Consumption cost calculator")
units = st.number_input("Enter number of units of electricity", min_value=0, step=1)

if st.button("Calculate"):
    cost = 0
    if units > 500:
        fixed_cost = 50
        cost += 350
        cost += 1380
        cost += 6.6 * (units - 500)
    elif units > 200:
        fixed_cost = 30
        cost += 2 * 100
        cost += 3 * (units - 200)
    elif units > 100:
        fixed_cost = 20
        cost += 1.5 * (units - 100)
    else:
        fixed_cost = 0
        cost += 0
    tax = round(cost * 0.05, 2)
    total = fixed_cost + cost + tax

    st.markdown(
        f"""
    | Charges             | cost         |
    | ------------------- | ------------ |
    | Electricity charges | {cost}       |
    | Taxes (@ 5%)        | {tax}        |
    | Fixed Cost          | {fixed_cost} |
    | **Total**           | **{total}**  |
    """
    )
