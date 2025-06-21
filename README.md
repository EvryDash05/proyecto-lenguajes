# Set up a local project environment
How to set up your local machine.

## Prerequisites
* Python > 3.11

## Backend (Python)

- **Create a Virtual Environment** 

    ```bash
    ** Windows ** 
    python -m venv venv
    .\venv\Scripts\activate
    ```

    ```bash
    ** MacOs ** 
    python -m venv venv
    .\venv\bin\activate
    ```

- **Install Dependencies**  
    ```bash
    pip install -r requirements.txt
    ```

- **Run the app**
    - **Windows**
    ```bash
    .\local_server.bat
    ```

    - **Unix-based**
    ```bash
    ./local_server.sh
    ```