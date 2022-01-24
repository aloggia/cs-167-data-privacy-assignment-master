Individual people each have a lot of personal data, such as names, addresses, ages, salaries, etc, and all that data
would be incredibly useful for research/data purposes. For example the govt might want to see what the average salaries
are in different geographic locations, so they know where to spend money to help people. However, people are usually
hesitant to give up private data, and putting all that data onto a server or spreadsheet means it's vulnerable to hackers
or other malicious actors. The solution is to add randomly generated noise to each individual piece of data that we are
tracking. By using a mathematical distribution function such as the normal/gaussian distribution or the laplace distribution
we can add random noise to the data to obscure the true value of the data.
While adding random noise to pieces of data makes each individual piece of data inaccurate, we can still get accurate
results by looking at the aggregate dataset. Like in the example above, the govt would collect salary info on people
in a specific location, then add random noise to that data. Now if an attacker steals the data, they would have all the
salary info, but because it's noisy they can't connect a specific salary to a specific person. By adding a controlled
amount of noise to the dataset we can add just enough to hide peoples personal info while still allowing us to draw
accurate conclusions from the dataset as a whole.