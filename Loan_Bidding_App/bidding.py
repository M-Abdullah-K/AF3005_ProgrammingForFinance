import streamlit as st
from db import loans_collection, bids_collection
from bson import ObjectId

def request_loan(username):
    st.subheader("📝 Request a Loan")
    
    amount = st.number_input("💰 Loan Amount ($)", min_value=100, step=100)
    duration = st.number_input("⏳ Duration (months)", min_value=1, step=1)

    if st.button("✅ Submit Loan Request"):
        loan_data = {"borrower": username, "amount": amount, "duration": duration, "status": "pending"}
        loans_collection.insert_one(loan_data)
        st.success("🎉 Loan request submitted!")

def place_bid(username):
    st.subheader("💰 Place a Bid")

    loans = list(loans_collection.find({"status": "pending"}))
    available_loans = [loan for loan in loans if loan["borrower"] != username]

    if not available_loans:
        st.warning("🚫 No available loan requests to bid on (or all are your own).")
        return

    loan_details = {f"💵 ${loan['amount']} | ⏳ {loan['duration']} months | Borrower: {loan['borrower']}": str(loan["_id"]) for loan in available_loans}

    selected_loan = st.selectbox("📌 Select Loan", list(loan_details.keys()))
    interest_rate = st.number_input("💸 Interest Rate (%)", min_value=1.0, step=0.1)

    if st.button("💵 Place Bid"):
        loan_id = loan_details[selected_loan]
        bid_data = {"loan_id": loan_id, "lender": username, "interest_rate": interest_rate}
        bids_collection.insert_one(bid_data)
        st.success(f"✅ Your bid was placed for {selected_loan}")

def view_loan_requests(username):
    st.subheader("📜 Your Loan Requests")

    loans = list(loans_collection.find({"borrower": username, "status": "pending"}))
    if not loans:
        st.warning("🚫 No loan requests found.")
        return

    for loan in loans:
        loan_id_str = str(loan["_id"])
        st.markdown(f"### 🆔 Loan ID: `{loan_id_str}`")
        st.write(f"💵 **Amount:** ${loan['amount']}")
        st.write(f"📆 **Duration:** {loan['duration']} months")
        st.write("---")

        bids = list(bids_collection.find({"loan_id": loan_id_str}))
        if not bids:
            st.write("🚫 No bids yet.")
        else:
            bids.sort(key=lambda x: x["interest_rate"])
            best_bid = bids[0]
            st.write(f"🏆 **Best Bid:** {best_bid['interest_rate']}% by {best_bid['lender']}")

            if st.button(f"✅ Accept Best Bid", key=loan_id_str):
                accept_loan_bid(ObjectId(loan_id_str), best_bid)

def accept_loan_bid(loan_id, bid):
    loans_collection.update_one({"_id": loan_id}, {"$set": {"status": "funded"}})
    st.success(f"🎉 Loan {loan_id} funded at {bid['interest_rate']}% by {bid['lender']}")

__all__ = ["request_loan", "place_bid", "view_loan_requests"]
