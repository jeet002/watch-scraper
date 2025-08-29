# 🕒 Snapdeal Watch Scraper (Under ₹2000)

A Python-based web scraping project that extracts **watch details** from Snapdeal’s search results for *“Watches for Men under 2000”*.  
This project demonstrates how to use `requests`, `BeautifulSoup`, and `pandas` to collect, process, and store product data.

## 📌 Features
- Scrapes the **first page** of Snapdeal search results.  
- Extracts:
  - ✅ Watch Name  
  - ✅ Price (₹)  
  - ✅ Brand (parsed from product info)  
  - ✅ Availability (In Stock / Out of Stock)  
- Filters out watches **priced above ₹2000**.  
- Saves data into:
  - `snapdeal_watches_html.txt` → raw HTML content  
  - `snapdeal_watches_under_2000.xlsx` → structured data in Excel format  

## 🛠️ Technologies Used
- **Python 3**  
- [Requests](https://docs.python-requests.org/) → Fetch HTML content  
- [BeautifulSoup (bs4)](https://www.crummy.com/software/BeautifulSoup/) → Parse HTML  
- [pandas](https://pandas.pydata.org/) → Store and export data  

## 📂 Project Structure
📁 Snapdeal-Watch-Scraper
├── 📄 scraper.py # Main Python script
├── 📄 snapdeal_watches_html.txt # Saved HTML (first page)
├── 📄 snapdeal_watches_under_2000.xlsx # Extracted data in Excel
└── 📄 README.md # Project documentation

## ▶️ How to Run
1. **Clone the repository** (or download the project files):  
   - git clone https://github.com/your-username/Snapdeal-Watch-Scraper.git
   - cd Snapdeal-Watch-Scraper
2. Install dependencies from requirements.txt:
   - pip install -r requirements.txt
3. Run the scraper:
   - python watch_scraper.py
4. Check results:
   - HTML saved → snapdeal_watches_html.txt
   - Excel file → snapdeal_watches_under_2000.xlsx
