import streamlit as st
import pandas as pd
import os

st.title("🧬 Schema Merge Tool")

st.markdown("Compare and merge two schema files from `/schemas/`.")

schemas_path = "schemas"
schema_files = [f for f in os.listdir(schemas_path) if f.endswith(".csv")]

col1, col2 = st.columns(2)

with col1:
    schema1 = st.selectbox("Select First Schema", schema_files, key="schema1")
with col2:
    schema2 = st.selectbox("Select Second Schema", schema_files, key="schema2")

if schema1 and schema2:
    df1 = pd.read_csv(os.path.join(schemas_path, schema1))
    df2 = pd.read_csv(os.path.join(schemas_path, schema2))

    st.subheader("🔍 Unique Fields in Each Schema")

    col1_unique = set(df1["Column Header"]) - set(df2["Column Header"])
    col2_unique = set(df2["Column Header"]) - set(df1["Column Header"])

    st.markdown("**Only in Schema 1:**")
    st.write(sorted(col1_unique))

    st.markdown("**Only in Schema 2:**")
    st.write(sorted(col2_unique))

    st.subheader("🧬 Merged Schema Preview")
    merged_headers = sorted(set(df1["Column Header"]).union(set(df2["Column Header"])))
    merged_df = pd.DataFrame({"Column Header": merged_headers})
    st.dataframe(merged_df)

    if st.button("💾 Export Merged Schema"):
        out_name = f"merged_{schema1.replace('.csv','')}_{schema2.replace('.csv','')}.csv"
        merged_df.to_csv(os.path.join(schemas_path, out_name), index=False)
        st.success(f"Merged schema saved as: {out_name}")
