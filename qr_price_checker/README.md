# 🏷️ QR Price Checker – Python + Flask + TailwindCSS

A practical barcode/QR price checking web app built with **Python (Flask)** and styled using **TailwindCSS**. Enter or scan a barcode to fetch product details: name, price, and stock status.

---

## 🚀 Features

- 🔍 Lookup items by barcode
- 🧾 Show item name, price (₦), and stock
- 💻 Responsive UI with TailwindCSS
- 🗃️ Lightweight SQLite database
- ✅ Barcode scanner/QR integration ready

---

## 🛠️ Tech Stack

- **Backend**: Python, Flask  
- **Frontend**: HTML, TailwindCSS  
- **Database**: SQLite

---

## 📂 Folder Structure

```
qr_price_checker/
├── app.py                # Flask application
├── database.py           # SQLite DB initializer
├── templates/
│   ├── index.html        # Barcode input form
│   └── result.html       # Result display
└── data.db               # SQLite database
```

---

## 📦 Setup Instructions

1. **Clone the project**
    ```bash
    git clone https://github.com/yourusername/qr_price_checker.git
    cd qr_price_checker
    ```

2. **Create the database**
    ```bash
    python database.py
    ```

3. **Run the app**
    ```bash
    python app.py
    ```

4. **Open in browser**  
    Go to [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 💡 Example Barcode for Testing

Use:

```
1234567890
```

Sample Output:

```
Item: Example Item
Price: ₦4500.00
Stock: 25
```

---

## 📲 Coming Soon

* 📸 Mobile barcode/QR scanner integration
* 🧾 Export scanned records (CSV/PDF)
* 🖨️ Printable receipts for retail

---

## 👨‍💻 Author

**Emmanuel Tar**  
Python Developer & Tech Enthusiast  
📩 [LinkedIn](https://www.linkedin.com/in/emmanueltar)

---

## 📄 License

Open source under the [MIT License](LICENSE).

---

*Want a custom badge section or GitHub-optimized README? Let me know!*
```
