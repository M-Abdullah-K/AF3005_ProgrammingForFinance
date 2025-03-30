💳 Debt Auction Marketplace
📚 Course Information
Course Name: AF3005 – Programming for Finance
Instructor: Dr. Usama Arshad

🚀 App Overview
The Debt Auction Marketplace is a loan bidding platform where users can request loans, and lenders can bid with competitive interest rates. Borrowers place loan requests, lenders can view and bid on these requests, and the borrower can accept the lowest interest rate. Additionally, an admin has privileges to match the best bids for all users, optimizing loans through the market forces of demand and supply.

🔑 Key Features
✅ User & Admin Authentication (secure login/signup)
✅ Loan Requests: Borrowers request loans with specific amounts & durations
✅ Bidding System: Lenders bid with custom interest rates
✅ Admin Dashboard: Admins can view all loans & match them with the best bids
✅ Financial Data Visualization:

📈 Loan request trends over time

📊 Loan status distribution

🏆 Top lenders leaderboard

🔍 Interest rate trends

💻 Installation Guide (How to Run Locally?)
1️⃣ Clone the Repository
git clone https://github.com/M-Abdullah-K/AF3005_ProgrammingForFinance.git
cd Loan_Bidding_App
2️⃣ Install Dependencies
Create a virtual environment and install the required Python packages:

# Create a virtual environment

python -m venv venv

# Activate the virtual environment

# On macOS/Linux

source venv/bin/activate

# On Windows

venv\Scripts\activate

# Install dependencies

pip install -r requirements.txt
3️⃣ Set Up MongoDB
Option 1: Local Implementation (MongoDB Compass)
Install MongoDB from MongoDB Official Website.

Open MongoDB Compass and connect to:

mongodb://localhost:27017
Create a new database:

Name: debt_auction_db
Create three collections:

users, loans, bids
Add the following .env file in the root directory:

MONGO_URI=mongodb://localhost:27017/debt_auction_db
Option 2: Cloud Deployment (MongoDB Atlas for Streamlit Share)
Create a MongoDB Atlas Account: Sign up here.

Create a new cluster and choose free tier.

Create a new database named:

debt_auction_db
Get your connection string from Atlas and update your .env file:

MONGO_URI="your_mongodb_atlas_uri_here"
Update Streamlit Secrets:

Go to Streamlit Share Dashboard → Secrets

Add:

MONGO_URI="your_mongodb_atlas_uri_here"
Deploy the App on Streamlit!

4️⃣ Run the Application

streamlit run app.py
The app will open in your browser at http://localhost:8501.

🚀 Deployment Link
👉 https://af3005programmingforfinance-uu6emrjhzgp73hlkynpnal.streamlit.app/

🔐 Admin Credentials
An admin account is automatically created when the app starts.

Username: admin123

Password: securepassword

Use these credentials to access the Admin Dashboard.

📷 Screenshots
🔑 Login Page
📌 Loan Request Page
![Screenshot (316)](https://github.com/user-attachments/assets/26fb2607-3e10-42aa-8583-c57345b33e2d)

💰 Bidding Page
![Screenshot (314)](https://github.com/user-attachments/assets/66ded6a6-8866-432a-8591-bf84ec21ebeb)

📑 View Loans
![Screenshot (317)](https://github.com/user-attachments/assets/5b99d26a-c965-41f1-a0ba-8a13756f650a)

📊 Financial Insights
![Screenshot (318)](https://github.com/user-attachments/assets/66a4f031-d3ec-4d49-aff9-9b22723e3858)

⚙️ Admin Panel (Match Loans Feature)
![Screenshot (319)](https://github.com/user-attachments/assets/dff17091-6f49-45b5-9d28-296ba22ff805)

📦 Dependencies
streamlit - UI Framework

pymongo - MongoDB Connection

bcrypt - Password Hashing

sendgrid - Email Support (Future Feature)

python-dotenv - Environment Variables

pandas - Data Analysis

matplotlib - Data Visualization

seaborn - Advanced Data Charts

To install all dependencies, run:

pip install -r requirements.txt
🚀 Future Improvements
✅ Email notifications for loan requests & bid approvals
✅ Live WebSocket updates for real-time bidding
✅ User profile pages with past transactions
✅ Automated credit scoring system

🤝 Contributing
Feel free to fork this repo and contribute!

Create a pull request or open an issue if you have suggestions.
