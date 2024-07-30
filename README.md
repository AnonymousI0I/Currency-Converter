# Currency Converter

This Python script converts a given amount in USD to another currency (GBP, EUR, or CNY). The script prompts users for the amount in USD and the target currency, then displays the converted amount.

## Features

- **Convert USD to GBP**: Convert a given amount in USD to British Pounds (GBP).
- **Convert USD to EUR**: Convert a given amount in USD to Euros (EUR).
- **Convert USD to CNY**: Convert a given amount in USD to Chinese Yuan (CNY).

## Requirements

- Python 3.x

## Usage

1. **Clone the repository**:

    ```bash
    git clone https://github.com/AnonymousI0I/Currency-Converter.git
    cd currency-converter
    ```

2. **Run the script**:

    ```bash
    python Currency Converter.py
    ```

3. **Follow the on-screen prompts**:

### Input USD Amount

- You will be prompted to enter the amount in USD you wish to convert.
- The amount must be a positive number.

    Example:

    ```
    Enter the dollar amount you wish to convert: 100
    ```

### Select Target Currency

- You will be prompted to enter the desired target currency (GBP, EUR, or CNY).
- Enter one of the valid currency codes (GBP, EUR, CNY).

    Example:

    ```
    Enter the desired currency (GBP for Pounds, EUR for Euro, or CNY for Yuan): GBP
    ```

### Output

- The script will display the converted amount in the selected currency.

    Example:

    ```
    $100 in GBP is 77.0.
    ```

## Code Overview

### Function Descriptions

#### `get_usd()`

Prompts the user to enter the amount in USD they wish to convert. Ensures the input is a positive number.

- **Returns**:
  - `float`: The amount in USD.

#### `get_currency()`

Prompts the user to enter the desired currency (GBP, EUR, or CNY). Ensures the input is one of the valid currency codes.

- **Returns**:
  - `str`: The currency code.

#### `usd_to_gbp(usd)`

Converts the given amount in USD to British Pounds (GBP).

- **Parameters**:
  - `usd` (float): The amount in USD.
- **Returns**:
  - `float`: The amount in GBP.

#### `usd_to_eur(usd)`

Converts the given amount in USD to Euros (EUR).

- **Parameters**:
  - `usd` (float): The amount in USD.
- **Returns**:
  - `float`: The amount in EUR.

#### `usd_to_cny(usd)`

Converts the given amount in USD to Chinese Yuan (CNY).

- **Parameters**:
  - `usd` (float): The amount in USD.
- **Returns**:
  - `float`: The amount in CNY.

### Main Function

The `main()` function orchestrates the workflow by prompting the user for inputs, calling the respective functions to perform the conversion, and displaying the results.

## Contribution

Contributions are welcome! Please fork the repository, create a new branch, and submit a pull request.


