# 💰 Personal Budget Tracker (Flask Web App)

Track your income and expenses easily, view summaries, and stay on top of your finances.

## 🔧 Built With
- Python + Flask
- SQLite (local database)
- Tailwind CSS (via CDN)

## 🚀 Features
- Add income or expense with amount, category, date, and note
- Categorize entries (e.g. Food, Rent, Entertainment)
- Monthly income and expense summary
- Export transactions to CSV
- Responsive UI with Tailwind

## 🛠️ Setup Instructions

1. **Clone the repo**
   ```bash
   git clone https://github.com/yourusername/budget_tracker.git
   cd budget_tracker
   ```

   2. **Create a virtual environment and activate it**
   ```bash
   python -m venv venv
   # On Windows
   venv\Scripts\activate
   # On macOS/Linux
   source venv/bin/activate
   ```

   3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

   4. **Run the application**
   ```bash
   python app.py
   ```
   The app will be available at [http://127.0.0.1:5000](http://127.0.0.1:5000).

   ## 📦 Project Structure

   ```
   expense_tracker/
   ├── app.py
   ├── requirements.txt
   ├── templates/
   │   └── ...
   ├── static/
   │   └── ...
   └── README.md
   ```

   ## 📝 Usage

   - Add new income or expense entries from the dashboard.
   - View monthly summaries and filter by category.
   - Export your transactions to CSV for backup or analysis.

   ## 🖌️ Customization

   - Edit categories in `app.py` or extend the database schema as needed.
   - Update styles in the `static/` folder or modify Tailwind CDN usage in templates.

   ## 🤝 Contributing

   Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

   ## 📄 License

   This project is licensed under the MIT License.
