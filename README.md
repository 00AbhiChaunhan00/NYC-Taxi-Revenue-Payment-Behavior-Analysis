<div align="center">

# 🚕 NYC Taxi Revenue & Payment Behavior Analysis

### Python EDA • MySQL Business Analysis • Statistical Hypothesis Testing

**Python • Pandas • NumPy • Matplotlib • Seaborn • SciPy • SQL • MySQL**

<br>

[![Python](https://img.shields.io/badge/Python-Data%20Analysis-3776AB?style=for-the-badge&logo=python&logoColor=white)](#)
[![MySQL](https://img.shields.io/badge/MySQL-Business%20Analysis-4479A1?style=for-the-badge&logo=mysql&logoColor=white)](#)
[![SQL](https://img.shields.io/badge/SQL-Ad--hoc%20Analysis-336791?style=for-the-badge)](#)
[![Statistics](https://img.shields.io/badge/Statistics-Hypothesis%20Testing-F04B23?style=for-the-badge)](#)

</div>

---

# 📌 Project Overview

This project analyzes **2.79M cleaned NYC Yellow Taxi trips from January 2025** to understand how trip characteristics and payment behavior relate to taxi fare revenue.

The project combines:

- Python data analysis and EDA
- Payment behavior analysis
- Fare and trip-distance analysis
- Passenger-count analysis
- MySQL ad-hoc business analysis
- Statistical hypothesis testing
- Business interpretation of statistical results

The analytical journey is:

```text
NYC YELLOW TAXI TRIP DATA
          ↓
     DATA CLEANING
          ↓
   PYTHON EDA & VISUALS
          ↓
     MYSQL ANALYSIS
          ↓
  HYPOTHESIS TESTING
          ↓
    BUSINESS INSIGHTS
```

The goal is not only to identify patterns in taxi revenue, but also to test whether the observed difference in fares between **Credit Card and Cash trips** is statistically meaningful.

---

# 🎯 Business Problem

Taxi revenue can vary based on factors such as:

- Payment method
- Trip distance
- Trip duration
- Pickup hour
- Passenger count

The analysis was designed to answer practical questions such as:

### Payment Behavior

- Which payment method is used most frequently?
- Do Credit Card and Cash trips have different average fares?
- Does payment method show a meaningful revenue advantage?

### Trip Characteristics

- How does fare revenue change across trip-distance groups?
- How does trip duration relate to average fare and revenue?
- Which pickup hours generate the highest revenue?

### Passenger Behavior

- Which passenger-count groups dominate taxi demand?
- How do fare and revenue vary by passenger count?

### Statistical Question

> **Is there a statistically significant difference in average fare between Credit Card and Cash trips?**

---

# 📊 Dataset

The project uses the **NYC TLC Yellow Taxi Trip Records — January 2025**.

After validation and cleaning, the analytical dataset contains:

> **2,791,538 trips × 8 fields**

### Fields Used

| Field | Purpose |
|---|---|
| `tpep_pickup_datetime` | Trip pickup timestamp |
| `tpep_dropoff_datetime` | Trip drop-off timestamp |
| `passenger_count` | Number of passengers |
| `trip_distance` | Trip distance in miles |
| `payment_type` | Credit Card / Cash |
| `fare_amount` | Base trip fare |
| `total_amount` | Total charged amount |
| `duration_minutes` | Derived trip duration |

### Analysis Scope

The payment analysis focuses on:

```text
Credit Card
vs
Cash
```

Other payment categories were excluded from the payment-method comparison so the statistical test directly compares the two target groups.

---

# 🧹 Data Preparation

The raw trip data was validated before analysis.

Key checks included:

- Missing values
- Duplicate records
- Invalid payment categories
- Zero / negative fare amounts
- Zero trip distances
- Invalid pickup/drop-off timestamps
- Passenger-count anomalies
- Fare outlier detection

### Cleaning Rules

```text
Keep Credit Card / Cash trips
        ↓
Fare Amount > 0
        ↓
Trip Distance > 0
        ↓
Drop-off Time > Pickup Time
        ↓
Create Duration Minutes
        ↓
Prepare Clean Analytical Dataset
```

Fare outliers were detected using the **IQR method**, but they were not blindly removed because high fares may represent legitimate long-distance or airport trips.

Passenger-count errors were handled separately for passenger analysis by restricting the analysis to valid counts from **1 to 6**.

---

# 🐍 Python Exploratory Data Analysis

Python was used to explore payment behavior, fare distributions, trip distance, and passenger patterns.

## 1️⃣ Fare & Distance Distribution

Both fare amount and trip distance were **right-skewed**, with most observations concentrated in lower-fare and shorter-distance ranges.

Credit Card trips appeared much more frequently than Cash trips across most ranges.

Average values were:

| Payment Type | Avg Fare | Avg Trip Distance |
|---|---:|---:|
| Credit Card | **$17.86** | **3.22 miles** |
| Cash | **$18.04** | **3.18 miles** |

The averages are very similar, which motivated formal hypothesis testing.

---

# 💳 Payment Preference

Approximately:

```text
Credit Card → 86.8%
Cash        → 13.2%
```

of the analyzed trips were paid using the two selected payment methods.

### Insight

> **Credit Card is the dominant payment method by trip volume, but dominance in transaction count does not automatically mean a higher average fare.**

---

# 👥 Passenger Count Analysis

Single-passenger trips dominate the valid passenger-count data.

Approximately:

```text
Credit Card + 1 Passenger → ~70% of valid passenger trips
Cash + 1 Passenger        → ~10%
```

Two-passenger trips form the next largest group, while trips with three or more passengers represent a much smaller share.

### Insight

Credit Card remains the dominant payment method across the major passenger-count groups, while demand is heavily concentrated among single-passenger trips.

---

# 🗄️ MySQL Business Analysis

MySQL was used for focused ad-hoc analysis of trip and revenue behavior.

## 1️⃣ Payment Method Performance

| Payment Method | Total Trips | Avg Fare | Total Fare Revenue |
|---|---:|---:|---:|
| Card | **2,423,623** | $17.86 | **$43.28M** |
| Cash | 367,915 | **$18.04** | $6.64M |

### Insight

Cash has a slightly higher average fare, but Credit Card generates far more total fare revenue because it accounts for substantially more trips.

---

## 2️⃣ Trip Distance Analysis

| Distance Group | Total Trips | Avg Distance | Avg Fare | Fare Revenue |
|---|---:|---:|---:|---:|
| Short (<2 miles) | **1,661,929** | 1.12 | $9.75 | $16.20M |
| Medium (2–5 miles) | 707,925 | 2.94 | $18.33 | $12.98M |
| Long (5+ miles) | 421,684 | 11.96 | **$49.18** | **$20.74M** |

### Insight

Short trips dominate trip volume, but long-distance trips generate the **highest average fare and the largest fare-revenue contribution** among the three distance groups.

---

## 3️⃣ Trip Duration Analysis

| Duration Group | Total Trips | Avg Fare | Fare Revenue |
|---|---:|---:|---:|
| Short (<10 min) | 1,191,375 | $8.44 | $10.05M |
| Medium (10–29 min) | **1,360,913** | $19.23 | **$26.17M** |
| Long (30+ min) | 239,250 | **$57.25** | $13.70M |

### Insight

Medium-duration trips generate the highest total fare revenue because of their large trip volume, while long-duration trips produce the highest average fare.

---

## 4️⃣ Peak Revenue Hours

The highest fare-revenue hours were concentrated in the afternoon and early evening.

Top hours included:

| Pickup Hour | Total Trips | Avg Fare | Fare Revenue |
|---:|---:|---:|---:|
| 17:00 | **204,963** | $17.31 | **$3.55M** |
| 16:00 | 188,772 | $18.75 | **$3.54M** |
| 15:00 | 187,090 | $18.69 | **$3.50M** |
| 18:00 | 204,062 | $16.31 | $3.33M |
| 14:00 | 177,758 | $18.62 | $3.31M |

### Insight

> **The 3 PM–5 PM period is particularly important for fare revenue**, with 5 PM producing the highest total fare revenue in this analysis.

---

## 5️⃣ Passenger Count Analysis

| Passengers | Total Trips | Avg Fare | Fare Revenue |
|---:|---:|---:|---:|
| 1 | **2,212,983** | $17.36 | **$38.42M** |
| 2 | 386,682 | $20.08 | $7.76M |
| 3 | 86,145 | $19.76 | $1.70M |
| 4 | 53,115 | **$22.06** | $1.17M |
| 5 | 17,566 | $16.86 | $0.30M |

### Insight

Single-passenger trips are the largest revenue contributor because of their overwhelming trip volume, while four-passenger trips have the highest average fare among the displayed groups.

---

# 🧪 Hypothesis Testing

## Business Question

> **Is there a statistically significant difference in average fare amount between Credit Card and Cash trips?**

### Null Hypothesis — H₀

There is no significant difference in average fare between Credit Card and Cash trips.

### Alternative Hypothesis — H₁

There is a significant difference in average fare between Credit Card and Cash trips.

### Significance Level

```text
α = 0.05
```

### Test Used

**Welch's Independent Two-Sample t-test**

### Why Welch's t-test?

- Two independent groups are being compared.
- Fare amount is numerical.
- Credit Card and Cash have substantially different sample sizes.
- Welch's test does not require equal population variances.

---

# 📐 Hypothesis Test Result

```text
T-Statistic = -5.60
P-Value     = 2.145 × 10⁻⁸
Alpha       = 0.05
```

Because:

```text
P-Value < 0.05
```

the null hypothesis was **rejected**.

Average fares:

```text
Credit Card → $17.86
Cash        → $18.04
Difference  → ~$0.19 per trip
```

### Statistical Interpretation

There is a **statistically significant difference** in average fare between Credit Card and Cash trips.

### Business Interpretation

The difference is only around **$0.19 per trip**.

> **Statistical significance does not automatically imply business significance.**

The very large sample size makes it possible for a small difference to be statistically significant. Therefore, the analysis does **not** show a meaningful fare advantage for Credit Card payments based on average fare alone.

The result demonstrates association, not causation.

---

# 🧠 Core Business Findings

### 1️⃣ Credit Card dominates trip volume

Credit Card represents approximately **86.8%** of analyzed Card/Cash trips.

### 2️⃣ Cash has a slightly higher average fare

```text
Cash        → $18.04
Credit Card → $17.86
```

The difference is only about **$0.19**.

### 3️⃣ Credit Card generates substantially more total fare revenue

```text
Credit Card → ~$43.28M
Cash        → ~$6.64M
```

This is primarily associated with much higher Credit Card trip volume.

### 4️⃣ Long-distance trips are high-value trips

Trips above 5 miles generated an average fare of approximately **$49.18** and about **$20.74M** in fare revenue.

### 5️⃣ Medium-duration trips generate the most total fare revenue

Trips lasting 10–29 minutes generated approximately **$26.17M**.

### 6️⃣ Afternoon / early-evening hours are revenue-intensive

The highest hourly fare revenue occurred at **5 PM (~$3.55M)**, followed closely by 4 PM and 3 PM.

### 7️⃣ Single-passenger trips drive volume and revenue

More than **2.21M** one-passenger trips generated approximately **$38.42M** in fare revenue.

---

# 🎯 Business Recommendations

### Priority 1 — Focus on High-Demand Payment Behavior

Credit Card trips account for the majority of transaction volume and total fare revenue, so digital-payment reliability and convenience are operationally important.

### Priority 2 — Prioritize High-Value Trip Opportunities

Long-distance trips produce much higher average fares and a substantial share of fare revenue despite lower trip volume.

### Priority 3 — Align Availability with Revenue-Intensive Hours

Afternoon and early-evening periods, particularly around **3 PM–5 PM**, show strong total fare revenue and may deserve greater operational attention.

### Priority 4 — Do Not Overstate the Payment-Method Effect

Although the t-test detected a statistically significant fare difference, the observed difference is only about **$0.19**. Payment method alone should therefore not be treated as a meaningful driver of higher average fare.

---

# 🧰 Technology Stack

| Area | Technology |
|---|---|
| Programming | Python |
| Data Manipulation | Pandas, NumPy |
| Visualization | Matplotlib, Seaborn |
| Statistical Analysis | SciPy |
| Database | MySQL |
| Business Analysis | SQL |
| Data Format | Parquet, CSV |
| Development | Jupyter Notebook |
| Version Control | GitHub |

---

# 📂 Repository Structure

```text
nyc-taxi-revenue-payment-analysis/
│
├── README.md
│
├── 01_Data_Cleaning/
│   └── taxi_data_cleaning.py
│
├── 02_Python_Analysis/
│   └── EDA_Hypothesis.ipynb
│
├── 03_SQL_Analysis/
│   └── taxi_business_analysis.sql
│
├── 04_SQL_Outputs/
│   ├── Payment_Method_Performance.csv
│   ├── Trip_Distance_Analysis.csv
│   ├── Trip_Duration_Analysis.csv
│   ├── Peak_Revenue_Hours.csv
│   └── Passenger_Count_Analysis.csv
│
└── 05_Documentation/
    └── Key_Insights.md
```

> The raw NYC TLC dataset is not required to be stored in the repository. It can be downloaded separately from the official NYC TLC Trip Record Data source.

---

# 🧑‍💼 Interview Quick Recall

If I had **60–90 seconds** to explain this project:

> I analyzed approximately 2.79 million cleaned NYC Yellow Taxi trips using Python, MySQL and statistical hypothesis testing. In Python, I performed EDA to study fare, distance, payment and passenger behavior, and found that Credit Card accounted for about 86.8% of the analyzed Card/Cash trips. I then used MySQL for ad-hoc business analysis across payment method, distance, duration, pickup hour and passenger count. Credit Card generated about $43.28M in fare revenue compared with $6.64M for Cash because of its much larger trip volume. To test whether payment method was associated with different average fares, I performed Welch's independent t-test. The result was statistically significant, but Cash averaged $18.04 versus $17.86 for Credit Card — only about a $0.19 difference. The key conclusion was that statistical significance does not necessarily mean business significance, and trip volume, distance, duration and timing provide more useful context for understanding revenue.

---

# 🧠 Interview Memory Map

Remember the project in five words:

```text
VOLUME
   ↓
TRIP BEHAVIOR
   ↓
REVENUE
   ↓
STATISTICAL TEST
   ↓
BUSINESS MEANING
```

---

# 🔑 Five Numbers to Remember

```text
2.79M
Cleaned Trips

86.8%
Credit Card Share

$43.28M
Credit Card Fare Revenue

$0.19
Average Fare Difference

2.145 × 10⁻⁸
T-Test P-Value
```

---

# 🛡️ Portfolio Accuracy / Limitations

This project should be interpreted as a portfolio analytics study.

Important limitations:

- The analysis uses NYC Yellow Taxi trip records for **January 2025**.
- The payment comparison focuses on **Credit Card and Cash** trips.
- Statistical significance does not establish causation.
- The t-test identifies a difference in average fares but does not prove that payment method causes the fare difference.
- High fare values were not automatically removed because some may represent legitimate long-distance or airport trips.
- Recommendations are analytical observations and were not deployed or measured as real-world business outcomes.

---

# 🚀 Skills Demonstrated

- Python
- SQL
- MySQL
- Pandas
- NumPy
- Exploratory Data Analysis
- Data Cleaning
- Data Validation
- Data Visualization
- Statistical Analysis
- Hypothesis Testing
- Welch's t-test
- Revenue Analysis
- Payment Behavior Analysis
- Ad-hoc Business Analysis
- Business Interpretation
- Analytical Storytelling

---

<div align="center">

## ⭐ NYC Taxi Revenue & Payment Behavior Analysis

**Explore → Analyze → Test → Interpret**

</div>
