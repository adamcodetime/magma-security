# 🌋 Magma Security

**Web Safety for Everyone**

Magma Security is a native macOS application built by **Magma** that helps users evaluate the safety and trustworthiness of websites before interacting with them.

Created for a school hackathon, the project aims to make online safety more accessible through a simple, fast, and user-friendly experience.

---

## ✨ Features

* Quiz
* Share your score
* Exit from trivia
* Dark and Light mode switcher

---

## 🚀 Download

Download the latest macOS release from the project page:

**Magma Security.app.zip**

1. Download the ZIP file
2. Extract the archive
3. Open the application

---

## 🍎 Installing on macOS

Because Magma Security is a hackathon project and may not be notarized by Apple, macOS may display a warning on first launch.

To open the application:

1. Right-click **Magma Security.app**
2. Select **Open**
3. Click **Open** again when prompted

After the first launch, the app should open normally.

---

## 🛠 Building From Source

### Requirements

* macOS 14+
* Xcode 16+
* Swift 5.10+

### Clone the Repository

```bash
git clone https://github.com/adamcodetime/magma-security.git
cd magma-security
```

### Open the Project

```bash
open "Magma Security.xcodeproj"
```

Or open the project manually in Xcode.

### Configure Signing

1. Open Xcode
2. Select the project
3. Select the **Magma Security** target
4. Open **Signing & Capabilities**
5. Choose your Apple ID under **Team**

A free Personal Team account is sufficient for local development.

### Run the Application

1. Select **My Mac** as the target device
2. Press **⌘R**

### Build a Release Version

```bash
xcodebuild \
-scheme "Magma Security" \
-configuration Release
```

---

## 🎯 Motivation

Online scams, phishing attacks, and malicious websites continue to affect millions of users every year.

Magma Security was created to explore how software can help people make safer decisions online by providing clear information about websites before they interact with them.

---

## ⚠️ Disclaimer

Magma Security is a student hackathon project intended for educational and demonstration purposes.

The application should not be considered a replacement for professional cybersecurity software, enterprise security solutions, or expert security advice.

Always use your own judgment when browsing online.

---

## 👥 Team

Built by **Magma**

School Hackathon 2025

---

## 📄 License

This project is provided for educational purposes.

© 2025 Magma
