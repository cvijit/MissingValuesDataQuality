import streamlit as st
import pandas as pd
import dtale
import klib

def handle_missing_values_with_klib(df):
    # Handle missing values using klib
    df_cleaned = klib.data_cleaning(df)
    return df_cleaned

def handle_missing_values_with_dtale(df):
    # Handle missing values using dtale
    dtale_app = dtale.show(df)
    return df

def main():
    st.title("Data Analysis and Manipulation App")

    # Upload file
    uploaded_file = st.file_uploader("Upload CSV or Excel file", type=["csv", "xlsx"])

    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file) if uploaded_file.name.endswith('.csv') else pd.read_excel(uploaded_file)

        st.subheader("Preview of the Dataset:")
        st.dataframe(df)

        if st.button("Use klib for Missing Data Handling"):
            df_cleaned_klib = handle_missing_values_with_klib(df)
            st.subheader("Dataset after handling missing values using klib:")
            st.dataframe(df_cleaned_klib)

        if st.button("Use dtale for Missing Data Handling"):
            df_cleaned_dtale = handle_missing_values_with_dtale(df)
            st.subheader("Dataset after handling missing values using dtale:")
            st.dataframe(df_cleaned_dtale)

        # Export the cleaned dataset
        export_format = st.selectbox("Export Format:", ["CSV", "Excel"])

        if st.button("Export Cleaned Data"):
            if export_format == "CSV":
                df.to_csv("cleaned_data.csv", index=False)
                st.success("Data exported to cleaned_data.csv")
            elif export_format == "Excel":
                df.to_excel("cleaned_data.xlsx", index=False)
                st.success("Data exported to cleaned_data.xlsx")

if __name__ == "__main__":
    main()
