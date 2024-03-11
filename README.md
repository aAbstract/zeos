# ZEOS

## Description
ZEOS is an IoT OS based on MicroPython

## Features

### 1. Kernel
The kernel is the core component of the OS.  
It manages system resources and provides essential services.  
It Sets up the foundation layer for higher-level software to run.  

<b>Kernel Components:</b>  
- [ ] Events Module - **IN_PROGRESS**
- [ ] File System (VFS Integration) - **IN_PROGRESS**
- [ ] HTTP, MQTT Integration - **IN_PROGRESS**
- [ ] ESPNOW Integration
- [x] Simple RPC Implementation
- [x] Device Drivers
- [x] Multitasking and Process Scheduling
- [x] Memory Manager

### 2. Shell
The shell is a text based interface that allows users to interact with ZEOS kernel.  

<b>Shell Capabilities:</b>  
- [ ] Device Config - **IN_PROGRESS**
- [ ] Cron Jobs
- [ ] File System API - **IN_PROGRESS**
- [x] GPIO API
- [x] I2C API
- [ ] OTA Firmware Update
- [ ] Shell Scripting:
    - [x] Unix Shell Utilities
    - [x] Shell Scripting
    - [ ] User Management and Access Control

### 3. Web Dashboard
A lightweight web dashboard served via device's builtin webserver.  

<b>Dashboard Features:</b>
- [ ] Device Resources Monitor
- [ ] A Terminal Connected to ZEOS Shell over HTTP
- [ ] System Configurations Portal
- [ ] Simple File Explorer
