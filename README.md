# IP Address External Geoloaction Locator / Localizador de IP e Geolocalização Externa

<p align="center">
  <a href="#en-us-english">English</a> | 
  <a href="#pt-br-português">Português</a>
</p>

---

## EN-US (English)

A Python-based command-line tool that consumes a public web API to capture, parse, and store detailed geographical and infrastructure intelligence about any given IP address. It automatically records the historical lookup data inside a persistent local relational database.

This is the third project in my personal portfolio, designed to demonstrate web data ingestion, data serialization formats, and relational database mechanics.

### 🚀 Features

- **External API Ingestion:** Real-time data fetching using asynchronous-friendly HTTP methods over public endpoints.
- **Relational Data Persistence:** Structured query architecture utilizing SQLite to log and track multiple lookup attributes efficiently without relying on text files.
- **Dynamic Input Handler:** Capable of scanning custom input parameters or dynamically shifting to isolate and check the host's own public WAN address.
- **Data Abstraction:** Isolates JSON communication protocols into clean internal native dictionary types (`.get()`).

### 🛠️ Technologies Used

- **Python 3**
- **Requests Library** (Third-party HTTP client for web parsing)
- **SQLite3** (Native relational database management system)
- **Git & GitHub**

### 📖 What I Learned From This Project

- **API Integrations & JSON Routing:** Mastered HTTP GET requests, status codes responses, and mapping complex structural formats down to local attributes.
- **SQL & Database Management:** Writing clean database initialization queries (`CREATE TABLE IF NOT EXISTS`), structure constraints (`PRIMARY KEY AUTOINCREMENT`), and parameter binding methods (`?`) to write log files securely.
- **Package Management (PIP):** Installing, configuring, and working with modular external abstractions outside the core standard Python package tree.

### 🔧 How to Run

1. Clone this repository:
   ```bash
   git clone (https://github.com/luizsantos540/localizador-ip.git)

2. Navigate to the project directory:
   cd localizador-ip

3. Install dependencies:
   pip install requests

4. Run teh Script:
   python main.py      