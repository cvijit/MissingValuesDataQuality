import streamlit as st
import pandas as pd

def main():
    st.title("Data Validation and Manipulation App")

    # File Upload
    st.header("Upload your CSV or Excel file")
    file_format = st.selectbox("Select file format:", ["CSV", "Excel"])

    if file_format == "CSV":
        uploaded_file = st.file_uploader("Choose a file", type=["csv"])
    else:
        uploaded_file = st.file_uploader("Choose a file", type=["xlsx"])

    if uploaded_file is not None:
        df = read_data(uploaded_file)

        # Data Quality Checks
        st.header("Data Quality Checks")
        st.subheader("Data Summary")
        st.write(df.describe())

        st.subheader("Missing Value Analysis")
        missing_values = df.isnull().sum()
        st.write(missing_values)

        st.subheader("Duplicate Values")
        duplicate_rows = df.duplicated()
        st.write(duplicate_rows)

        # Data Validation Checks
        st.header("Data Validation Checks")
        st.subheader("Data Type Validation")
        column_datatypes = df.dtypes
        st.write(column_datatypes)

        st.subheader("Unique Values")
        unique_values = df.nunique()
        st.write(unique_values)

        # Data Manipulation
        st.header("Data Manipulation")
        if st.checkbox("Remove Rows with Missing Values"):
            df_cleaned = df.dropna()

        if st.checkbox("Drop Duplicate Rows"):
            df_cleaned = df.drop_duplicates()

        st.subheader("Data After Manipulation")
        st.write(df_cleaned)

        # Export cleaned data to CSV or Excel
        st.header("Export Cleaned Data")
        if st.button("Export"):
            if file_format == "CSV":
                export_csv(df_cleaned)
            else:
                export_excel(df_cleaned)

def read_data(file):
    if file.type == "csv":
        df = pd.read_csv(file)
    elif file.type == "xlsx":
        df = pd.read_excel(file, engine='openpyxl')
    else:
        st.error("Invalid file type. Only CSV and Excel files are supported.")
        df = None
    return df

def export_csv(df):
    csv_file = "cleaned_data.csv"
    df.to_csv(csv_file, index=False)
    st.success(f"Data exported to {csv_file}")

def export_excel(df):
    excel_file = "cleaned_data.xlsx"
    df.to_excel(excel_file, index=False, engine='openpyxl')
    st.success(f"Data exported to {excel_file}")

if __name__ == "__main__":
    main()
