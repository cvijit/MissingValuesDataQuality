import streamlit as st
import numpy as np
import pandas as pd

def handle_missing_values(df):
    # Remove rows with missing values
    df_cleaned = df.dropna()
    return df_cleaned

def main():
    st.title("Data Quality Tool")
    st.write("Upload your dataset to handle missing values!")

    uploaded_file = st.file_uploader("Upload CSV or Excel file", type=["csv", "xlsx"])

    if uploaded_file is not None:
        try:
            df = pd.read_csv(uploaded_file) if uploaded_file.name.endswith('.csv') else pd.read_excel(uploaded_file)
            st.write("Original Dataset:")
            st.write(df)

            # Show button to view dataset with highlighted missing values
            if st.button("View Dataset with Missing Values"):
                st.write("Dataset with Missing Values:")
                df_with_missing_values = df.copy()
                missing_values_mask = df_with_missing_values.isnull()
                st.dataframe(df_with_missing_values.style.highlight_null(null_color='red'))

            # Handle missing values
            df_cleaned = handle_missing_values(df)
            st.write("Dataset after handling missing values:")
            st.write(df_cleaned)

            # Show button to delete rows with missing values
            if st.button("Delete Rows with Missing Values"):
                df_cleaned = handle_missing_values(df)
                st.write("Dataset after deleting rows with missing values:")
                st.write(df_cleaned)

            # Allow user to export the cleaned dataset
            export_format = st.selectbox("Export Format:", ["CSV", "Excel"])
            if st.button("Export"):
                if export_format == "CSV":
                    st.write("Exporting as CSV...")
                    df_cleaned.to_csv("cleaned_data.csv", index=False)
                    st.success("Data exported to cleaned_data.csv")
                elif export_format == "Excel":
                    st.write("Exporting as Excel...")
                    df_cleaned.to_excel("cleaned_data.xlsx", index=False)
                    st.success("Data exported to cleaned_data.xlsx")

        except Exception as e:
            st.error(f"Error occurred: {e}")

if __name__ == "__main__":
    main()
