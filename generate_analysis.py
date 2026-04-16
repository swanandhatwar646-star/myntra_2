import pandas as pd
import streamlit as st
from cloud_io import MySQLIO
from constants import SESSION_PRODUCT_KEY
from utils import fetch_product_names_from_cloud
from data_report.generate_data_report import DashboardGenerator

mysql_con = MySQLIO()


def create_analysis_page(review_data: pd.DataFrame):
    if review_data is not None and not review_data.empty:
        st.dataframe(review_data)
        if st.button("Generate Analysis"):
            dashboard = DashboardGenerator(review_data)

            # Display general information
            dashboard.display_general_info()

            # Display product-specific sections
            dashboard.display_product_sections()


try:
    if st.session_state.data:
        # For cloud deployment, use session state data instead of MySQL
        if mysql_con.is_cloud or mysql_con.connection is None:
            # Get data from session state (stored by scrapper)
            if 'scrapped_data' in st.session_state:
                data = st.session_state.scrapped_data
            else:
                data = pd.DataFrame({
                    'Product': ['Sample Product'] * 5,
                    'Rating': [4, 5, 3, 4, 5],
                    'Review': [
                        'Great product, loved it!',
                        'Good quality material',
                        'Average product, could be better',
                        'Nice fit and comfortable',
                        'Excellent value for money'
                    ],
                    'Date': ['2024-01-15', '2024-01-14', '2024-01-13', '2024-01-12', '2024-01-11']
                })
        else:
            # Local development - get from MySQL
            data = mysql_con.get_reviews(product_name=st.session_state[SESSION_PRODUCT_KEY])
        
        create_analysis_page(data)

    else:
        with st.sidebar:
            st.markdown("""
            No Data Available for analysis. Please Go to search page for analysis.
            """)
except AttributeError:
    product_name = None
    st.markdown(""" # No Data Available for analysis.""")
