<h1 align="center"> Decentralized AI-Driven Marketplace </h1>
<p align="center">
  <img src="static/images/v4/qt-black-transparent.png" alt="QuantumTrade Logo" width="400">
</p>

Welcome to **QuantumTrade**, a decentralized AI-powered blockchain marketplace built using **Django**, blockchain integration for secure transactions and an AI recommendation system to personalize user experiences.

## Features

- **User Authentication**: JWT, SSO, and MFA support.
- **Product Listings**: Users can list, view, and search products.
- **AI Recommendations**: Personalized product recommendations based on user behavior.
- **Blockchain Transactions**: Smart contract integration for secure payments.
- **Admin Dashboard**: Marketplace management by admins.

## 📂 Project Directory Structure

```
decentralized-ai-marketplace/      # 🏗️ Root directory (Git Repository)
│── QuantumTrade/                   # 📂 Main Django App (Core Settings)
│   ├── settings.py                   # ⚙️ Django settings file
│   ├── urls.py                       # 🌍 URL routing
│   ├── wsgi.py                       # 🚀 WSGI entry point
│   ├── asgi.py                       # 🚀 ASGI entry point (for WebSockets)
│   ├── templates/                    # 📂 Django Templates
│   │   ├── base.html                  # 🖼️ Base HTML template
│   │   ├── index.html                 # 🖼️ Main HTML template
│   │   ├── includes/                  # 🏗️ Common UI Components
│   │   │   ├── navbar.html             # 🏠 Navigation bar
│   │   │   ├── footer.html             # 📄 Footer
│
│── users/                            # 👤 Users Management App
│   ├── models.py                       # 🗃️ User Models
│   ├── views.py                        # 🖥️ User Views
│   ├── urls.py                         # 🌍 User Routes
│   ├── forms.py                        # ✍️ Forms for user auth
│   ├── templates/                      # 📂 User-related templates
│   │   ├── login.html                   # 🔑 Login Page
│   │   ├── signup.html                  # 📝 Signup Page
│   │   ├── profile.html                 # 👤 User Profile
│
│── marketplace/                       # 🏪 Digital Assets Marketplace App
│   ├── models.py                        # 🛒 NFT & Assets Models
│   ├── views.py                         # 🏬 Marketplace Views
│   ├── urls.py                          # 🌍 Marketplace Routes
│   ├── templates/                       # 📂 Marketplace Templates
│   │  ├── listings.html                   # 📃 Asset Listings
│   │  ├── details.html                    # 🏷️ Asset Details
│
│── blockchain/                         # ⛓️ Blockchain Integration App
│   ├── models.py                         # 🗃️ Blockchain Models (Transactions, Ownership)
│   ├── views.py                          # 🖥️ Blockchain Interaction Views
│   ├── urls.py                           # 🌍 Blockchain API Routes
│   ├── utils.py                          # 🛠️ Blockchain Helper Functions
│
│── ai/                                  # 🤖 AI-based Personalization App
│   ├── models.py                         # 🧠 AI Models
│   ├── views.py                          # 🖥️ AI API Views
│   ├── urls.py                           # 🌍 AI Routes
│
│── static/                              # 🎨 Static Files (Processed by Webpack)
│   ├── dist/                             # 📂 Webpack output (final minified files)
│   │   ├── js/                           # 📂 Minified JS files
│   │   │   ├── main.min.js               # 🎛️ Main bundled JS
│   │   │   ├── runtine.min.js            # 🔑 WalletKit script
│   │   │   ├── vendors.min.js            # 🔧 Vendors script
│   │   │   ├── styles.min.css            # 🎨 Main compiled SCSS
│   ├── images/                           # 🖼️ Static images
│   ├── scss/                             # 🎨 SCSS Files
│   │   ├── abstracts/                    # 🎨 Variables, Mixins, Functions
│   │   ├── base/                         # 🌎 Base styles (Typography, Resets)
│   │   ├── layout/                       # 📐 Grid, Containers, Sections
│   │   ├── components/                   # 🔧 Buttons, Modals, Forms
│   │   ├── themes/                       # 🎭 Dark/Light Mode
│   │   ├── styles.scss                   # 🎨 Main SCSS Entry
│
│── k8s/                                 # ⚡ Kubernetes Deployment Files
│   ├── quantum-trade-deployment.yml       # 🛠️ K8s Deployment Config
│
│── package.json                           # 📦 Node Package Manager (NPM)
│── webpack.config.mjs                     # ⚙️ Webpack Configuration (ESM)
│── manage.py                              # 🚀 Django Command-Line Utility
│── requirements.txt                       # 📜 Python dependencies
│── .gitignore                             # 🚫 Git Ignore Unwanted Files
│── Dockerfile                             # 🐳 Docker Setup (If Needed)
│── README.md                              # 📖 Project Documentation
```

---

## 🚀 Setup & Installation

### 1️⃣ **Clone the Repository**
```bash
git clone https://github.com/niral-nadisara/decentralized-ai-marketplace.git
cd decentralized-ai-marketplace
```

### 2️⃣ **Set Up Python Environment & Install Dependencies**
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
pip install -r requirements.txt
```

### 3️⃣ **Apply Migrations & Create Superuser**
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

### 4️⃣ **Run Django Development Server**
```bash
python manage.py runserver
```

---

## 🎨 Frontend Setup (SCSS, Webpack, JavaScript Modules)

### 1️⃣ **Install NPM Dependencies**
```bash
npm install
```

### 4️⃣ **Clear Node Modules & Reinstall (If Needed)**
```bash
rm -rf node_modules package-lock.json
npm install
```

---

## ⚡ Useful Development Commands
| Task | Command |
|-----------------|------------------------------------------------|
| Start Django Server | `python manage.py runserver` |
| Run Migrations | `python manage.py migrate` |
| Create Superuser | `python manage.py createsuperuser` |
| Install Python Dependencies | `pip install -r requirements.txt` |
| Install JS Dependencies | `npm install` |
| Clear Cache & Reinstall Node Modules | `rm -rf node_modules package-lock.json && npm install` |

---

## 🤝 Contributing
Our team from **Clark University** is developing this project as part of the **Advanced Software Engineering** course.
Contributions are welcome from team members! Please follow these steps:
1. **Clone the repo**
2. **Create a new branch** (`feature-branch`)
3. **Commit changes** (`git commit -m "Added new feature"`)
4. **Push and create a PR**
5. **Request for review**

---

## 📜 License
This project is licensed under the **MIT License**.

🚀 **Happy Coding!** 🎉

