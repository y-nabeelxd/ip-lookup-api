# IP Lookup API 🔍

A simple Python tool to fetch IP address details using the IPFind API.  
This script automatically manages API keys, checks for API usage limits, and provides detailed information about any IP address.

---

## ⚙️ Features
- Checks `.env` file for an API key.
- If the key exists, it verifies whether the API limit has been reached.
- If the key is missing or invalid, prompts the user to enter and save a new API key.
- Fetches and displays detailed IP address information including country, city, timezone, and more.

---

## 📦 Installation
### **Step 1: Clone the Repository**
```
git clone https://github.com/y-nabeelxd/ip-lookup-api
cd ip-lookup-api
```

### **Step 2: Install Required Packages**
```
pip install -r requirements.txt
```

---

## 🚀 Usage
### **Run the script:**
```
python ip.py
```

### **How It Works:**
- If the `.env` file exists and contains a valid API key:
  - The script checks if the API has reached its limit.
  - If not, it asks for an IP address and displays the details.
- If no API key is found:
  - It prompts the user to create an account on **[IPFind](https://ipfind.com/signup)**.
  - Asks for an API key and saves it in `.env` for future use.
  - Then, it fetches IP address details.

---

## 🔥 Example Output
### ✅ **When API key is valid:**
```
Enter IP Address: 8.8.8.8

IP Address Details:
IP Address: 8.8.8.8
Country: United States (US)
City: Mountain View
Region: California (CA)
Continent: North America (NA)
Timezone: America/Los_Angeles
Latitude: 37.386
Longitude: -122.0838
Currency: USD
Languages: en-US, es-US, haw, fr
```

### ❌ **When API key is missing:**
```
Please create an account  
https://ipfind.com/signup  (blue color)

(waiting 10 seconds...)

Must confirm your email to activate your API key.  
Must check and confirm your API before using this tool.  

(waiting 20 seconds...)

Enter your API KEY: 123456-abcdef-ghijkl

(screen clears)

Enter IP Address:
```

---

## 🛠️ Configuration
- API key is stored in a `.env` file:
```
API=your_api_key_here
```
- If the API key is missing or invalid, the script prompts for a new one.

---

## 📝 License
This project is open-source under the [MIT License](LICENSE).

---

## 🤝 Contributing
Want to improve this project? Feel free to fork the repository and submit a pull request!

---

## 📧 Contact
**GitHub:** [y-nabeelxd](https://github.com/y-nabeelxd)  
