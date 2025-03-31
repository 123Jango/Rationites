# Rationites
Here’s an updated version of the `README.md` file to reflect the deployment on Streamlit Cloud:

---

# Rationites - Smarter Stock Analysis

Rationites is a stock analysis tool built using Streamlit, designed to provide users with clear and insightful visualizations of stock data. The application pulls historical stock data, financial data (including revenue and net income), and displays it interactively with charts.

## Features

- **Interactive Stock Price Chart**: Visualize the stock price (closing price) over different time ranges.
- **Revenue vs Net Income Chart**: Compare the stock's total revenue and net income across different years.
- **Customizable Time Range**: Choose from multiple time ranges to analyze historical data (1 Year, 6 Months, 1 Month, 7 Days).
- **Real-Time Data Fetching**: The app fetches real-time stock data and financial data using the Yahoo Finance API.

## Technologies Used

- **Streamlit**: For building the interactive web application.
- **yFinance**: To fetch historical stock data and financial information from Yahoo Finance.
- **Plotly**: To create interactive, dynamic plots.

## Live Application

You can access the live application here:  
[Rationites - Smarter Stock Analysis](https://rationites-123jango.streamlit.app/)

## Setup Instructions

### Prerequisites

- Python 3.6 or higher
- The following Python libraries:
  - `streamlit`
  - `yfinance`
  - `pandas`
  - `plotly`

### Installation

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/your-username/Rationites.git
    cd Rationites
    ```

2. **Install Required Libraries**:
    Create a virtual environment and install the required packages.
    ```bash
    python -m venv venv
    source venv/bin/activate  # For Linux/Mac
    venv\Scripts\activate     # For Windows
    pip install -r requirements.txt
    ```

3. **Run the Application**:
    After installing the necessary libraries, you can run the Streamlit app locally using the following command:
    ```bash
    streamlit run app.py
    ```

### Input

- **Stock Symbol**: The app takes a stock symbol as input (e.g., TSLA, AAPL) for analysis.
- **Time Range**: You can select the time range for analyzing stock price data:
  - 1 Year
  - 6 Months
  - 1 Month
  - 7 Days

### Features Explained

1. **Stock Data Fetching**:  
   The app uses the `yfinance` library to fetch stock data for the selected stock symbol. It pulls historical data for the last year by default, and the user can filter the data by different time ranges.

2. **Revenue and Net Income Analysis**:  
   It fetches financial data including `Total Revenue` and `Net Income` for the past years and visualizes this data in a grouped bar chart.

3. **Interactive Visualization**:  
   The app uses `plotly` to plot the data. The charts are interactive, and users can hover over data points to see detailed information.

### Example Use Case

1. **Input Stock Symbol**: Enter a stock symbol, for example, `AAPL` for Apple.
2. **Select Time Range**: Choose one of the available time ranges (e.g., "1 Year").
3. **View Data**: See the stock's market price, revenue, and net income over time.

### Screenshots

![image](https://github.com/user-attachments/assets/c1b0d0e3-fd80-43fe-8621-26966e64e11e)

*Interactive chart showing stock price over time.*

![image](https://github.com/user-attachments/assets/6d6e254c-21bf-465a-8841-f42ad6635351)

*Grouped bar chart comparing revenue and net income.*

---

### Contributing

If you'd like to contribute to the development of this project, feel free to fork the repository and submit a pull request with your changes.

### License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

### Conclusion

Rationites allows users to analyze stocks interactively with ease. With features like time range selection and financial data visualization, it’s a useful tool for anyone interested in financial analysis.

---

This updated `README.md` now includes the link to the deployed app on Streamlit Cloud and instructions for both local and cloud access. Let me know if you'd like further modifications!
