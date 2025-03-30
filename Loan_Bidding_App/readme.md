💳 Debt Auction Marketplace
📚 Course Information
Course Name: AF3005 – Programming for Finance

Instructor: Dr. Usama Arshad

🚀 App Overview
The Debt Auction Marketplace is a loan bidding platform where users can request loans, and lenders can bid with competitive interest rates. How is works is that some user places their loan requests, others can view and bid on this request as well as place their own loan requests. The borrowers can then accept the lowest interest rate. The admin also has privledges to accept the best bids for all the users, "Matching" the borrowers and the lenders. This helps us find the best loans through the market forces of demand and supply.

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
👉 https://af3005programmingforfinance-uu6emrjhzgp73hlkynpnal.streamlit.app/

🔐 Admin Credentials
An admin account is automatically created when the app starts.

Username: admin123

Password: securepassword

Use these credentials to access the Admin Dashboard.

📷 Screenshots
🔑 Login Page

📌 Loan Request Page
![Screenshot (316)](https://github.com/user-attachments/assets/80152123-37ac-4d7e-913e-9e10186745ad)

💰 Bidding Page
![Screenshot (314)](https://github.com/user-attachments/assets/d193e9f3-232c-4919-9388-ef585e139f02)

View Loan (Accept Loan on own bids, and view other loans)
![Screenshot (317)](https://github.com/user-attachments/assets/d179bb84-a4fc-440f-ace7-95b973c7e262)

📊 Financial Insights
![Screenshot (318)](https://github.com/user-attachments/assets/371e404c-0f10-4b8c-acf5-77c13f196781)

(📹 Watch a Demo Video)


🔗 GitHub Repository
👉 https://github.com/M-Abdullah-K/AF3005_ProgrammingForFinance/tree/main/Loan_Bidding_App

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
