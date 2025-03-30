import streamlit as st
from db import loans_collection, bids_collection
from bson import ObjectId

def view_admin_dashboard():
    st.subheader("📊 Admin Dashboard")

    loans = list(loans_collection.find({}))
    if not loans:
        st.warning("🚫 No loan requests found.")
        return

    for loan in loans:
        loan_id_str = str(loan["_id"])
        st.markdown(f"### 🆔 Loan ID: `{loan_id_str}`")
        st.write(f"💵 **Amount:** ${loan['amount']}")
        st.write(f"⏳ **Duration:** {loan['duration']} months")
        st.write(f"📌 **Status:** {loan['status']}")
        st.write("---")

    if st.button("🔄 Match Loans"):
        match_loans()
        st.success("✅ Loan matching completed!")

def match_loans():
    loans = list(loans_collection.find({"status": "pending"}))
    for loan in loans:
        loan_id_str = str(loan["_id"])
        bids = list(bids_collection.find({"loan_id": loan_id_str}))
        if bids:
            bids.sort(key=lambda x: x["interest_rate"])
            best_bid = bids[0]
            accept_loan_bid(ObjectId(loan_id_str), best_bid)

def accept_loan_bid(loan_id, bid):
    loans_collection.update_one({"_id": loan_id}, {"$set": {"status": "funded"}})
    st.success(f"🎉 Loan `{loan_id}` funded at {bid['interest_rate']}% interest by {bid['lender']}")
