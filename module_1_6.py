number_of_comleted_tasks: int = 12
number_of_hours_spent: float = 1.5
average_value = float(number_of_hours_spent) / int(number_of_comleted_tasks)
course_name = "Python"
print("Курс: " + str(course_name) +", "+ "всего задач: " + str(number_of_comleted_tasks) +", "
      + "затрачено часов: " + str(number_of_hours_spent) + ", " + "среднее время выполнения: " + str(average_value)
       +"  часа")