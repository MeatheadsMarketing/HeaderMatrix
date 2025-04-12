import streamlit as st
import pandas as pd
import os

st.title("Framework Registry Schema")

st.markdown("This tab governs the `Framework Registry` layer. Below is the schema structure used to define this system layer.")

schema_path = f"schemas/tab_framework_registry.csv"
output_path = f"data/tab_framework_registry_entries.csv"
if os.path.exists(schema_path):
    df = pd.read_csv(schema_path)
    st.dataframe(df, use_container_width=True)

    st.markdown("### ➕ Add New Entry")

    # Placeholder for AI suggestion logic
    if st.button("🧠 Suggest All Fields (via GPT)"):
        st.info("Field suggestion triggered (integration logic to be added).")

    with st.form("entry_form", clear_on_submit=True):
        inputs = {{}}
        for col in df["Column Header"]:
            inputs[col] = st.text_input(col, placeholder=f"Enter or auto-fill for '{col}'")
        submitted = st.form_submit_button("Add Entry")
        if submitted:
            new_row = pd.DataFrame([inputs])
            if os.path.exists(output_path):
                existing = pd.read_csv(output_path)
                new_df = pd.concat([existing, new_row], ignore_index=True)
            else:
                new_df = new_row
            new_df.to_csv(output_path, index=False)
            st.success(f"✅ Entry saved to {output_path}")
            st.dataframe(new_row)
else:
    st.error(f"Schema file not found: {schema_path}")
