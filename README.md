# Jamfinance

## Project Overview
Jamfinance is a microservices-based day trading application designed to automate stock trading decisions. It integrates real-time and historical data collection, advanced trading algorithms, and direct brokerage execution.

## Project Structure
- `data-collection/`: Microservice for collecting real-time and historical financial data.
  - `src/`: Contains the source code for the data collection service.
    - `scripts/`: Contains scripts for real-time and historical data collection. Scripts include advanced error handling, data validation, and use environment variables for API keys.
    - `tests/`: Includes tests for validating the functionality and robustness of the data collection scripts and the API endpoints.
  - `app.py`: Flask application that provides API endpoints for accessing real-time and historical data.
- More directories will be added as the project develops.

## Environment Setup
- Install WSL 2 and Docker on Windows.
- Setup Python environment and Node.js for React development.
- Ensure all Python packages are installed. You can run `pip install -r requirements.txt` for each microservices to ensure.
- Detailed setup instructions can be found in the `setup` directory.

## Building and Running
Before building and running the data collection service, ensure that the `ALPHA_VANTAGE_API_KEY` environment variable is set with your API key. Please refer to our [configure API key guide](docs/API_KEYS_CONFIG.md) for more information.

### Data Collection Service
To build and run the data collection service:
```bash
cd data-collection/docker
docker build -t data-collection-service .
docker run -p 5000:5000 --name dc-container data-collection-service
```

Access the service at `http://localhost:5000/` to see a welcome message.

## API Endpoints
### Data Collection Service Endpoints
The data collection service provides RESTful API endpoints to access real-time and historical financial data for specified stock symbols. Below are the available endpoints with their expected responses and functionalities:

#### Real-time Data Endpoint
- **Endpoint**: `/api/realtime/<sym>`
- **Method**: GET
- **Description**: Returns real-time financial data for a specified stock symbol.
- **Parameters**:
  - `sym` (string): Stock symbol for which real-time data is requested.
- **Response Format**: JSON
- **Example Request**:
  ```bash
  curl http://localhost:5000/api/realtime/AAPL
  ```
- **Example Response:**
  ```json
    {
    "Time Series (5min)": {
      "2024-07-24 16:00:00": {
        "1. open": "150.10",
        "2. high": "150.12",
        "3. low": "149.90",
        "4. close": "150.00",
        "5. volume": "10457"
      }
    }
  }
  ```

#### Historical Data Endpoint
- **Endpoint:** `/api/historical/<sym>`
- **Method:** GET
- **Description:** Returns historical financial data for a specified stock symbol, formatted in JSON.
- **Parameters:**
  - `sym` (string): Stock symbol for which historical data is requested.
- **Response Format:** JSON
- **Example Request:**
  ```bash
  curl http://localhost:5000/api/historical/AAPL
  ```
- **Example Response:**
  ```json
  {
    "columns": ["Date", "Open", "High", "Low", "Close", "Volume"],
    "index": ["2024-07-23", "2024-07-22", "2024-07-21"],
    "data": [
      ["2024-07-23", 150.10, 155.20, 149.00, 154.90, 14000],
      ["2024-07-22", 148.50, 150.00, 147.00, 149.50, 10000],
      ["2024-07-21", 145.00, 150.00, 145.00, 148.00, 12000]
    ]
  }
  ```
### Error Handling
A global error handler is implemented to manage exceptions and return appropriate error messages along with HTTP status codes. This ensures that any issues with API requests are communicated clearly to the user.

#### Common HTTP Status Codes

- **200 OK:** The request has succeeded and the response body contains the requested data.
- **400 Bad Request:** The request could not be understood by the server due to malformed syntax or invalid parameters.
- **500 Internal Server Error:** The server encountered an unexpected condition which prevented it from fulfilling the request.

This detailed documentation of the API endpoints and error handling will help developers and users interact with the API more effectively, understanding what to expect in each scenario.

## Testing
Testing is an integral part of ensuring the reliability of the Jamfinance services. Here's how you can run the tests:

### Data Collection Service
- Navigate to the `data-collection/src/tests/` directory.
- Run `pytest` to execute the test suite and verify the data collection functionalities including robust error handling and input validation.

We have implemented tests to cover:
- Real-time and historical data fetching functionalities from Alpha Vantage and yfinance.
- Input validation for stock symbols, ensuring they are valid and correctly formatted.
- Comprehensive error handling for API responses and data processing, including checks for API connectivity and data integrity.

## Developing Diary
### 07/24/2024: Code Refactoring and Testing Enhancements
- **Refactoring**: The data collection scripts have been refactored to improve modularity and error handling.
- **Testing**: New tests have been added to cover the improvements in error handling and data validation.

## Future Plans
We are constantly working to improve Jamfinance and plan to add the following features:
- Enhanced data analysis tools within the `data-processing` microservice.
- A fully functional user interface for monitoring and managing trades.
- Integration with additional financial APIs for broader market coverage.

Stay tuned to our [GitHub issues](https://github.com/jampamatos/jamfinance/issues) for upcoming features and how you can contribute to each milestone.

## Support
For support, please open an issue on our GitHub repository or contact me directly at [jp.coutm@gmail.com](mailto:jp.coutm@gmail.com).

## Contributions
Contributions are welcome! Please read the [contribuition guide](docs/CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests.

## License
This project is licensed under the MIT License - [click here](LICENSE.md) for details.