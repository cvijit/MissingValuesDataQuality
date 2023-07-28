import streamlit as st
import pandas as pd

def main():
    st.title("Duplicate Finder App")

    # File Upload
    st.header("Upload your CSV or Excel file")
    uploaded_file = st.file_uploader("Choose a file", type=["csv", "xlsx"])

    if uploaded_file is not None:
        df = read_data(uploaded_file)

        # Find duplicates
        duplicates = find_duplicates(df)

        # Highlight duplicates in the DataFrame
        df_style = df.style.apply(highlight_duplicates, subset=duplicates)

        # Show the DataFrame with highlighted duplicates
        st.header("Data with Duplicates Highlighted")
        st.dataframe(df_style)

        # Option to delete or ignore duplicates
        st.header("Options")
        option = st.radio("Choose an option:", ("Ignore Duplicates", "Delete Duplicates"))

        if option == "Ignore Duplicates":
            df_cleaned = df.drop_duplicates(keep='first')
        else:
            df_cleaned = df.drop_duplicates()

        # Export cleaned data to CSV or Excel
        st.header("Export Cleaned Data")
        export_format = st.radio("Choose export format:", ("CSV", "Excel"))

        if st.button("Export"):
            if export_format == "CSV":
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

def find_duplicates(df):
    duplicates = df.duplicated(keep=False)
    return duplicates

def highlight_duplicates(s):
    return ['background-color: yellow' if v else '' for v in s]

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
