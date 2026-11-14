# COVID-19 Data Analysis and Visualization

Exploratory analysis and visualization of COVID-19 cases, recoveries and deaths over time and across countries, including interactive charts.

## Tools & Libraries

- Pandas
- Matplotlib
- Seaborn
- Plotly


# Tools

- Vs code
- Git
- Git Hub
- Python
- Libraries of Python




## Dataset

- **Source:** COVID-19 CSV dataset (e.g., from Kaggle or Our World in Data).
- **Typical columns:** Date, Country, Confirmed cases, Recoveries, Deaths.
- **Government interventions:** Requires intervention data (e.g., a stringency index column or a separate dataset merged by country and date).

## Project Workflow

### 1. Load Dataset
- Read the COVID-19 CSV file using Pandas.

### 2. Explore Dataset
- Display first 5 rows
- Check dataset shape
- Display column names
- Check data types

### 3. Data Cleaning
- Handle missing values
- Convert date column to datetime
- Remove duplicate records

### 4. Data Analysis
- Analyze cases, recoveries and deaths over time
- Compare different countries
- Identify countries with the highest cases and deaths

### 5. Data Visualization
- Line chart: Cases over time
- Line chart: Recoveries over time
- Line chart: Deaths over time
- Bar chart: Country-wise cases
- Comparison: Government interventions vs virus spread

### 6. Interactive Visualization
- Create interactive charts using Plotly

## Installation

```bash
pip install pandas matplotlib seaborn plotly
```

## Usage

```bash
git clone <your-repo-url>
cd covid19-analysis
jupyter notebook covid19_analysis.ipynb
```

## Project Structure

```
├── main.ipynb
├── covid-data.csv
├── output.png
└── README.md
```


## Author
``` Adnan ```