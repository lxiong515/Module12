"""
Program: Class.py
Author:  Luke Xiong
Date: 7/12/2020

This file will create attributes for all the columns in the CSV.
"""

class NewClass:

    def __init__(self, rank,county,per_capita_income,median_household_income,median_family_income,
        population,number_of_households):
        self.rank = rank
        self.county = county
        self.per_capita_income=per_capita_income
        self.median_household_income=median_household_income
        self.median_family_income=median_family_income
        self.population=population
        self.number_of_households=number_of_households

    def display(self):
        return 'Rank: ' + str(self.rank) + ' County: ' + str(self.county) + ' Per Capita: ' + str(self.per_capita_income) + ' Median Household Income: $' + str(self.median_household_income) + ' Median Family Income: $' + str(self.median_family_income) + ' Population: ' + str(self.population) + ' Number of Households: ' + str(self.number_of_households)

    def __str__(self):
        return 'Rank: ' + str(self.rank) + ' County: ' + str(self.county) + ' Per Capita: ' + str(self.per_capita_income) + ' Median Household Income: $' + str(self.median_household_income) + ' Median Family Income: $' + str(self.median_family_income) + ' Population: ' + str(self.population) + ' Number of Households: ' + str(self.number_of_households)

    def __repr__(self):
        return (f'{self.__class__.__name__}('f'{self.rank!r}, {self.county!r}, {self.per_capita_income!r}, {self.median_household_income!r}, {self.median_family_income!r},{self.population!r},{self.number_of_households!r})')
