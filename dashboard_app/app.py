import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="HealthKart Influencer Dashboard", layout="wide")

@st.cache_data
def load_data():
    influencers = pd.read_csv("data/influencers.csv")
    posts = pd.read_csv("data/posts.csv")
    tracking = pd.read_csv("data/tracking_data.csv")
    payouts = pd.read_csv("data/payouts.csv")
    return influencers, posts, tracking, payouts

influencers, posts, tracking, payouts = load_data()

merged = tracking.merge(payouts, on='influencer_id', how='left')
summary = merged.groupby('influencer_id').agg({
    'revenue': 'sum',
    'total_payout': 'first'
}).reset_index()
summary['ROAS'] = summary['revenue'] / summary['total_payout']
summary = summary.merge(influencers[['influencer_id', 'name', 'category', 'platform']], on='influencer_id')

st.sidebar.title("📊 Filters")
platforms = st.sidebar.multiselect("Platform", influencers['platform'].unique(), default=influencers['platform'].unique())
categories = st.sidebar.multiselect("Category", influencers['category'].unique(), default=influencers['category'].unique())

filtered_summary = summary[
    (summary['platform'].isin(platforms)) &
    (summary['category'].isin(categories))
]

tab1, tab2, tab3 = st.tabs(["📈 Campaign Overview", "🧑‍🤝‍ Influencer Insights", "💰 Payout Tracking"])

with tab1:
    st.header("📈 Campaign Overview")
    st.metric("Total Revenue", f"₹{int(filtered_summary['revenue'].sum()):,}")
    st.metric("Total Payout", f"₹{int(filtered_summary['total_payout'].sum()):,}")
    total_roas = filtered_summary['revenue'].sum() / filtered_summary['total_payout'].sum()
    st.metric("Overall ROAS", f"{total_roas:.2f}")

    st.subheader("Top Influencers by ROAS")
    top5 = filtered_summary.sort_values(by="ROAS", ascending=False).head(5)
    st.dataframe(top5)

    st.subheader("ROAS by Platform")
    fig, ax = plt.subplots()
    sns.barplot(data=filtered_summary, x="platform", y="ROAS", ax=ax)
    st.pyplot(fig)

with tab2:
    st.header("🧑‍🤝‍ Influencer Insights")
    st.dataframe(filtered_summary.sort_values(by="ROAS", ascending=False))

    st.subheader("ROAS Distribution")
    fig2, ax2 = plt.subplots()
    sns.histplot(filtered_summary['ROAS'], bins=10, kde=True, ax=ax2)
    st.pyplot(fig2)

    st.download_button("📥 Download Summary CSV", filtered_summary.to_csv(index=False), "influencer_summary.csv")

with tab3:
    st.header("💰 Payout Tracking")
    st.dataframe(payouts)

    st.subheader("Total Payouts by Influencer")
    payout_chart = payouts.merge(influencers[['influencer_id', 'name']], on='influencer_id')
    fig3, ax3 = plt.subplots(figsize=(10, 4))
    sns.barplot(data=payout_chart.sort_values(by="total_payout", ascending=False), x="name", y="total_payout", ax=ax3)
    plt.xticks(rotation=45)
    st.pyplot(fig3)
