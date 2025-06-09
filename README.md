# E-Commerce Price Comparison Scraper

## Overview
This project is a Flask-based web application that allows users to search for products on Amazon and Flipkart, compare prices within a custom range, and download the results as a text file. Built with Python, it uses web scraping techniques to fetch data from product listings, making it a handy tool for savvy online shoppers looking for the best deals.

## Features
- **Multi-Platform Search**: Scrape product listings from Amazon and Flipkart based on user-defined search terms.
- **Price Filtering**: Filter results by minimum and maximum price ranges.
- **User-Friendly Web Interface**: Simple web form to input search criteria and view results.
- **Downloadable Output**: Export search results as a text file for offline analysis.
- **Responsive Scraping**: Handles errors and CAPTCHAs gracefully with rate-limiting to respect website policies.

## Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Git (optional, for cloning the repository)

## Installation
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/scrapper.git
   cd ecommerce-scraper
   ```

2. **Set Up a Virtual Environment** (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

   The `requirements.txt` file includes:
   - Flask
   - pandas
   - requests
   - beautifulsoup4
   - fake-useragent

## Usage
1. **Run the Application**:
   ```bash
   python app.py
   ```
   The app will start in debug mode and be available at `http://localhost:5000`.

2. **Access the Web Interface**:
   - Open your browser and navigate to `http://localhost:5000`.
   - Enter a search term (e.g., "laptop"), optional price range, and select websites (Amazon, Flipkart, or both).
   - Submit the form to view results in a table.
   - Click "Download" to export the results as a `.txt` file.

3. **Example**:
   - Search Term: "wireless headphones"
   - Min Price: $20
   - Max Price: $200
   - Websites: Amazon, Flipkart
   - Output: A text file listing product names, prices, and links.

## Project Structure
- `app.py`: Main Flask application with routes for the web interface and file download.
- `scraper.py`: Contains functions to scrape Amazon and Flipkart product listings.
- `templates/`: Directory for HTML templates (`index.html`, `results.html`).
- `requirements.txt`: Lists Python dependencies.

## Notes
- **Web Scraping Ethics**: This tool is for personal, educational use only. Respect the terms of service of Amazon and Flipkart. Excessive or unauthorized scraping may result in CAPTCHAs or IP bans.
- **CAPTCHA Handling**: The scraper includes basic error detection for CAPTCHAs but may fail if websites block requests. Consider using APIs or proxies for production use.
- **Customization**: Modify `scraper.py` to adjust scraping logic, add more websites, or enhance filtering.

## Disclaimer
This project is for educational purposes and demonstrates web scraping techniques. Use responsibly and comply with all applicable laws and website policies. The author is not responsible for misuse or consequences of running this tool.

## Contributing
Feel free to fork the repository, create issues, or submit pull requests. Contributions to improve scraping reliability, add features, or enhance the UI are welcome!

## License
This project is licensed under the MIT License. See `
