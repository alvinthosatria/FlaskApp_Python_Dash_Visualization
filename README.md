# Flask App (REST APIs) - Python Data Visualization with Dash & Plotly <br />
S&P 500 Companies with Financial Information Dataset from [Kaggle](https://www.kaggle.com/datasets/franoisgeorgesjulien/s-and-p-500-companies-with-financial-information)
- “/Sector” that returns a list of unique sectors in the csv file.
- “/EBITDA” that takes in url parameters (i.e. ?Sector=xxx), that allow
users to query EBITDAs of a certain sector (e.g. if user provides with
URL http://127.0.0.1:5000?Sector=Materials, it will return a list of
numbers with all EBITDAs from that sector)
- Utilizing Dash and plotly to render Pie chart and multi-select component which uses the selection values to query the API for getting the EBITDA for multiple Sectors
<img width="1419" alt="Screenshot 2024-08-23 at 9 45 14 PM" src="https://github.com/user-attachments/assets/27d0f85f-5012-44cf-ac77-9f3b60a7529d">
