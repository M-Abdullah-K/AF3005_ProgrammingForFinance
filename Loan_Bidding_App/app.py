import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from auth import login, signup, ensure_admin_exists
from bidding import request_loan, place_bid, view_loan_requests
from admin import match_loans, view_admin_dashboard
from db import loans_collection, bids_collection
import time

if "admin_checked" not in st.session_state:
    ensure_admin_exists()
    st.session_state["admin_checked"] = True

st.markdown(
    """
    <style>
    .big-font { font-size:22px !important; font-weight: bold; }
    .small-text { font-size:16px; color: gray; }
    @keyframes fadeIn { from { opacity: 0; } to { opacity: 1; } }
    .fade-in { animation: fadeIn 1.5s; }
    @keyframes slideIn {
        from { transform: translateY(-20px); opacity: 0; }
        to { transform: translateY(0); opacity: 1; }
    }
    .slide-in { animation: slideIn 1s ease-out; }
    .stButton>button { transition: 0.3s; border-radius: 8px; }
    .stButton>button:hover { transform: scale(1.05); background-color: #ff7f50; color: white; }
    .stSidebar { background-color: #f8f9fa; padding: 10px; border-radius: 8px; }
    .card {
        padding: 15px;
        border-radius: 10px;
        background: #ffffff;
        box-shadow: 3px 3px 15px rgba(0, 0, 0, 0.1);
        margin: 10px 0;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("💳 Debt Auction Marketplace")

with st.spinner("🚀 Loading application..."):
    time.sleep(1.5)

if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False
    st.session_state["username"] = ""
    st.session_state["is_admin"] = False

if not st.session_state["logged_in"]:
    tab_login, tab_signup = st.tabs(["🔑 Login", "📝 Signup"])

    with tab_login:
        st.subheader("🔒 Login to Your Account")
        user_type = st.radio("👥 Login as", ["User", "Admin"], horizontal=True)
        login_username = st.text_input("👤 Username")
        login_password = st.text_input("🔑 Password", type="password")

        if st.button("✅ Login"):
            if login(login_username, login_password, "admin" if user_type == "Admin" else "user"):
                st.session_state["logged_in"] = True
                st.session_state["username"] = login_username
                st.session_state["is_admin"] = user_type == "Admin"
                st.success(f"✅ Welcome, {login_username}!")
                st.rerun()
            else:
                st.error("❌ Invalid username or password.")

    with tab_signup:
        st.subheader("📝 Create a New Account")
        signup_username = st.text_input("👤 Choose a Username")
        signup_password = st.text_input("🔑 Choose a Password", type="password")

        if st.button("🆕 Signup"):
            if signup_username and signup_password:
                if signup(signup_username, signup_password):
                    st.success("✅ Account created! Please log in.")
                    st.rerun()
                else:
                    st.error("⚠️ Username already exists.")
            else:
                st.warning("⚠️ Please enter a username and password.")

else:
    st.sidebar.markdown(f"👋 **Welcome, {st.session_state['username']}**")
    menu_options = ["📌 Request Loan", "💰 Place a Bid", "📑 View Loans", "📊 Financial Insights", "🚪 Logout"]

    if st.session_state["is_admin"]:
        menu_options.insert(4, "⚙️ Admin Dashboard")

    choice = st.sidebar.radio("📌 Navigation", menu_options)
    st.sidebar.markdown("<hr>", unsafe_allow_html=True)

    if choice == "📌 Request Loan":
        request_loan(st.session_state["username"])

    elif choice == "💰 Place a Bid":
        place_bid(st.session_state["username"])

    elif choice == "📑 View Loans":
        view_loan_requests(st.session_state["username"])

    elif choice == "⚙️ Admin Dashboard" and st.session_state["is_admin"]:
        view_admin_dashboard()

    elif choice == "📊 Financial Insights":
        st.subheader("📊 Financial Data Visualization")
        st.markdown("Analyze loan and bid trends with interactive graphs!")

        loans_data = list(loans_collection.find({}))
        bids_data = list(bids_collection.find({}))

        if loans_data:
            df_loans = pd.DataFrame(loans_data)
            df_loans["date"] = pd.to_datetime(df_loans["_id"].apply(lambda x: x.generation_time))
            df_loans = df_loans.sort_values("date")

            st.markdown("### 📈 Loan Requests Over Time")
            fig, ax = plt.subplots(figsize=(8, 4))
            sns.lineplot(data=df_loans, x="date", y="amount", marker="o", ax=ax)
            plt.xticks(rotation=45)
            plt.ylabel("Loan Amount ($)")
            plt.xlabel("Date")
            plt.grid(True)
            st.pyplot(fig)

        if loans_data:
            df_loans_status = pd.DataFrame(loans_data)
            st.markdown("### 📊 Loan Status Distribution")
            fig, ax = plt.subplots(figsize=(6, 4))
            sns.countplot(data=df_loans_status, x="status", palette="coolwarm", ax=ax)
            plt.xlabel("Status")
            plt.ylabel("Count")
            st.pyplot(fig)

        if bids_data:
            df_bids = pd.DataFrame(bids_data)
            df_bids_grouped = df_bids.groupby("lender")["interest_rate"].count().reset_index()
            df_bids_grouped = df_bids_grouped.rename(columns={"interest_rate": "Number of Bids"})
            df_bids_grouped = df_bids_grouped.sort_values("Number of Bids", ascending=False)

            st.markdown("### 🏆 Top Lenders Leaderboard")
            st.table(df_bids_grouped)

        if bids_data:
            df_bids["interest_rate"] = df_bids["interest_rate"].astype(float)
            st.markdown("### 🔍 Interest Rate Trends")
            fig, ax = plt.subplots(figsize=(8, 4))
            sns.histplot(df_bids["interest_rate"], kde=True, bins=10, color="purple", ax=ax)
            plt.xlabel("Interest Rate (%)")
            plt.ylabel("Frequency")
            st.pyplot(fig)

    elif choice == "🚪 Logout":
        st.session_state["logged_in"] = False
        st.session_state["username"] = ""
        st.session_state["is_admin"] = False
        st.rerun()
