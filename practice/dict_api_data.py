# Takes a list of API response dictionaries - Returns a summsry with:
#
# total_count
# count_of_passed_responses
# unique_users
# average_response_time
#
# Example_inputs:

responses = [
    {"users" : "name1", "status_code" : 200, "response_time" : 120},
    {"users" : "name2", "status_code" : 500, "response_time" : 300},
    {"users" : "name2", "status_code" : 200, "response_time" : 150}
]
total_count = []
count_of_passed_responses = []
users = []
unique_users = []
average_response_time = []
c=0
for response in responses:
    c+=1
    total_count.append(response["status_code"])
    total_count.append(response["response_time"])
    users.append(response["users"])
    average_response_time.append(response["response_time"])
print("total_count_is", sum(total_count))
print("average_response_time_is", (sum(average_response_time))/c)
for i in total_count:
    if i == 200:
        count_of_passed_responses.append(i)
print("count_of_passed_responses_is", sum(count_of_passed_responses))

for person in users:
    if person not in unique_users:
        unique_users.append(person)
print("unique_users", unique_users)