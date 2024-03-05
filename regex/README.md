# Flask Application with Regular Expressions for Data Processing

## Introduction

In today's data-driven world, the ability to extract meaningful insights from unstructured text data is crucial for decision-making processes within organizations.
This Flask application demonstrates the usage of regular expressions (regex) to streamline data processing tasks. 
Regular expressions provide a powerful tool for pattern matching and text processing, enabling efficient data extraction, validation, and transformation.

## Features

- **Input Form**: Users can input regex patterns and textual data through intuitive input fields.
- **Real-time Analysis**: The application performs regex pattern matching on the input data and displays the matched results in real-time.
- **Data Processing Tasks**: Various data processing tasks such as email extraction, URL identification, and date recognition can be performed using regex patterns.

## Usage

1. Start the Flask application:

    ```bash
    python app.py
    ```

2. Access the application in your web browser at `(http://13.234.204.23:5000/)`.

3. Input regex patterns and textual data to perform data processing tasks.

## Deployment

The application can be deployed on various platforms. Below are instructions for deploying on an AWS EC2 instance:

1. **Launch an EC2 instance on AWS**: Configure it with the necessary software environment.
  
2. **Upload Flask Application Files**: Use SCP or SFTP to upload the Flask application files to the EC2 instance.

3. **Install Dependencies**: Install required dependencies such as Flask and other libraries on the EC2 instance.

4. **Start the Flask Application**: Run the Flask application on the EC2 instance:

    ```bash
    python app.py
    ```

5. **Access the Application**: Access the application via the instance's public IP address.

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes.


## Authors

- Deepraj Vadhwane   deeprajvadhwane01@gmail.com


