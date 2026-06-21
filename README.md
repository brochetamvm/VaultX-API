# VaultX API 📦🔒

Choose your language / Scegli la tua lingua:
* [English](#-english-version)
* [Italiano](#-versione-italiana)

---

## 🇺🇸 English Version

**VaultX API** is a robust, scalable, and secure backend solution designed for efficient inventory and product management. Built with modern Python frameworks, it acts as the central "vault" for inventory systems, providing fast and reliable data operations.

### 🚀 Key Features
* **Asynchronous Architecture:** Built with **FastAPI** for non-blocking, high-performance requests.
* **Strict Data Validation:** Utilizes **Pydantic** to ensure data integrity and proper formatting before reaching the database.
* **Professional Data Persistence:** Integrates **SQLAlchemy** (ORM) for secure database mapping. Currently configured with SQLite for portability, but production-ready for PostgreSQL.
* **Automated Documentation:** Interactive API documentation via **Swagger/OpenAPI** built-in natively, making frontend integration seamless.
* **Containerized:** Fully ready for production and cloud deployment using **Docker**.

### 🛠️ Tech Stack
![Python](https://img.shields.io/badge/Python-3.12+-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=flat&logo=fastapi)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-red.svg)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat&logo=docker&logoColor=white)

### 🐳 How to Run (with Docker)
Running the VaultX API is incredibly simple using Docker. You don't need to install Python or any dependencies locally on your machine.

1. **Build the image:**
   ```bash
   docker build -t vaultx-api .
   ```

2. **Run the container:**
   ```bash
   docker run -p 8000:8000 vaultx-api
   ```

3. **Access the documentation:**
   Open your browser and navigate to: `http://localhost:8000/docs`

---

## 🇮🇹 Versione Italiana

**VaultX API** è una soluzione backend robusta, scalabile e sicura, progettata per una gestione efficiente dell'inventario e dei prodotti. Sviluppata con framework Python moderni, funge da "cassaforte" (vault) centrale per i sistemi di inventario, garantendo operazioni sui dati rapide e affidabili.

### 🚀 Caratteristiche Principali
* **Architettura Asincrona:** Sviluppata con **FastAPI** per gestire le richieste in modo non bloccante e ad alte prestazioni.
* **Validazione Rigorosa dei Dati:** Utilizza **Pydantic** per garantire l'integrità e la corretta formattazione dei dati prima che raggiungano il database.
* **Persistenza dei Dati Professionale:** Integra **SQLAlchemy** (ORM) per una mappatura sicura del database. Attualmente configurato con SQLite per portabilità, ma pronto per la produzione con PostgreSQL.
* **Documentazione Automatica:** Documentazione API interattiva tramite **Swagger/OpenAPI** inclusa nativamente, rendendo l'integrazione frontend un processo fluido.
* **Containerizzato:** Completamente pronto per la produzione e il deployment in cloud tramite **Docker**.

### 🛠️ Tecnologie Utilizzate
![Python](https://img.shields.io/badge/Python-3.12+-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=flat&logo=fastapi)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-red.svg)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat&logo=docker&logoColor=white)

### 🐳 Come Eseguire (con Docker)
Eseguire la VaultX API è incredibilmente semplice grazie a Docker. Non è necessario installare Python o altre dipendenze localmente sul tuo computer.

1. **Costruisci l'immagine (Build):**
   ```bash
   docker build -t vaultx-api .
   ```

2. **Avvia il container (Run):**
   ```bash
   docker run -p 8000:8000 vaultx-api
   ```

3. **Accedi alla documentazione:**
   Apri il browser e vai su: `http://localhost:8000/docs`