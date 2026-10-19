# Exercise 20: find_highest_paid_employee(database)
# Receive a tuple of employee records (id, name, department, salary) and return
# the record with the highest salary. Return () if database is empty.
#
# Example tests:
#   find_highest_paid_employee(()) -> ()
#   find_highest_paid_employee(((1, "Alice", "Engineering", 7500),))
#       -> (1, 'Alice', 'Engineering', 7500)
#   find_highest_paid_employee(((1, "Alice", "Engineering", 5500),
#                               (2, "Bob", "HR", 6200),
#                               (3, "Charlie", "Engineering", 6100)))
#       -> (2, 'Bob', 'HR', 6200)

def find_highest_paid_employee(database):
    if not database:
        return ()
    highest = database[0]
    for record in database[1:]:
        if record[3] > highest[3]:
            highest = record
    return highest


if __name__ == "__main__":
    print(find_highest_paid_employee(()))
    print(find_highest_paid_employee(((1, "Alice", "Engineering", 7500),)))
    print(find_highest_paid_employee(((1, "Alice", "Engineering", 5500),
                                      (2, "Bob", "HR", 6200),
                                      (3, "Charlie", "Engineering", 6100))))
