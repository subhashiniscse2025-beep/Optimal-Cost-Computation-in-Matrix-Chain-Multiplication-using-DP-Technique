import streamlit as st
from PROGRAM import matrix_chain_order, print_optimal_parens
st.set_page_config(
    page_title="Matrix Chain Multiplication",
    page_icon="📊"
)
st.title("Optimal Cost Computation in Matrix Chain Multiplication using DP")
st.write("Enter the dimensions separated by commas.")
dims_input = st.text_input(
    "Dimensions",
    "10,30,5,60,10"
)
if st.button("Compute"):
    dims = list(map(int, dims_input.split(",")))
    m, s = matrix_chain_order(dims)
    n = len(dims) - 1
    st.success(f"Minimum Scalar Multiplications: {m[1][n]}")
    st.success(
        f"Optimal Parenthesization: {print_optimal_parens(s,1,n)}"
    )
    st.subheader("DP Cost Table")
    table = []
    for i in range(1, n + 1):
        row = []
        for j in range(1, n + 1):
            if j < i:
                row.append("---")
            else:
                row.append(m[i][j])
        table.append(row)
    st.table(table)
