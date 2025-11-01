FLIGHT PRICE DASHBOARD

An interactive data visualization web application built with Streamlit and Python to analyze and compare flight prices based on airlines, travel classes, routes, number of stops, and duration.

SETUP INSTRUCTIONS

PREREQUISITES
• Python 3.8 or higher
• pip (Python package manager)
• A CSV dataset file (example: airline_flights_csv.csv)

INSTALLATION STEPS

Clone the repository or download the source code

Open the project folder in your code editor or terminal

Install the required libraries by running:
pip install -r requirements.txt

DATASET CONFIGURATION

Place your dataset file (for example: airline_flights_csv.csv) in the project folder.
Make sure the dataset contains the following key columns:

airline – Airline name
class – Flight class (Economy, Business, etc.)
source_city – Departure city
destination_city – Arrival city
price – Ticket price
days_left – Number of days left before departure
stops – Number of stops in the flight
duration – Flight duration (in hours or minutes)

If your dataset uses different column names, rename them or update the code accordingly.

RUNNING THE APPLICATION

To start the dashboard, open a terminal in the project folder and run:
streamlit run app.py

After the application starts, open your browser and go to:
http://localhost:8501

FEATURES

• Interactive filters for airline, class, source, and destination
• Visual analysis of price distribution
• Days left vs. price scatter plot
• Airline-wise price comparison using boxplots
• Stops and duration vs. price analysis
• Option to view filtered raw data
• Cached data loading for faster performance

TECHNOLOGIES USED

Python – Core programming language
Streamlit – For creating the interactive web dashboard
Pandas – For data manipulation and cleaning
NumPy – For numerical operations
Matplotlib and Seaborn – For data visualization

TROUBLESHOOTING

File not found: Make sure the dataset file airline_flights_csv.csv is placed in the same folder as app.py.

Empty graphs: Check that your filter selections are not removing all records.

Slow performance: Large datasets can be optimized using Streamlit caching (@st.cache_data).

FUTURE ENHANCEMENTS

• Integration with live flight APIs for real-time fare updates
• Predictive modeling for price forecasting using machine learning
• Mobile-friendly and responsive interface
• Option to download or export filtered data

COMMAND SUMMARY
pip install -r requirements.txt
streamlit run app.py
AUTHOR

Project by: Sanskruti S. Desai
Title: Flight Price Analysis and Visualization using Streamlit

pip install -r requirements.txt
streamlit run app.py
