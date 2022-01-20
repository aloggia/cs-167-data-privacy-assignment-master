# Data Privacy Assignment
*CS167 - Cybersecurity Defense*

## Overview
You want to release a set of data containing salaries, ages and a location of either Burlington or South Burlington.
This data will be useful to see the average salaries of people in Burlington vs South Burlington, as well as compare
salaries to age. You have removed the names from the data set to protect the subjects privacy, and put it in a
file called `salaries.csv` to be posted on your website.

However there is another data set available online released by someone else, which has names, ages, and cities, which you'll find in a file called `names.csv`. Given these two data sets, could someone figure out what Mary's salary is? What about John?

Even though you are not releasing names, someone could still look at both data sets and figure out the salaries of
people in the data, by comparing their age and location. This is called a **Linkage Attack**.

## TODO
Complete the function `anonymize_age_data()` in the `differential_privacy.py` file so that it modifies the Age data to be written to a new file
called `private_salaries.csv`, which is a copy of `salaries.csv` (same fields), but with some "noise", or randomization
in the Age column, such that a malicious actor could no longer link someones age and location to determine their salary.

However in privatizing the age data, make sure that the average age in both towns is mostly unchanged, so the data is
still accurate when comparing average salaries and ages between Burlington and South Burlington. For this exercise, the
difference in average age between the original data and privatized data must be less than 1.00. In other words, adding too
much noise will alter the data, but just enough noise will leave the published data statistically useful without
compromising the resident's privacy (i.e. salary).

Write your algorithm in the function `anonymize_age_data()`, then run the `differential_privacy.py` file to write the privatized data to the csv file. Then,
run the `linkage_attack.py` file to verify that:
1. No links were found **AND** 
2. The difference in the original age average and the privatized age average for BOTH Burlington and South Burlington is less than 1.00.

*NOTE: the data provided is random and not representative of any real people, ages or salaries.*

## Running
Requires Python >= 3.7

Place all files in the same directory. Initially run the `linkage_attack.py` script with the `PRIVATIZED` boolean set to `False`. This will display the links found between `salaries.csv` file and the `names.csv` file.
It will also display the average age of both the Burlington and South Burlington residents in the data set. Next, follow the assignment instructions to modify the `differential_privacy.py` file
to include an algorithm that will add noise to the Age data and write it to `private_salaries.csv`. Now, run the `linkage_attack.py` script again (now with the `PRIVATIZED` boolean set to `True` to read in the
`private_salaries.csv` data) to verify that no links were found and the difference in the average ages is within the defined acceptable range (see TODO above).
