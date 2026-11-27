# Physics Unit Converter

A beginner-friendly, terminal-based Python program for converting common units of length, time, velocity, and force. It accepts decimal values, checks menu choices, and lets you perform multiple conversions before quitting.

## Features

- **Length:** cm ↔ m and km ↔ m
- **Time:** seconds to hours or minutes; minutes to seconds or hours; days to minutes
- **Velocity:** m/s ↔ cm/s and km/h ↔ m/s
- **Force:** newtons ↔ kg·m/s² and newtons ↔ dynes
- Decimal number input and helpful handling of invalid menu entries

## Requirements

- Python 3
- No third-party package

## Run

Save `main.py` and run it from a terminal:

```bash
python main.py
```

If your system uses `python3` as the command, run `python3 main.py` instead.

## Example

Choose **Length**, then **Centimeter to Meter**, and enter `250`:

```text
250 Centimeter = 2.5 Meter
```

## Conversion notes

- `1 N = 1 kg·m/s²`
- `1 N = 100,000 dynes`
- The program accepts signed values as well as decimals; it does not enforce whether a value is physically meaningful for a particular situation.

## Project status

This is an early learning project. It currently focuses on unit conversions; physics formula calculations are not included yet.

## Possible next steps

- Add more unit categories and formula calculations.
- Add automated checks for conversion results.
- Improve the display of units and conversion precision.
