# Compresor PDF

**Autor / Author:** Charlie Martínez – Quirinux GNU/Linux®  
**Licencia / License:** GPLv2.0

![Compresor PDF Screenshot](https://github.com/user-attachments/assets/6dab20ee-9023-40bf-a758-704057061609)

---

## 🧭 Descripción general / Overview

**ES:**  
`Compresor PDF` es una aplicación gráfica, multilingüe y sin conexión, diseñada para reducir el tamaño de archivos PDF utilizando **Ghostscript**.  

Pensada para usuarios de GNU/Linux, especialmente en entornos educativos u oficinas, permite seleccionar un archivo PDF y generar una copia más liviana.

**EN:**  
`PDF Compressor` is a graphical, multilingual, and offline application designed to reduce the size of PDF files using **Ghostscript**.  

Designed for GNU/Linux users, especially in educational or office settings, it allows you to select a PDF file and create a lighter copy.

---

## ✔️ Características / Features

**ES:**
- Compresión automática de PDFs mediante Ghostscript  
- Interfaz gráfica sencilla basada en tkinter  
- Soporte multilingüe: Español, Gallego, Francés, Alemán, Portugués, Italiano e Inglés  
- Detecta si Ghostscript no está instalado y muestra una advertencia  
- Uso completamente offline (no requiere conexión ni dependencias externas)  
- Optimizada para sistemas basados en Debian

**EN:**
- Automatic PDF compression using Ghostscript  
- Simple GUI based on tkinter  
- Multilingual interface: Spanish, Galician, French, German, Portuguese, Italian, English  
- Detects missing Ghostscript and warns the user  
- Fully offline usage (no internet or pip dependencies required)  
- Designed for Debian-based systems

---

## 📋 Requisitos / Requirements

**ES**  
Instalar las siguientes dependencias antes de ejecutar:  

**EN:**  
Install the following dependencies before running:

```bash
su root
apt install ghostscript python3-tk
```

---

## ▶️ Ejecución / How to Run

**ES:**  
Aplicación principal:  

**EN:**  
Main application:

```bash
git clone https://github.com/quirinux-so/quirinux-compresorpdf.git
cd quirinux-compresorpdf/usr/local/bin
python3 comprimirpdf.py
```

---

## 📦 Instalación alternativa / Optional Installation (Quirinux)

**ES:**  
Disponible como paquete oficial `.deb` desde el repositorio de Quirinux o desde el Centro de Software.

**EN:**  
Available as an official `.deb` package via the Quirinux repository or Software Center.

**Comando / Command:**

    su root
    apt install compresorpdf

**Repositorio / Repository:**  
[https://repo.quirinux.org/pool/main/c/compresorpdf](https://repo.quirinux.org/pool/main/c/compresorpdf)

---

## ⚖️ Aviso legal / Legal Notice

**ES:**  
Este proyecto forma parte del ecosistema **Quirinux**, pero es compatible con cualquier distribución moderna de GNU/Linux.  
Distribuido bajo los términos de la licencia **GPLv2**.

**EN:**  
This project is part of the **Quirinux** ecosystem but remains compatible with any modern GNU/Linux distribution.  
Released under the terms of the **GPLv2 license**.

**Autor / Author:** Charlie Martínez  
📧 <cmartinez@quirinux.org>

**Más información / More information:**  
[https://www.quirinux.org/aviso-legal](https://www.quirinux.org/aviso-legal)
