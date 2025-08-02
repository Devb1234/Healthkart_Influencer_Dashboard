
# 💼 HealthKart Influencer ROI Dashboard

This project is an open-source analytics dashboard built for HealthKart to track and visualize the ROI of influencer marketing campaigns. It helps in evaluating campaign performance, calculating incremental ROAS, analyzing influencer effectiveness, and tracking payouts.

---

## 🚀 Features

- 📊 **Campaign Performance** overview
- 💰 **Incremental ROAS (Return on Ad Spend)** calculations
- 🌟 **Top Influencers** and **Best Personas**
- 🧍 **Influencer Profile Insights**
- 🧾 **Payout Tracking**
- 🔍 Filters by platform, brand, product, influencer category
- 📤 Export data to CSV
- 📈 Charts and metrics powered by `matplotlib` and `seaborn`
- 📎 Easy deployment on Streamlit Cloud

---

## 📁 Dataset Simulation

The app uses simulated influencer campaign data across 4 CSV files:

| File | Description |
|------|-------------|
| `influencers.csv` | Influencer profiles |
| `posts.csv` | Posts made by influencers |
| `tracking_data.csv` | Order and revenue attribution per influencer |
| `payouts.csv` | Payout info per influencer (per post or per order) |

---

## 🏗️ Folder Structure

```
healthkart-influencer-dashboard/
├── data/
│   ├── influencers.csv
│   ├── posts.csv
│   ├── tracking_data.csv
│   └── payouts.csv
├── dashboard_app/
│   └── app.py
├── requirements.txt
└── README.md
```

---

## 📦 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/healthkart-influencer-dashboard.git
cd healthkart-influencer-dashboard
```

### 2. Create a Virtual Environment (Optional)

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Requirements

```bash
pip install -r requirements.txt
```

### 4. Run the App Locally

```bash
cd dashboard_app
streamlit run app.py
```

---

## ☁️ Deploy on Streamlit Cloud

1. Push this project to GitHub
2. Visit: [https://streamlit.io/cloud](https://streamlit.io/cloud)
3. Click **New App**
4. Set:
   - **Repo**: `your-username/healthkart-influencer-dashboard`
   - **Branch**: `main`
   - **App file path**: `dashboard_app/app.py`
5. Click **Deploy**

---

## 📊 Sample Insights You Can Derive

- Which influencer drove the highest revenue?
- Which platform had the best conversion per post?
- What is the ROAS for MuscleBlaze campaigns on Instagram?
- Are payouts aligned with actual performance?

---

## 🛠️ Technologies Used

- [Python](https://www.python.org/)
- [Pandas](https://pandas.pydata.org/)
- [Matplotlib](https://matplotlib.org/)
- [Seaborn](https://seaborn.pydata.org/)
- [Streamlit](https://streamlit.io/)

---

## 📬 Contact

For any queries or contributions, feel free to connect:

- 👤 **Your Name**
- 📧 youremail@example.com
- 🔗 [LinkedIn](https://linkedin.com/in/your-profile)

---

## 📄 License

This project is licensed under the MIT License.
