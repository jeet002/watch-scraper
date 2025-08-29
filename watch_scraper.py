import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

def scrape_snapdeal_watches():
    """Scrape watch data from Snapdeal (first page, under 2000₹)"""

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/91.0.4472.124 Safari/537.36"
    }

    url = "https://www.snapdeal.com/search?keyword=watches%20for%20men%20under%202000"

    # 1. Fetch HTML content
    response = requests.get(url, headers=headers, timeout=10)
    if response.status_code != 200:
        print("❌ Failed to fetch page. Status code:", response.status_code)
        return None

    # 2. Save HTML content to txt
    with open("snapdeal_watches_html.txt", "w", encoding="utf-8") as f:
        f.write(response.text)
    print("✅ HTML content saved to snapdeal_watches_html.txt")

    soup = BeautifulSoup(response.text, "html.parser")

    watch_names, prices, brands, availability = [], [], [], []

    # 3. Identify product blocks
    products = soup.find_all("div", class_="product-tuple-description")

    for product in products:
        # Extract fields
        name_tag = product.find("p", class_="product-title")
        price_tag = product.find("span", class_="product-price")
        brand_tag = product.find("p", class_="product-brand")

        if name_tag and price_tag:
            name = name_tag.get_text(strip=True)
            price_text = price_tag.get_text(strip=True)

            # Clean price (remove ₹ and commas)
            price_match = re.findall(r"\d+", price_text.replace(",", ""))
            price_val = int("".join(price_match)) if price_match else 0

            # Skip if price > 2000
            if price_val > 2000:
                continue

            # Brand: either given, or first word of name
            brand = brand_tag.get_text(strip=True) if brand_tag else name.split()[0]

            # Availability (Snapdeal usually shows if out of stock, else assume In Stock)
            availability_status = "In Stock"
            if "out of stock" in product.get_text(strip=True).lower():
                availability_status = "Out of Stock"

            # Append to lists
            watch_names.append(name)
            prices.append(price_val)
            brands.append(brand)
            availability.append(availability_status)

    # 4. Create DataFrame
    df = pd.DataFrame({
        "Watch Name": watch_names,
        "Price (₹)": prices,
        "Brand": brands,
        "Availability": availability
    })

    # 5. Save to Excel
    df.to_excel("snapdeal_watches_under_2000.xlsx", index=False)
    print("✅ Data saved to snapdeal_watches_under_2000.xlsx")

    return df


if __name__ == "__main__":
    print("📌 Starting Snapdeal Watch Scraper")
    print("=" * 50)

    df = scrape_snapdeal_watches()

    if df is not None:
        print("\n📊 First few records:")
        print(df.head(10))
        print(f"\n🔢 Total watches scraped: {len(df)}")
