# Jamfinance

## Project Overview
Jamfinance is a microservices-based day trading application designed to automate stock trading decisions. It integrates real-time and historical data collection, advanced trading algorithms, and direct brokerage execution.

## Project Structure
- `data-collection/`: Microservice for collecting real-time and historical financial data.
  - `src/`: Contains the source code for the data collection service.
    - `scripts/`: Contains scripts for real-time and historical data collection. Scripts include advanced error handling, data validation, and use environment variables for API keys.
    - `tests/`: Includes tests for validating the functionality and robustness of the data collection scripts and the API endpoints.
  - `app.py`: Flask application that provides API endpoints for accessing real-time and historical data.
- `trading-decision/`: Microservice for making trading decisions.
  - `src/`:
    - `scripts/`: Contains the trading logic implementing various trading algorithms including moving averages and RSI.
    - `tests/`: Includes tests to ensure the accuracy and reliability of the trading algorithms.
  - `app.py`: Flask application that provides an API endpoint for processing trading decisions based on the input data.

## Environment Setup
- Install WSL 2 and Docker on Windows.
- Setup Python environment and Node.js for React development.
- Ensure all Python packages are installed. You can run `pip install -r requirements.txt` for each microservices to ensure.
- Detailed setup instructions can be found in the `setup` directory.

## Building and Running
Each service can be built and run using Docker. Ensure environment variables such as `ALPHA_VANTAGE_API_KEY` are set before running the services.

### Data Collection Service
```bash
cd data-collection/docker
docker build -t data-collection-service .
docker run -p 5000:5000 --name dc-container data-collection-service
```

Access the service at `http://localhost:5000/` to see a welcome message.

### Trading Decision Service

```bash
cd trading-decision/docker
docker build -t trading-decision-service .
docker run -p 5001:5001 --name td-container trading-decision-service
```

## API Endpoints
### Data Collection Service Endpoints

- **Real-time Data Endpoint:** `/api/realtime/<sym>`
- **Historical Data Endpoint:** `/api/historical/<sym>`

### Trading Decision Service Endpoint

- **Trading Decision Endpoint:** `/api/trading_decision`
  - **Method:** `POST`
  - **Description:** Processes input data to determine trading signals.
  - **Input:** JSON format with price data.
  - **Output:** JSON containing trading decisions.

## Error Handling

Both services implement global error handlers to manage exceptions and return appropriate error messages along with HTTP status codes.

## Testing

Navigate to the respective `src/tests/` directories of each service to run automated tests.

## Future Plans

Further enhancements will focus on improving the trading algorithms, integrating with additional data sources, and developing a front-end interface for real-time trading insights.

## Contributions

Contributions are welcome! Please read our [contribution guide](docs/CONTRIBUTING.md) for details on our code of conduct and the process for submitting pull requests.

## License

This project is licensed under the MIT License - [view license](LICENSE.md).