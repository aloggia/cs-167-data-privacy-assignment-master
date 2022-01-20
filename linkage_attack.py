"""
DATA PRIVACY EXAMPLE
Linkage Attack

This script reads in two data sets (csv files) and looks for links.
Toggle the PRIVATIZED boolean to True to use the private_salaries.csv
data to test the algorithm you created in the differential_privacy.py script.
The goal is to have zero links found AND the difference in the average ages
between the original data and the privatized data be less than 1.0 (for both
Burlington and South Burlington). Modify your algorithm until it is.
"""

import csv
import sys

# Set to True to use privatized age data (i.e. noise added to anonymize data)
PRIVATIZED = False

# Define data sources
NAME_DATA = 'names.csv'
SALARY_DATA = 'salaries.csv'
PRIVATE_SALARY_DATA = 'private_salaries.csv'


def main():
    """
    Control program flow. Read data, calculate average age,
    determine data links, compare original age averages with
    privatized age averages (if PRIVATIZED = True).

    :return: None
    """
    average_ages = dict()
    names = read_data(NAME_DATA)
    if PRIVATIZED:
        private_salaries = read_data(PRIVATE_SALARY_DATA)
        data_linkage(names, private_salaries)
        private_averages = calculate_averages(private_salaries)
        average_ages["burlington_with_noise"] = private_averages[0]
        average_ages["south_burlington_with_noise"] = private_averages[1]

        salaries = read_data(SALARY_DATA)
        averages = calculate_averages(salaries)
        average_ages["burlington_no_noise"] = averages[0]
        average_ages["south_burlington_no_noise"] = averages[1]
        display_results(average_ages)

    else:
        salaries = read_data(SALARY_DATA)
        data_linkage(names, salaries)
        averages = calculate_averages(salaries)
        average_ages["burlington_no_noise"] = averages[0]
        average_ages["south_burlington_no_noise"] = averages[1]
        display_results(average_ages)


def read_data(read_file):
    """
    Read csv file and return data in list
    :param read_file: csv data source
    :return: list
    """
    data_list = []
    try:
        with open(read_file, 'rt') as f:
            data = csv.reader(f)
            headers = True
            for row in data:
                if headers:
                    headers = False
                else:
                    data_list.append(row)
        return data_list
    except IOError:
        print("\nError opening file.")
        sys.exit()


def data_linkage(names, salaries):
    """
    Attempt Linkage Attack
    Compare data from names and salaries lists to identify links

    :param names: list
    :param salaries: list
    :return: None
    """
    print("\nAttempting Linkage Attack".upper())
    print("Comparing data...")
    print("\nLinkage Results:")
    name_salary_links = []
    for name_row in names:
        for salary_row in salaries:
            name = name_row[0]
            salary = salary_row[0]
            name_age = name_row[1]
            salary_age = salary_row[1]
            name_city = name_row[2]
            salary_city = salary_row[2]
            if name_age == salary_age and name_city == salary_city:
                duplicate = False
                for link in name_salary_links:
                    if name == link[0]:
                        link[1].append(salary)
                        duplicate = True
                if not duplicate:
                    name_salary_links.append([name, [salary]])

    for link in name_salary_links:
        if len(link[1]) > 1:
            print(" " + str(link[0]) + "'s salary is one of the following: ")
            for val in link[1]:
                print("$".rjust(5) + val + "k", end="")
        else:
            print(" " + str(link[0]) + "'s salary is: $" + link[1][0] + "k", end="")
        print()
    print("\n **** " + str(len(name_salary_links)) + " Links Found. ****\n")


def calculate_averages(salaries):
    """
    Calculate average age of Burlington and South Burlington residents
    Return average ages by town

    :param salaries: list
    :return: tuple
    """

    burlington_age = 0
    burlington_age_count = 0
    south_burlington_age = 0
    south_burlington_age_count = 0
    for salary_row in salaries:
        if salary_row[2] == "burlington":
            burlington_age += float(salary_row[1])
            burlington_age_count += 1
        else:
            south_burlington_age += float(salary_row[1])
            south_burlington_age_count += 1

    burlington_age_average = burlington_age / burlington_age_count
    south_burlington_age_average = south_burlington_age / south_burlington_age_count

    return burlington_age_average, south_burlington_age_average


def display_results(avg_age):
    """
    Display average ages by town, both before and after the data was privatized
    Display average age difference between original and privatized age averages (if
    PRIVATIZED = True)

    :param avg_age: dict
    :return: None
    """

    burlington_avg_age = avg_age.get("burlington_no_noise")
    south_burlington_avg_age = avg_age.get("south_burlington_no_noise")
    print("\nAverage Age".upper())
    print("--------------------------------------------------")
    print("Average age in Burlington:", format(burlington_avg_age, ".3f"))
    print("Average age in South Burlington:", format(south_burlington_avg_age, ".3f"), "\n")

    if PRIVATIZED:
        privatized_burlington_avg_age = avg_age.get("burlington_with_noise")
        privatized_south_burlington_avg_age = avg_age.get("south_burlington_with_noise")
        print("Privatized average age in Burlington:", format(privatized_burlington_avg_age, ".3f"))
        print("Privatized average age in South Burlington:", format(privatized_south_burlington_avg_age, ".3f"), "\n")

        burlington_avg_age_difference = abs(burlington_avg_age - privatized_burlington_avg_age)
        south_burlington_avg_age_difference = abs(south_burlington_avg_age - privatized_south_burlington_avg_age)
        print("Burlington Average Age Difference:", format(burlington_avg_age_difference, ".6f"))
        print("South Burlington Average Age Difference:", format(south_burlington_avg_age_difference, ".6f"))

        if burlington_avg_age_difference > 1 or south_burlington_avg_age_difference > 1:
            print("\n **** Averages changed. Too much noise. ****")


if __name__ == '__main__':
    main()
