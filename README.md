# Python Delivery System Assignment

## Overview

This project is a Python-based delivery system simulator.

The system assigns each package to the nearest delivery agent based on the distance between the agent and the package warehouse.

After assigning packages, the system simulates the delivery route and calculates the total delivery distance and efficiency of each agent.

The program also identifies the best-performing agent and exports the top performer to a CSV file.

## Features

- Read and parse JSON input data
- Calculate Euclidean distance
- Assign packages to the nearest agent
- Simulate package delivery
- Calculate total delivery distance
- Calculate agent efficiency
- Identify the best-performing agent
- Generate a JSON report
- Export the top performer to CSV
- Support different input JSON formats
- Handle multiple test cases

## Technologies Used

- Python
- JSON
- CSV
- Math

## How It Works

### Step 1: Read Input Data

The program reads the input data from a JSON file containing:

- Warehouses
- Delivery agents
- Packages
- Package destinations

### Step 2: Find the Nearest Agent

For each package, the distance between every agent and the package's warehouse is calculated.

The package is assigned to the nearest agent.

If two agents have the same distance, the first agent in the input order is selected.

### Step 3: Simulate Delivery

The delivery route is:

```text
Agent → Warehouse → Destination
```

The total distance is calculated by adding:

```text
Agent → Warehouse
+
Warehouse → Destination
```

### Step 4: Generate Report

The program calculates the following information for every agent:

- Number of packages delivered
- Total delivery distance
- Average distance per package
- Best-performing agent

### Step 5: Save Report

The generated report is saved in:

```text
report.json
```

## Distance Calculation

Euclidean distance is calculated using:

```text
distance = √((x2 - x1)² + (y2 - y1)²)
```

The program uses this formula to calculate the distance between two points.

## Efficiency

Efficiency is calculated as:

```text
Efficiency = Total Distance / Packages Delivered
```

A lower average delivery distance represents higher efficiency.

Agents with zero delivered packages have an efficiency value of `0.0`.

## Assumptions

- The solution follows the input data and Euclidean distance calculation provided in the assignment.
- Each package is assigned independently to the nearest agent.
- If multiple agents have the same distance, the first agent in the input order is selected.
- All packages are assumed to be successfully delivered.
- Only agents who delivered at least one package are considered when selecting the best agent.
- The delivery route is assumed to be Agent → Warehouse → Destination.

## Bonus Feature

The optional top performer export feature is implemented.

After the delivery report is generated, the best-performing agent is exported to:

```text
top_performer.csv
```

The CSV file contains:

- Agent ID
- Packages delivered
- Total distance
- Efficiency

This provides an additional way to view the top-performing agent's results.

## How to Run

Make sure Python is installed on the system.

Open the project folder in the terminal and run:

```bash
python main.py
```

The program uses `base_case.json` by default.

After execution, the following files are generated:

```text
report.json
top_performer.csv
```

## Running Test Cases

The program also supports running individual test case files.

For example:

```bash
python main.py test_case_1.json
```

Other test cases can be run using:

```bash
python main.py test_case_2.json
```

```bash
python main.py test_case_3.json
```

The same command structure can be used for all provided test cases.

## Project Structure

```text
Nexgensis_Python_Assignment
│
├── main.py
├── base_case.json
├── report.json
├── README.md
└── test_cases
    ├── test_case_1.json
    ├── test_case_2.json
    ├── test_case_3.json
    ├── test_case_4.json
    ├── test_case_5.json
    ├── test_case_6.json
    ├── test_case_7.json
    ├── test_case_8.json
    ├── test_case_9.json
    └── test_case_10.json
```

## Testing

The solution was tested using the provided test cases to verify:

- JSON input handling
- Package assignment
- Nearest-agent calculation
- Distance calculation
- Delivery route calculation
- Agent efficiency
- Best-agent selection
- Report generation
- Different JSON input formats
- Top performer CSV generation

## Output

For the base case, the program generates a report containing the performance of each delivery agent.

Example output format:

```text
Delivery simulation completed successfully.

A1: 2 packages, 78.28 distance, efficiency = 39.14
A2: 2 packages, 72.24 distance, efficiency = 36.12
A3: 1 packages, 14.14 distance, efficiency = 14.14

Best Agent: A3
Report saved to report.json
Top performer exported to top_performer.csv
```

## Conclusion

This project demonstrates a simple delivery simulation using Python, JSON data processing, Euclidean distance calculation, package assignment, delivery simulation, report generation, and CSV export.
