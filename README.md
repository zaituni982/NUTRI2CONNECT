# 🌱 **NUTRI2CONNECT**is a digital platform designed to bridge the gap between farmers and clients, making the process of buying, selling, and managing nutrition-related products easier and more transparent. It serves as a hub where farmers can showcase their products, manage orders, and communicate directly with clients, while clients can discover high-quality products, place requests, and track their orders seamlessly.

Why NUTRI2CONNECT?

Simplifies Communication: Farmers and clients can interact directly, reducing delays and miscommunication.

Streamlines Transactions: Orders and requests are tracked efficiently in one platform.

Supports Local Farmers: Empowers small and medium-scale farmers to reach more clients.

Enhances Transparency: Both parties can view product details, order status, and updates in real-time.

Modern, User-Friendly Experience: Designed for easy navigation and usability on both desktop and mobile devices.

---

## 🚀 Features

- 🌾 **User Authentication**: Separate roles for Farmers, Clients, and Admin.
- 📦 **Product & Request Management**: Add, view, update, and manage products and requests.
- 📊 **Dashboard Analytics**: Overview of activity, requests, and user engagement.
- 🔔 **Notifications**: Alerts for new requests or updates.
- ⚡ **Future-ready Architecture**: Easy to scale and integrate new features.

---


## 🧰 Tech Stack

- **Backend:** Django (Python)
- **Frontend:** HTML, CSS (Bootstrap / custom styling)
- **Database:** SQLite3 (default)
- **Authentication:** OAuth 
- **Version Control:** Git + GitHub

---

## 📁 Project Structure

nutri/
│
├── nutriconnect/
│ ├── templates/nutriconnect/
│ │ ├── base.html
│ │ ├── home.html
│ │ ├── login.html
│ │ ├── register.html
│ │ ├── farmer_list.html
│ │ ├── farmer_form.html
│ │ ├── farmer_confirm_delete.html
│ │ ├── client_list.html
│ │ ├── client_form.html
│ │ ├── client_confirm_delete.html
│ ├── views.py
│ ├── models.py
│ ├── forms.py
│ ├── urls.py
│
└── manage.py

### 
## **Installation**

1. **Clone the repository**

```bash
git clone https://github.com/zaituni982/NUTRI2CONNECT.git
cd NUTRI2CONNECT
Create a virtual environment

bash
Copy code
python -m venv env
Activate the virtual environment

On Windows:

bash
Copy code
env\Scripts\activate
On Mac/Linux:

bash
Copy code
source env/bin/activate
Install dependencies

bash
Copy code
pip install -r requirements.txt
Apply migrations

bash
Copy code
python manage.py makemigrations
python manage.py migrate
Create a superuser (optional)

bash
Copy code
python manage.py createsuperuser
Run the development server

bash
Copy code
python manage.py runserver
Open http://127.0.0.1:8000 in your browser.



Usage

Log in as a Farmer / Client / Admin

Add or manage products and requests

View dashboard analytics

Receive notifications for updates



Roadmap / Future Improvements

Payment integration

Enhanced notifications & alerts

Advanced analytics & reporting

UI/UX refinements for mobile and desktop

API documentation for developers

Authors & Acknowledgments

Zaituni – Author / Maintainer

Contributors

Libraries & frameworks:Django 6

Python 3.14

SQLite (development)

HTML, CSS

Bootstrap / Custom Styles

📄 License

This project is open-source and available under the MIT License.

❤️ Support This Project

If you find NUTRI2CONNECT useful:

⭐ Star the repository

Share it with someone working in agriculture

Contribute ideas or improvements