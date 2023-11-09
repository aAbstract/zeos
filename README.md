# ZEOS

## Description
ZEOS is an IoT OS based on Arduino HAL (Hardware Abstraction Layer)

## Features

### 1. Kernel
The kernel is the core component of the OS.  
It manages system resources and provides essential services.  
It Sets up the foundation layer for higher-level software to run.  
<b>Kernel Components: </b>  
- Basic Kernel Data Structures [TODO-0]
- File System (Littlefs Integration) [TODO-0]
- Networking (HTTP MQTT ESP-NOW Integration) [TODO-0]
- Device Drivers (Using Arduino HAL)
- Process Scheduler (RTOS Integration) [TODO-*]

### 2. Shell
The shell is a text based interface that allows users to interact with ZEOS kernel.  
<b>Shell Capabilities: </b>  
- System Bindings (Lua Wrapper for Kernel Components) [TODO-1]
- Scripting (Setting up a Lua REPL) [TODO-1]
- User Management and Access Control [TODO-*]

### 3. Web Dashboard
A lightweight web dashboard served via device's builtin webserver.  
<b>Dashboard Features: </b>
- Device Resources Monitor [TODO-3]
- A Terminal Connected to ZEOS Shell over HTTP [TODO-2]
- System Configurations Portal [TODO-2]
- Simple File Explorer and Text Editor [TODO-4]

### 4. Firmware OTA Update [TODO-*]
