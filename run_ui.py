
import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="HeaderMatrix Assistant", layout="wide")

# Load Applet Matrix
def load_applet_matrix():
    try:
        df = pd.read_csv("Applet_Matrix.csv")
        return df
    except Exception as e:
        st.error(f"Error loading Applet_Matrix.csv: {e}")
        return pd.DataFrame()

# Sidebar Navigation
tab = st.sidebar.radio("Select Tab", [
    "Applet Explorer", 
    "Column Validator", 
    "Audit History Viewer", 
    "Upgrade Recommender"
])

df = load_applet_matrix()

if tab == "Applet Explorer":
    st.title("Applet Explorer")
    if df.empty:
        st.warning("No data loaded.")
    else:
        phase = st.selectbox("Filter by Execution Phase", ["All"] + sorted(df["Execution Phase"].dropna().unique()))
        if phase != "All":
            df = df[df["Execution Phase"] == phase]
        st.dataframe(df, use_container_width=True)

elif tab == "Column Validator":
    st.title("Column Validator")
    expected_columns = [
        "Applet Name", "Parent Workflow", "Execution Phase", "Order", "Status",
        "Trigger Condition", "Input Intent", "Output Goal", "Context Scope", "Assistant Dependency",
        "Strategic Layer", "Monetization Role", "Impact Score (Export Quality)", "Reuse Score", "Reuse Context",
        "Profit Layer Enabled", "Last Run Timestamp", "Run Success", "Runtime (ms)", "Output File(s)",
        "Error Logged", "Validation Status", "Bundle ID", "Release Tag", "Deployment Status",
        "Included in Zip", "Used in Launcher", "Synced to Notion", "Visual Verification Passed", "Notes / Comments"
    ]
    missing = [col for col in expected_columns if col not in df.columns]
    if missing:
        st.error(f"Missing columns: {missing}")
    else:
        st.success("All expected columns are present.")

elif tab == "Audit History Viewer":
    st.title("Audit History Viewer")
    audit_cols = ["Applet Name", "Run Success", "Validation Status", "Last Run Timestamp", "Error Logged"]
    audit_df = df[audit_cols] if not df.empty else pd.DataFrame(columns=audit_cols)
    st.dataframe(audit_df, use_container_width=True)

elif tab == "Upgrade Recommender":
    st.title("Upgrade Recommender")
    upgrade_cols = {
        "Assistant Dependency": "Expand to include mode (train/execute)",
        "Reuse Score": "Split into use case tags + numeric value",
        "Export Value Score": "Rename to Impact Score (Export Quality)",
        "Order": "Consider using Execution Priority Index"
    }
    st.write("Recommended Enhancements:")
    for col, suggestion in upgrade_cols.items():
        if col in df.columns:
            st.markdown(f"- **{col}** → *{suggestion}*")
