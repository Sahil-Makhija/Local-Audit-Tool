# Local Audit Tool (Security Configuration Scanner)

A tool for scanning and identifying dangerous settings in common network service configurations.

## Overview

This security tool helps system administrators and security professionals identify potentially dangerous configurations in network services such as:

- FTP (File Transfer Protocol)
- SMB (Samba)
- NFS (Network File System)

## Features

- Scans configuration files for security issues
- Identifies dangerous settings with clear explanations
- Easy to use command-line interface
- Modular design for adding new protocol scanners

## Usage

### 🛠️ Prerequisites

Make sure you have:

- Python 3.7+

### 📦 Installation

- **Clone the repository:**

  ```bash
  $ git clone https://github.com/Sahil-Makhija/Local-Audit-Tool.git
  $ cd Local-Audit-Tool
  ```

<!-- 2. **Install dependencies (if any):**

   > 💡 If you plan to use additional libraries later, add a `requirements.txt` — for now, this assumes only Python standard libraries are used. -->

### 🚀 Running the Tool

To run the tool for a specific protocol:

    python3 main.py <protocol>

**Example:**

    python3 main.py smb

This will scan the Samba (SMB) configuration file (usually `/etc/samba/smb.conf`) and report any dangerous or insecure settings it finds.

### 📚 Supported Protocols

| Protocol | Description                      | Config File Location (default) |
| -------- | -------------------------------- | ------------------------------ |
| ftp      | FTP (File Transfer Protocol)     | /etc/vsftpd.conf               |
| smb      | Samba (SMB) file sharing service | /etc/samba/smb.conf            |
| nfs      | NFS (Network File System)        | /etc/exports                   |
