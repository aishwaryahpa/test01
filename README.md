

# 🛒 SmartCart AI

SmartCart AI is an AI-powered e-commerce shopping assistant built using **Python, Streamlit, LangChain, Ollama, and Llama 3.2**.

The application helps users browse products, manage their shopping cart, compare products, get AI-powered recommendations, place orders, and track orders.

---

## 🚀 Features

- 🏠 **Home Dashboard**
  - Product statistics
  - AI model information
  - Ollama runtime information

- 🛍️ **Product Catalog**
  - Search products
  - Filter products by category
  - View product price and rating
  - View product descriptions

- 🛒 **Shopping Cart**
  - Add products
  - Remove products
  - Manage quantities
  - Calculate total price

- 🤖 **AI Shopping Assistant**
  - Powered by Llama 3.2
  - Local AI using Ollama
  - Product recommendations
  - Budget-based suggestions
  - Shopping recommendations for:
    - College
    - Travel
    - Fitness
    - Office
    - Study
    - Gifts
    - Daily use

- 📊 **Product Comparison**
  - Compare up to 3 products
  - AI-powered comparison
  - Customer suitability explanation

- 📦 **Order Tracking**
  - Track orders using Order ID
  - Display order status

- 💳 **Checkout**
  - Customer information
  - Payment method selection
  - Order placement
  - Automatic Order ID generation

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Backend and application logic |
| Streamlit | Web application framework |
| LangChain | LLM integration |
| Ollama | Local AI runtime |
| Llama 3.2 | AI language model |

---

## 📋 Requirements

Before running this project, make sure you have:

- Python 3.9 or higher
- Ollama
- Llama 3.2 model
- Internet connection for initial package/model installation

---

## 📥 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/smartcart-ai.git
cd smartcart-ai

Replace YOUR_USERNAME with your GitHub username.

2. Create a Virtual Environment
Windows
python -m venv venv
venv\Scripts\activate

macOS / Linux
python3 -m venv venv
source venv/bin/activate

3. Install Python Dependencies
pip install streamlit langchain langchain-core langchain-ollama

Or install from requirements.txt:

pip install -r requirements.txt

🦙 Ollama Setup
SmartCart AI uses Llama 3.2 through Ollama.

Install Ollama on your computer and download the Llama 3.2 model.

ollama pull llama3.2:latest

Check whether the model is installed:

ollama list

You can also test the model:

ollama run llama3.2:latest

The application connects to Ollama using:

http://127.0.0.1:11434

Make sure Ollama is running before starting the application.

▶️ Run the Application
Run the Streamlit application:

streamlit run app.py

If your Python file has another name, replace app.py with your filename.

For example:

streamlit run smartcart.py

After running the command, Streamlit will display a local URL such as:

http://localhost:8501

Open the URL in your browser.

📂 Project Structure
smartcart-ai/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
└── venv/

Files
app.py

Main Streamlit application containing:

Product catalog

Shopping cart

AI assistant

Product comparison

Order tracking

Checkout

requirements.txt

Contains all required Python packages.

README.md

Project documentation.

.gitignore

Prevents unnecessary files from being uploaded to GitHub.

📦 Products
The application currently contains the following products:

Product	Price	Category	Rating
Laptop	₹55,000	Electronics	⭐ 4.5
Smartphone	₹25,000	Electronics	⭐ 4.3
Headphones	₹3,000	Accessories	⭐ 4.2
Smart Watch	₹5,000	Wearables	⭐ 4.4
Bluetooth Speaker	₹2,500	Accessories	⭐ 4.1
Running Shoes	₹3,500	Fashion	⭐ 4.6
Backpack	₹1,800	Fashion	⭐ 4.3
Coffee Maker	₹4,500	Home	⭐ 4.2

🤖 AI Assistant Examples
You can ask the AI assistant questions such as:

Which product is suitable for travel?

I am a college student. What should I buy?

Suggest a product for fitness.

Which product is suitable for office work?

I have a budget of ₹5000. What can I buy?

The AI is configured to recommend products only from the available SmartCart catalog.

🧠 How the AI Works
SmartCart AI uses LangChain to communicate with the Llama 3.2 model running locally through Ollama.

The application provides the product catalog to the AI model and instructs it to:

Use only products available in the catalog.

Never invent products.

Never invent product prices.

Understand the customer's requirements.

Recommend suitable products.

Explain why a product is suitable.

Answer only SmartCart-related shopping questions.

AI Architecture
User
  │
  ▼
Streamlit Interface
  │
  ▼
SmartCart AI
  │
  ▼
LangChain
  │
  ▼
Ollama
  │
  ▼
Llama 3.2
  │
  ▼
AI Response

🛒 Application Flow
Home
 │
 ├── Products
 │      └── Search / Filter / Add to Cart
 │
 ├── Cart
 │      └── Manage Products / Calculate Total
 │
 ├── AI Assistant
 │      └── AI Product Recommendations
 │
 ├── Compare
 │      └── Compare Products Using AI
 │
 ├── Order Tracking
 │      └── Track Order
 │
 └── Checkout
        └── Place Order

⚠️ Current Limitations
This project is currently a prototype/demo e-commerce application.

Product information is stored directly in Python.

Cart information uses Streamlit session state.

Orders are stored temporarily in session state.

No permanent database is currently used.

Payment processing is simulated.

Order tracking is simulated.

User authentication is not implemented.

Product inventory management is not implemented.

The AI assistant requires Ollama to be running locally.

Restarting the application can reset cart and order information.

🔮 Future Improvements
Future versions can include:

🔐 User authentication

🗄️ MySQL/PostgreSQL database

💳 Real payment gateway

📦 Inventory management

🚚 Advanced order tracking

❤️ Wishlist

⭐ Customer reviews

🧠 Advanced AI recommendations

🔎 Semantic product search

🖼️ Product images

👤 User profiles

📊 Admin dashboard

📱 Mobile-friendly interface

☁️ Cloud deployment

🔒 Privacy
The AI model is currently executed locally using Ollama.

No cloud AI API key is required for the current implementation.

Do not upload passwords, API keys, database credentials, or other sensitive information to GitHub.

📄 License
This project is created for educational and demonstration purposes.

You can add an open-source license such as the MIT License if you want to allow others to use and modify the project.

👨‍💻 Author
Your Name

GitHub: https://github.com/YOUR_USERNAME

⭐ Support
If you find this project useful, please consider giving the repository a ⭐ on GitHub.

🛒 SmartCart AI
Shop Smarter. Choose Better. Powered by AI. 🤖

Also create a **`requirements.txt`** file in the same GitHub folder:

```text
streamlit
langchain
langchain-core
langchain-ollama

Your GitHub project can then have:

smartcart-ai/
├── app.py
├── requirements.txt
├── README.md
└── .gitignore