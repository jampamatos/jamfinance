# Jamfinance

## Project Overview
Jamfinance is a microservices-based day trading application designed to automate stock trading decisions. It integrates real-time and historical data collection, advanced trading algorithms, and direct brokerage execution.

## Project Structure
- `data-collection/`: Microservice for collecting real-time and historical financial data.
- `data-processing/`: Microservice for processing collected data and calculating financial indicators.
- More directories will be added as the project develops.

## Environment Setup
- Install WSL 2 and Docker on Windows.
- Setup Python environment and Node.js for React development.
- Detailed setup instructions can be found in the `setup` directory.

## Building and Running
### Data Collection Service
To build and run the data collection service:
```bash
cd data-collection/docker
docker build -t data-collection-service .
docker run -p 5000:5000 --name dc-container data-collection-service
```

Access the service at `http://localhost:5000/` to see a welcome message.

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