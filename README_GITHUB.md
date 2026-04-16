# 🛍️ Myntra Review Scraper

A powerful web scraping application that extracts and analyzes customer reviews from Myntra e-commerce platform.

## ✨ Features

- **🔍 Product Search**: Search for any product on Myntra
- **📊 Review Scraping**: Extract reviews from multiple products
- **💾 Database Storage**: Store reviews in MySQL database
- **📈 Data Visualization**: View and analyze scraped data
- **🌐 Web Interface**: Built with Streamlit for easy interaction

## 🚀 Quick Start

### Local Development
1. Clone this repository
2. Install dependencies: `pip install -r requirements.txt`
3. Set up `.env` file with MySQL credentials
4. Run: `streamlit run app.py`

### Cloud Deployment
This app is optimized for **Streamlit Community Cloud** deployment. See [STREAMLIT_DEPLOYMENT.md](STREAMLIT_DEPLOYMENT.md) for detailed instructions.

## 📋 Requirements

- Python 3.8+
- MySQL Database
- Streamlit
- Selenium (for web scraping)
- Chrome/ChromeDriver

## 🔧 Configuration

### Environment Variables
```bash
MYSQL_HOST=localhost
MYSQL_USER=root
MYSQL_PASSWORD=your_password
MYSQL_DATABASE=myntra_reviews
```

### Streamlit Cloud Secrets
For cloud deployment, use Streamlit secrets:
```toml
[mysql]
host = "your-cloud-mysql-host"
user = "your-mysql-user"
password = "your-mysql-password"
database = "myntra_reviews"
```

## 📱 Demo

Deployed on Streamlit Cloud: `https://your-app-name.streamlit.app`

## 🛠️ Tech Stack

- **Frontend**: Streamlit
- **Backend**: Python, Flask (alternative)
- **Database**: MySQL
- **Scraping**: Selenium, BeautifulSoup
- **Deployment**: Streamlit Community Cloud

## 📁 Project Structure

```
├── app.py                 # Main Streamlit application
├── application.py         # Flask alternative
├── src/
│   ├── cloud_io/         # Database operations
│   ├── constants/        # Application constants
│   ├── scrapper/         # Web scraping logic
│   └── utils/            # Utility functions
├── templates/            # Flask templates
├── static/              # Static assets
├── requirements.txt     # Python dependencies
└── packages.txt        # System dependencies for cloud
```

## 🌟 Features in Detail

### Product Search
- Search for any product by name
- Specify number of products to scrape
- Real-time search results

### Review Extraction
- Scrapes product ratings
- Extracts customer comments
- Captures reviewer information
- Records review dates

### Data Storage
- Automatic database creation
- Structured data storage
- Query and retrieve functionality

### Data Visualization
- Interactive dataframes
- Rating distributions
- Review sentiment analysis (future feature)

## 🔄 Deployment Options

1. **Streamlit Community Cloud** (Recommended - Free)
2. **Docker** (Self-hosted)
3. **Heroku** (Paid tier)
4. **AWS/GCP** (Enterprise)

## 🤝 Contributing

1. Fork this repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## ⚠️ Disclaimer

This tool is for educational purposes only. Please respect Myntra's terms of service and robots.txt file. Use responsibly and at your own risk.

## 🆘 Support

- 📧 Email: [your-email@example.com]
- 🐛 Issues: [GitHub Issues](https://github.com/your-username/myntra-review-scraper/issues)
- 💬 Discussions: [GitHub Discussions](https://github.com/your-username/myntra-review-scraper/discussions)

---

**Built with ❤️ using Streamlit and Selenium**
