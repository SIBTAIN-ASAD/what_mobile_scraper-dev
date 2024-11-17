
<div align="center">

# <span style="color:#4CAF50;">WhatMobile Scraper</span>

Scrape mobile phone details with ease using this sophisticated Scrapy project designed for the WhatMobile website.

[![Python](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/)

</div>

---

## <span style="color:#FFD700;">Overview</span>

🚀 The WhatMobile Scraper is a powerful tool that effortlessly extracts mobile phone details from the popular WhatMobile website. This project employs Scrapy, a robust and extensible web scraping framework for Python.

## <span style="color:#9400D3;">Features</span>

- **Ease of Use:** With a simple command, you can start scraping data and gathering valuable insights.
- **Data Formats:** The scraper automatically saves scraped data in both JSON and CSV formats.
- **Error Handling:** Any errors that occur during the scraping process are logged in the <span style="color:#FF6347;">`logfile.log`</span> file for easy debugging.

## <span style="color:#008000;">How to Run</span>

### <span style="color:#1E90FF;">Prerequisites</span>

Make sure you have [Python](https://www.python.org/downloads/) (version 3.8 or higher) installed.

### <span style="color:#1E90FF;">Installation</span>

```bash
git clone https://github.com/Muhammad-Sibtain-Asad/what_mobile_scraper.git
cd what_mobile_scraper
pip3 install -r requirements.txt
```

### <span style="color:#1E90FF;">Run the Scraper</span>

```bash
scrapy crawl whatspider 2> logfile.log
```

This command initiates the scraper, and logs redirected to the <span style="color:#FF6347;">`logfile.log`</span> file.

## <span style="color:#008000;">Output</span>

The scraped data is automatically stored in two formats:

- 📄 **JSON:** The data is saved in <span style="color:#4169E1;">`output.json`</span>.
- 📊 **CSV:** The data is saved in <span style="color:#4169E1;">`output.csv`</span>.

## <span style="color:#9400D3;">Additional Details</span>

During the scraping process, the program will prompt you to enter a Sr. No for additional details. This prompt is triggered by the <span style="color:#FF6347;">`close_spider`</span> method, allowing you to fetch extra information for a specific item.

Additionally, all item details, including the additional information, are saved in <span style="color:#4169E1;">`details.json`</span>.

## <span style="color:#FF4500;">License</span>

This project is licensed under the MIT License - see the <span style="color:#FF6347;">[LICENSE](LICENSE)</span> file for details.

---

**Happy Scraping!** 🕷️📱