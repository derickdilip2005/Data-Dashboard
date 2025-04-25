import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title('Simple Data Dashboard')

uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.subheader("Data Preview")
    st.write(df.head())

    st.subheader("Data Summary")
    st.write(df.describe())

    st.subheader('Filter Data')
    columns = df.columns.tolist()
    selected_column = st.selectbox("Select columns to filter by", columns)
    unique_values = df[selected_column].unique()
    selected_value = st.selectbox("Select value", unique_values)

    filtered_df = df[df[selected_column] == selected_value]
    st.write(filtered_df)

    st.subheader("Plot Data")
    x_column = st.selectbox("Select X-axis column", columns)
    y_column = st.selectbox("Select Y-axis column", columns)

    if st.button("Generate Plot"):
        st.line_chart(filtered_df.set_index(x_column)[y_column])
else:
    st.write("Waiting on file upload...")

    footer_html = """
    <style>
        .footer {
            position: fixed;
            left: 0;
            bottom: 0;
            width: 100%;
            background-color: #0e1117;
            padding: 20px;
            border-top: 1px solid #30363d;
            display: grid;
            grid-template-columns: 1fr auto;
        }
        .footer-center {
            margin: auto;
            text-align: center;
            grid-column: 1 / -1;
        }
        .footer-left {
            position: absolute;
            margin: auto;
            top: 15px;
            left: 40px;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            text-align: center;
            color: #ffffff;
        }
        .footer p {
            margin: 5px 0;
            color: #ffffff;
            font-size: 16px;
        }
        .social-links {
            display: flex;
            gap: 10px;
            margin-top: 3px;
        }
        .social-link {
            color: #ffffff;
            text-decoration: none;
        }
        .social-icon {
            width: 25px;
            height: 25px;
            border-radius: 30%;
        }
    </style>
    <div class='footer'>
        <div class='footer-center'>
            <p>Website Developed by Derick Dilip</p>
            <p>© 2025. All Rights Reserved.</p>
        </div>
        <div class='footer-left'>
            <p>Connect with me</p>
            <div class='social-links'>
                <a href='https://www.linkedin.com/in/derick-dilip-17751b282/' target='_blank' class='social-link'>
                    <img class='social-icon' src='data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyNCIgaGVpZ2h0PSIyNCIgdmlld0JveD0iMCAwIDI0IDI0Ij48cGF0aCBmaWxsPSIjMDBhY2VlIiBkPSJNMTkgMEg1YTUgNSAwIDAwLTUgNXYxNGE1IDUgMCAwMDUgNWgxNGE1IDUgMCAwMDUtNVY1YTUgNSAwIDAwLTUtNXpNOCAxOUg1VjhoM3YxMXpNNi41IDYuNzMyYy0uOTY2IDAtMS43NS0uNzktMS43NS0xLjc2NGMwLS45NzQuNzg0LTEuNzY0IDEuNzUtMS43NjRzMS43NS43OSAxLjc1IDEuNzY0YzAgLjk3NC0uNzgzIDEuNzY0LTEuNzUgMS43NjR6TTE5IDE5aC0zdi01LjYwNGMwLTMuMzY4LTQtMy4xMTMtNCAwVjE5aC0zVjhoM3YxLjc2NWMxLjM5Ni0yLjU4NiA3LTIuNzc3IDcgMi40NzZWMTl6Ii8+PC9zdmc+'>
                </a>
                <a href='https://github.com/derickdilip2005' target='_blank' class='social-link'>
                    <img class='social-icon' src='https://github.githubassets.com/assets/GitHub-Mark-ea2971cee799.png'>
                </a>
            </div>
        </div>
    </div>
    """
    st.markdown(footer_html, unsafe_allow_html=True)
