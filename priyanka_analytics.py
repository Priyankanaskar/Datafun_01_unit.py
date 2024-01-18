import math
import statistics

#Define Variables of Different Types
#Define at least one variable of each of these types: str, int, float, bool, list of strings, list of number


company_name: str = "Stellar Analytics Inc."
count_active_projects: int = 5
has_international_presence: bool = False
average_client_satisfaction: float = 4.7
services_offered: list = ["Data Analysis", "Machine Learning Consulting", "Business Intelligence Solutions"]
satisfaction_scores: list = [4.8, 4.6, 4.9, 5.0, 4.7]

#Define Formatted Strings

active_projects_string: str = f"Active Projects: {count_active_projects}"
international_presence_string: str = f"International Presence: {has_international_presence}"
client_satisfaction_string: str = f"Average Client Satisfaction: {average_client_satisfaction}"

#Calculate Descriptive Statistics

import statistics

smallest= min(satisfaction_scores)
largest= max(satisfaction_scores)
total= sum(satisfaction_scores)
count= len(satisfaction_scores)
mean= statistics.mean(satisfaction_scores)
mode= statistics.mode(satisfaction_scores)
median= statistics.median(satisfaction_scores)
standard_deviation=statistics.stdev(satisfaction_scores)

stats_string: str = f"""
Descriptive Statistics for Our Satisfaction Scores:
  Smallest: {smallest}
  Largest: {largest}
  Total: {total}
  Count: {count}
  Mean: {mean}
  Mode: {mode}
  Median: {median}
  Standard Deviation: {standard_deviation}
"""

# Define Byline String

byline: str = f"""
{company_name}
{active_projects_string}
{international_presence_string}
{client_satisfaction_string}
{services_offered_string}
{stats_string}
"""
#Define Main Function
    def main():
    ''' Display all output'''
    print(company_name)
    print(active_projects_string)
    print(international_presence_string)
    print(client_satisfaction_string)
    print(services_offered_string)
    print(numbers_string)
    print(stats_string)

    # If all of the above works, then the byline should work too:
    print(byline)

# Conditional Script Execution
if __name__ == '__main__':
    main()

Stellar Analytics Inc
Rate Per Hour: $62.99
Skills Include: Quick-learner, Problem-Solver, Enthusiastic, and Open-Minded
Has Masters Degree: False
Years in the Field: 3
Average Rating: 7.91
Max Rating: 8.7
