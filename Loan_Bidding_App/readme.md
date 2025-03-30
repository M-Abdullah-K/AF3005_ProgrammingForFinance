📌 Debt Auction Marketplace
🚀 Overview
Debt Auction Marketplace is a loan bidding system built using Streamlit and MongoDB.
Users can request loans, and lenders can place bids with interest rates.
The system matches borrowers with the best available lenders automatically.

📂 Project Structure:

📁 Debt Auction Marketplace
│── 📄 app.py # Main Streamlit application
│── 📄 db.py # MongoDB connection
│── 📄 auth.py # Authentication (Signup/Login)
│── 📄 bidding.py # Loan & bidding logic
│── 📄 admin.py # Admin dashboard & loan matching
│── 📄 .env # Environment variables
│── 📄 requirements.txt # Dependencies list
│── 📄 README.md # Project documentation (this file)
🔧 Setup Instructions

1️⃣ Clone the Repository
git clone https://github.com/your-repo/debt-auction-marketplace.git
cd debt-auction-marketplace

2️⃣ Install Dependencies
Create a virtual environment and install the required Python packages.

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

🔐 Admin Credentials
An admin account is automatically created when the app starts.

Use these credentials to access the Admin Dashboard:

Username: admin123

Password: securepassword

📊 Features
🔑 Authentication
✅ User & Admin login system with password encryption.
✅ Signup for new users (Admins are created automatically).

💵 Loan Requests & Bidding
✅ Users can request loans with an amount & duration.
✅ Lenders can place bids with competitive interest rates.
✅ Borrowers can view & accept the best bid.

⚙️ Admin Dashboard
✅ View all loan requests.
✅ Match loans to the best available bid.

📊 Financial Data Visualization
✅ Interactive graphs & charts (Matplotlib & Seaborn).
✅ Loan request trends over time.
✅ Loan status distribution.
✅ Top lenders leaderboard.
✅ Interest rate trends analysis.

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
💡 Future Improvements
✅ Email notifications for loan requests & bid approvals.
✅ Live WebSocket updates for real-time bidding.
✅ User profile pages with past transactions.
✅ Automated credit scoring system.

🤝 Contributing
Feel free to fork this repo and contribute!
Create a pull request or open an issue if you have suggestions.
