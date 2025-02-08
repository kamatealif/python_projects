# Currency Converter Web App

## 📌 Overview

The **Currency Converter Web App** is a simple Flask-based application that allows users to convert currency values using real-time exchange rates fetched from an API.

## 🚀 Features

- ✅ Real-time exchange rates using **ExchangeRate-API**
- ✅ User-friendly UI with dropdowns for selecting currencies
- ✅ Responsive design with a clean interface
- ✅ Conversion result displayed instantly
- ✅ Secure and lightweight

## 🛠️ Tech Stack

- **Backend:** Flask (Python)
- **Frontend:** HTML, CSS, JavaScript
- **API:** ExchangeRate-API

## 📂 Project Structure

```
📦 currency-converter-app
│-- 📂 static          # CSS and other static files
│-- 📂 templates       # HTML templates
│-- app.py            # Flask backend
│-- requirements.txt  # Dependencies
│-- .env              # API keys and environment variables
│-- README.md         # Project documentation
```

## 📥 Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-repo/currency-converter.git
   cd currency-converter
   ```
2. **Set up a virtual environment (Optional but recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Mac/Linux
   venv\Scripts\activate     # Windows
   ```
3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
4. **Set up environment variables:**
   - Create a `.env` file in the root directory.
   - Add your ExchangeRate-API key:
     ```env
     API_KEY=your_api_key_here
     ```
5. **Run the Flask app:**
   ```bash
   python app.py
   ```
6. **Open the app in your browser:**
   ```
   http://127.0.0.1:5000/
   ```

## ⚙️ Usage

1. Enter the **amount** you want to convert.
2. Select the **currency** to convert from.
3. Select the **currency** to convert to.
4. Click **Convert**, and the result will be displayed instantly.

## 📌 API Used

- [ExchangeRate-API](https://www.exchangerate-api.com/) (Free for basic usage)

## 🎯 Future Enhancements

- 🌙 **Dark Mode Toggle**
- 📊 **Conversion history feature**
- 📌 **Currency symbols support**
- 📈 **Graphical representation of rates over time**
- 🔔 **Notifications for rate changes**

## 🏆 Contributing

Feel free to contribute to this project! Fork, make your changes, and create a pull request. 🚀

## 📝 License

This project is open-source and available under the **MIT License**.

---

Made with ❤️ by [Your Name]

