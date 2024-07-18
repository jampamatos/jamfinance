# API Keys Configuration Guide

This document provides step-by-step instructions on how to securely configure API keys for the Jamfinance application using environment variables. This method ensures that API keys are not hard-coded in the source code and are not exposed publicly.

## Setting Up Environment Variables

To ensure the security of API keys, this project uses environment variables. Follow the steps below to set up your API keys locally:

### For Linux/Mac Users:

1. Open your terminal.
2. Run the following commands, replacing `your_alpha_vantage_key_here` and `your_yfinance_key_here` with your actual API keys:

```bash
echo 'export ALPHA_VANTAGE_API_KEY="your_alpha_vantage_key_here"' >> ~/.bashrc
source ~/.bashrc
```

### For Windows Users:

1. Open Command Prompt.
2. Execute the following commands:

```cmd
setx ALPHA_VANTAGE_API_KEY "your_alpha_vantage_key_here"
```

## Verifying the Configuration
To verify that the environment variables are set correctly, you can run the following command in your terminal or Command Prompt:

```bash
echo $ALPHA_VANTAGE_API_KEY
```

If everything is set up correctly, this command should print your API key.

## Important Notes

- **Security:** Never share your API keys publicly or in your codebase. Always use environment variables to manage sensitive information securely.
- **.gitignore:** Ensure that any local configuration files that might store API keys temporarily are included in your `.gitignore` file to prevent them from being committed to your version control system.

## Troubleshooting

If you encounter any issues while setting up your API keys, please check the following:

- Ensure that you have correctly replaced `your_alpha_vantage_key_here` with your actual API key.
- Make sure to restart your terminal or Command Prompt after setting the environment variables.
- Verify that there are no typos in your environment variable names or values.

For further assistance, contact support or refer to the FAQ section of this documentation.