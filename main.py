import json
import math
import sys
import csv


def calculate_distance(point1, point2):
    """Calculate Euclidean distance between two points."""
    x1, y1 = point1
    x2, y2 = point2

    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def get_warehouse_location(warehouses, warehouse_id):
    """Get warehouse location from either supported input format."""

    # Supports list format used by base_case.json
    if isinstance(warehouses, list):
        for warehouse in warehouses:
            if warehouse["id"] == warehouse_id:
                return warehouse["location"]

    # Supports dictionary format used by test cases
    return warehouses[warehouse_id]


def get_agents(agents):
    """Return agents as (agent_id, location) pairs."""

    # Supports list format
    if isinstance(agents, list):
        return [
            (agent["id"], agent["location"])
            for agent in agents
        ]

    # Supports dictionary format
    return list(agents.items())


def get_package_warehouse_id(package):
    """Support both warehouse key formats."""

    if "warehouse_id" in package:
        return package["warehouse_id"]

    return package["warehouse"]


def find_nearest_agent(package, agents, warehouses):
    """Find the nearest agent to the package warehouse."""

    warehouse_id = get_package_warehouse_id(package)

    warehouse_location = get_warehouse_location(
        warehouses,
        warehouse_id
    )

    nearest_agent = None
    shortest_distance = float("inf")

    for agent_id, agent_location in get_agents(agents):

        distance = calculate_distance(
            agent_location,
            warehouse_location
        )

        # If there is a tie, select the first agent in input order.
        if distance < shortest_distance:
            shortest_distance = distance
            nearest_agent = agent_id

    return nearest_agent


def load_data(filename):
    """Read and parse the JSON input file."""

    with open(filename, "r") as file:
        return json.load(file)


def generate_report(data):
    """Assign packages and generate the delivery report."""

    agents = data["agents"]
    warehouses = data["warehouses"]
    packages = data["packages"]

    report = {}

    # Initialize report for all agents.
    for agent_id, agent_location in get_agents(agents):
        report[agent_id] = {
            "packages_delivered": 0,
            "total_distance": 0.0
        }

    agent_locations = dict(get_agents(agents))

    # Process every package.
    for package in packages:

        # Assign package to the nearest agent.
        agent_id = find_nearest_agent(
            package,
            agents,
            warehouses
        )

        warehouse_id = get_package_warehouse_id(package)

        warehouse_location = get_warehouse_location(
            warehouses,
            warehouse_id
        )

        agent_location = agent_locations[agent_id]
        destination = package["destination"]

        # Calculate Agent -> Warehouse distance.
        distance_to_warehouse = calculate_distance(
            agent_location,
            warehouse_location
        )

        # Calculate Warehouse -> Destination distance.
        distance_to_destination = calculate_distance(
            warehouse_location,
            destination
        )

        # Total route:
        # Agent -> Warehouse -> Destination
        total_distance = (
            distance_to_warehouse
            + distance_to_destination
        )

        report[agent_id]["packages_delivered"] += 1
        report[agent_id]["total_distance"] += total_distance

    # Calculate efficiency for every agent.
    for agent_id in report:

        packages_delivered = report[agent_id]["packages_delivered"]
        total_distance = report[agent_id]["total_distance"]

        if packages_delivered > 0:
            efficiency = (
                total_distance / packages_delivered
            )
        else:
            efficiency = 0.0

        report[agent_id]["total_distance"] = round(
            total_distance,
            2
        )

        report[agent_id]["efficiency"] = round(
            efficiency,
            2
        )

    # Consider only agents who delivered at least one package.
    agents_with_packages = {
        agent_id: details
        for agent_id, details in report.items()
        if details["packages_delivered"] > 0
    }

    if agents_with_packages:
        # Lower average delivery distance means better efficiency.
        best_agent = min(
            agents_with_packages,
            key=lambda agent_id:
                agents_with_packages[agent_id]["efficiency"]
        )
    else:
        best_agent = None

    report["best_agent"] = best_agent

    return report


def save_report(report, filename="report.json"):
    """Save the generated report to a JSON file."""

    with open(filename, "w") as file:
        json.dump(report, file, indent=4)


def save_top_performer_csv(report, filename="top_performer.csv"):
    """Export the best-performing agent to a CSV file."""

    best_agent = report["best_agent"]

    if best_agent is None:
        return

    details = report[best_agent]

    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)

        writer.writerow([
            "agent_id",
            "packages_delivered",
            "total_distance",
            "efficiency"
        ])

        writer.writerow([
            best_agent,
            details["packages_delivered"],
            details["total_distance"],
            details["efficiency"]
        ])


def main():

    # Use the filename provided in the command.
    # If no filename is provided, use base_case.json.
    if len(sys.argv) > 1:
        input_file = sys.argv[1]
    else:
        input_file = "base_case.json"

    data = load_data(input_file)

    report = generate_report(data)

    save_report(report)

    # Bonus feature: export the top performer to CSV.
    save_top_performer_csv(report)

    print("Delivery simulation completed successfully.")
    print()

    for agent_id, details in report.items():

        if agent_id != "best_agent":
            print(
                f"{agent_id}: "
                f"{details['packages_delivered']} packages, "
                f"{details['total_distance']} distance, "
                f"efficiency = {details['efficiency']}"
            )

    print()
    print("Best Agent:", report["best_agent"])
    print("Report saved to report.json")
    print("Top performer exported to top_performer.csv")


if __name__ == "__main__":
    main()