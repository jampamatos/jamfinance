# Jamfinance

## Project Overview
Jamfinance is a microservices-based day trading application designed to automate stock trading decisions. It integrates real-time and historical data collection, advanced trading algorithms, and direct brokerage execution.

## Project Structure
- `data-collection/`: Microservice for collecting real-time and historical financial data.
  - `data-collection/src/scripts/`: Contains the scripts for real-time and historical data collection. Scripts include advanced error handling, data validation, and environmental variable management for API keys.
  - `data-collection/src/tests/`: Includes tests for validating the functionality and robustness of the data collection scripts. Tests ensure proper error handling, API response processing, and symbol validation.
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