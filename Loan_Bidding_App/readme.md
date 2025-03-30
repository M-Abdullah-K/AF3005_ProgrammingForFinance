💳 Debt Auction Marketplace
📚 Course Information
Course Name: AF3005 – Programming for Finance

Instructor: Dr. Usama Arshad

🚀 App Overview
The Debt Auction Marketplace is a loan bidding platform where users can request loans, and lenders can bid with competitive interest rates. The system then matches the borrower with the best available lender based on the lowest interest rate.

🔑 Key Features:
✅ User & Admin authentication (secure login/signup)
✅ Loan Requests: Borrowers can request loans with specific amounts & durations
✅ Bidding System: Lenders can place bids with custom interest rates
✅ Admin Dashboard: Admins can view all loans and match them with the best bids
✅ Financial Data Visualization:

📈 Loan request trends over time

📊 Loan status distribution

🏆 Top lenders leaderboard

🔍 Interest rate trends

💻 Installation Guide (How to run locally?)
1️⃣ Clone the Repository
git clone https://github.com/your-repo/debt-auction-marketplace.git
cd debt-auction-marketplace

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
Ensure MongoDB is installed and running on localhost:27017.

Create a .env file in the project root with the following content:

MONGO_URI=mongodb://localhost:27017/debt_auction_db
4️⃣ Run the Application
streamlit run app.py
The app will open in your browser at http://localhost:8501.

🚀 Deployment Link
👉 Live App on Streamlit

🔐 Admin Credentials
An admin account is automatically created when the app starts.

Username: admin123

Password: securepassword

Use these credentials to access the Admin Dashboard.

📷 Screenshots
🔑 Login Page

📌 Loan Request Page

💰 Bidding Page

📊 Financial Insights

(📹 Watch a Demo Video)

🔗 GitHub Repository
👉 GitHub Repo

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
