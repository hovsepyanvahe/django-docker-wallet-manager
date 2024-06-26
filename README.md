# Wallet Manager

This is a Django project for managing wallets and transactions.

## Running with Docker Compose

To run the project using Docker Compose, follow these steps:

1. Make sure you have Docker and Docker Compose installed on your system.
2. Clone the project repository to your local machine.
3. Navigate to the project directory containing the `docker-compose.yml` file.
4. Run the following command to start the Docker containers:

    ```
    docker-compose up --build
    ```

This will build the Docker images and start the containers for the project.

5. Once the containers are running, you can access the Django application in your web browser
   at `http://localhost:8000`.

6. To stop the Docker containers, press `Ctrl + C` in the terminal where Docker Compose is running, and then run the
   following command to remove the containers:

    ```
    docker-compose down
    ```

## Running Tests

To run tests for the project, follow these steps:

1. Make sure you have Python and pip installed on your system.
2. Install the required Python packages using pip:

    ```
    pip install -r requirements.txt
    ```

3. Navigate to the project directory containing the `manage.py` file.
4. Run the tests using the following command:

    ```
    python manage.py test
    ```

This will execute all the tests in the project and display the results.