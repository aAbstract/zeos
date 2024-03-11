# ZEOS

## Description
ZEOS is an IoT OS based on MicroPython

## Features

### 1. Kernel
The kernel is the core component of the OS.  
It manages system resources and provides essential services.  
It Sets up the foundation layer for higher-level software to run.  

<b>Kernel Components:</b>  
- Basic Kernel Data Structures - **IN_PROGRESS**
- File System (VFS Integration) - **IN_PROGRESS**
- Networking (HTTP MQTT ESP-NOW Integration) - **IN_PROGRESS**
- Device Drivers - **TODO**
- [x] Multitasking and Process Scheduling
- [x] Memory Manager

### 2. Shell
The shell is a text based interface that allows users to interact with ZEOS kernel.  

<b>Shell Capabilities:</b>  
- Device Config - **IN_PROGRESS**
- Cron Jobs - **TODO**
- File System API - **IN_PROGRESS**
- [x] GPIO API
- [x] I2C API
- OTA Firmware Update - **TODO**
- Shell Scripting: - **IN_PROGRESS**
    - Unix Shell Utilities
    - Shell Scripting
    - User Management and Access Control

### 3. Web Dashboard
A lightweight web dashboard served via device's builtin webserver.  

<b>Dashboard Features:</b>
- Device Resources Monitor - **TODO**
- A Terminal Connected to ZEOS Shell over HTTP - **TODO**
- System Configurations Portal - **TODO**
- Simple File Explorer and Text Editor - **TODO**

### 4. Firmware OTA Update - **TODO**
