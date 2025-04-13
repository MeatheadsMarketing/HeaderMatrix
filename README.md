
# 🧠 HeaderMatrix

**Modular Tabbed Schema Builder & Validator**

---

## 🚀 Overview
HeaderMatrix is a Streamlit-based assistant that governs the schema architecture of assistants, applets, chains, deployments, and more. It enables:

- Tab-specific schema validation
- Row creation with save-to-CSV logic
- GPT-ready field suggestion scaffolding
- Master viewer tab to explore all data

---

## 📁 Folder Structure

```
HeaderMatrix/
├── run_ui.py
├── Applet_Matrix.csv
├── header_matrix_manifest.json
├── schemas/
│   └── tab_<type>.csv          # 10 CSV schemas by tool category
├── tabs/
│   └── tab_<type>.py           # 10 matching Streamlit tab modules
├── data/
│   └── tab_<type>_entries.csv  # User entries stored per tab
└── .github/
    └── workflows/
        └── deploy_headermatrix.yml
```

---

## 🖥️ Local Run Instructions

```bash
git clone https://github.com/MeatheadsMarketing/HeaderMatrix.git
cd HeaderMatrix
pip install streamlit pandas
streamlit run run_ui.py
```

---

## ☁️ Streamlit Cloud Deploy

1. Go to [streamlit.io/cloud](https://streamlit.io/cloud)
2. Create a new app
3. Select:
   - Repo: `MeatheadsMarketing/HeaderMatrix`
   - File: `run_ui.py`
4. Click **Deploy**

---

## ✅ Notion Integration (Optional)

If you enable Notion sync for saving entries:

### Required Secrets

| Secret Key           | Purpose                         |
|----------------------|----------------------------------|
| `NOTION_TOKEN`       | Integration token from Notion   |
| `NOTION_DATABASE_ID` | Target database UUID string     |

These are used by: `notion_sync_headermatrix.py` and `notion_bulk_sync_headermatrix.py`.

---

## 📦 Version

**HEAD-v1**

---

## 🧠 Designed by: MeatheadsMarketing

For modular assistant systems, schema intelligence, and Streamlit-first architecture.
