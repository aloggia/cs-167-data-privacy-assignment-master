"""
OVERVIEW:
You want to release a set of data containing salaries, ages and a location of either Burlington or South Burlington.
This data will be useful to see the average salaries of people in Burlington vs South Burlington, as well as compare
salaries to age. You have removed the names from the data set to protect the subjects privacy, and put it in a
file called salaries.csv to be posted on your website.

However there is another data set available online released by someone else, which has names, ages, and cities
(names.csv). Given these two data sets, could someone figure out what Mary's salary is? What about John?

Even though you are not releasing names, someone could still look at both data sets and figure out the salaries of
people in the data, by comparing their age and location. This is called a Linkage Attack.

TODO: Complete the function "anonymize_age_data()" below so that it modifies the Age data to be written to a new file
called private_salaries.csv, which is a copy of salaries.csv (same fields), but with some "noise", or randomization
in the Age column, so that you can no longer compare someones age and location to determine their salary.

However in privatizing the age data, make sure that the average age in both towns is mostly unchanged, so the data is
still accurate when comparing average salaries and ages between Burlington and South Burlington. For this exercise, the
difference in average age between the original data and privatized data must be less than 1.00. In other words, adding
too much noise will alter the data, but just enough noise will leave the published data statistically useful without
compromising the resident's privacy (i.e. salary).

Write your algorithm in the "anonymize_age_data()" function below, then run this file to write the privatized data to
the csv file. Then, run the linkage_attack.py file again to verify that 1) no links were found AND 2) the difference
in the original age average and the privatized age average for BOTH Burlington and South Burlington is less than 1.00.

NOTE: this data is random and not representative of any real people, ages or salaries.
"""

import csv
import sys
import numpy as np


def main():
    """
    Control program flow: 1) Read original data, 2) anonymize age data,
    3) write updated data to private_salaries.csv
    """
    original_salaries = read_data()
    privatized_data = anonymize_age_data(original_salaries)
    write_privatized_data(privatized_data)


def read_data():
    """
    Read salaries.csv into list and return
    :return: list
    """
    salaries = []
    try:
        with open('salaries.csv', 'rt') as f:
            data = csv.reader(f)
            for row in data:
                salaries.append(row)
        return salaries
    except IOError:
        print("\nError opening file.")
        sys.exit()


def anonymize_age_data(salaries):
    """
    TODO: Design an algorithm to add noise to Age data. Keep in
    mind too much noise will affect the age statistics (e.g. average) of each town.
    Return a list containing the salaries data with updated ages in Age column,
    with all of the same fields (Salary,Age,Town).

    :param salaries: list
    :return: list
    """

    # **** START student work **** #
    def extract(ages):
        ages = ages[1:]
        return [int(item[1]) for item in ages]

    def laplace_mech_vec(data, sensitivity, epsilon):
        return data + np.random.laplace(loc=0, scale=sensitivity/epsilon)

    def insert(salaries, priv_ages):
        j = 0
        for i in salaries[1:]:
            i[1] = priv_ages[j]
            j += 1
        return salaries



    # Your algorithm here.
    ages = extract(salaries)
    priv_ages = []
    for age in ages:
        priv_ages.append(laplace_mech_vec(age, 1, .05))
    salaries = insert(salaries, priv_ages)


    # Return data with updated ages
    return salaries
    # **** END student work **** #


def write_privatized_data(salaries):
    """
    Write updated data to private_salaries.csv
    :param salaries: list
    """
    with open('private_salaries.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        for row in salaries:
            writer.writerow(row)
    print("\n **** Data written successfully. ****")


if __name__ == '__main__':
    main()
