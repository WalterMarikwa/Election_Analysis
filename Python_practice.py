# counties = ["Arapahoe","Denver","Jefferson"]
# if "Arapahoe" in counties and "El Paso" in counties:
#     print("Arapahoe and El Paso are in the list of counties.")
# else:
#     print("Arapahoe or El Paso is not in the list of counties.")

# for county in counties:
#     print(county)


# numbers = [0, 1, 2, 3, 4]
# for num in numbers:
#     print(num)

# print('-----------------------')

# for num in range(5):
#     print(num)

# print('-----------------------')


# for i in range(len(counties)):
#     print(counties[i])


counties_dict = {
    "Arapahoe": 422829,
    "Denver": 463353, 
    "Jefferson": 432438
}

# for county in counties_dict.items():
#     print(county)

voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

for county_dict in voting_data:
    print(county_dict)


























































































































































