StudyFluence Tutoring App
Welcome to StudyFluence, an AI-powered tutoring and real-time study room platform designed to enhance learning through collaboration. Built with Streamlit, this app offers features like discussions, session booking, topic exploration, and tutor matching, all accessible after a simple login.
Overview

Purpose: Facilitate global learning with AI assistance, live study rooms, and peer collaboration.
Features:
Secure login system (demo credentials: username "student", password "pass123").
Active discussion threads with comment functionality.
Schedule and book study sessions with downloadable records.
Explore trending topics and request tutor assistance.
Contact support for inquiries.


Last Updated: 12:51 PM EAT, August 9, 2025.

Installation
To run the app locally, follow these steps:

Clone the Repository:
git clone <your-repository-url>
cd studyfluence-app


Install Dependencies:Ensure you have Python 3.8+ installed. Then, install the required packages:
pip install -r requirements.txt


Run the App:Launch the Streamlit app locally:
streamlit run app.py


Use the demo login credentials ("student"/"pass123") to access features.
Test discussions, session booking, topic selection, and tutor requests.



Usage

Login: Enter username and password on the login page. Logout by refreshing the page.
Discussions: View active threads, add comments, and see the latest responses.
Sessions: Book existing sessions or schedule new ones with date and time. Download session data as a CSV.
Topics: Select a trending topic to explore (expandable with content).
Tutors: Request a tutor by subject for personalized support.
Contact: Reach out via the provided email or phone number.

Deployment on Streamlit Community Cloud
To deploy the app on Streamlit Community Cloud:

Prepare Files:

Ensure app.py and requirements.txt are in the root directory (e.g., studyfluence-app).


Set Up GitHub Repository:

Initialize a Git repository if not already done:git init
git add app.py requirements.txt
git commit -m "Initial deployable StudyFluence app"


Create a new repository on GitHub and push:git remote add origin <your-repository-url>
git push -u origin main




Deploy:

Visit Streamlit Community Cloud.
Sign in with your GitHub account.
Click "New app" and connect to your repository.
Set the branch to main and the main file path to /app.py.
Click "Deploy" and monitor the build log for any issues.


Access:

Once deployed, use the provided URL to access the app. Note that session state resets on redeployment; persistent data requires a backend integration (e.g., SQLite).



Requirements

Dependencies: streamlit>=1.22.0 and pandas>=1.5.0 (both supported on Streamlit Community Cloud).
Python: 3.8 or higher.

Notes

Session State: Data (e.g., discussions, sessions) persists during a session but resets on redeployment. For production, integrate a database.
Resource Usage: The app is lightweight, with no heavy computations or external API calls beyond CSV export.
Error Handling: Includes validation to prevent crashes (e.g., empty inputs).
Customization: Enhance with a backend for persistent data or additional features like AI Q&A (currently simulated).

Contributing
Feel free to fork this repository, submit issues, or pull requests to improve StudyFluence. Contact support@studyfluence.com for collaboration.
License
© 2023-2025 StudyFluence. Learn together, anywhere.
