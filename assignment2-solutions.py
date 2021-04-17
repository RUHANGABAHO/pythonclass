# """assignment two - programming club- solution """
#
# """ Number one  a) """
# def Course():
#     pass
#
#
# """ number 1 b) """
# def Course():
#     course_name = ""
#     mark_one = ""
#     mark_two = ""
#
# """ number 1 c) """
# def Course():
#
#     course_name = ""
#     mark_one = ""
#     mark_two = ""
#
#     course_name = input("Enter your course name: ")
#     mark_one = input("Enter mark one: ")
#     mark_two = input("Enter mark two: ")
#
# """ number 1 d) """
# def Course():
#
#     course_name = ""
#     mark_one = ""
#     mark_two = ""
#
#     course_name = input("Enter your course name: ")
#     mark_one = input("Enter mark one: ")
#     mark_two = input("Enter mark two: ")
#
#     avg_mark = (int(mark_one) + int(mark_two))/2
#
# """ number 1 e) """
# def Course():
#
#     course_name = ""
#     mark_one = ""
#     mark_two = ""
#
#     course_name = input("Enter your course name: ")
#     mark_one = input("Enter mark one: ")
#     mark_two = input("Enter mark two: ")
#
#     avg_mark = (int(mark_one) + int(mark_two))/2
#     total_mark = (int(mark_one) + int(mark_two))
#
# """ number 1 f) """
# def Course():
#
#     course_name = ""
#     mark_one = ""
#     mark_two = ""
#
#     course_name = input("Enter your course name: ")
#     mark_one = input("Enter mark one: ")
#     mark_two = input("Enter mark two: ")
#
#     avg_mark = (int(mark_one) + int(mark_two))/2
#     total_mark = (int(mark_one) + int(mark_two))
#
#     my_collections = [mark_one, mark_two, avg_mark, total_mark]
#
# """ number 1 g) """
# def Course():
#
#     course_name = ""
#     mark_one = ""
#     mark_two = ""
#
#     course_name = input("Enter your course name: ")
#     mark_one = input("Enter mark one: ")
#     mark_two = input("Enter mark two: ")
#
#     avg_mark = (int(mark_one) + int(mark_two))/2
#     total_mark = (int(mark_one) + int(mark_two))
#
#     my_collections = [mark_one, mark_two, avg_mark, total_mark]
#
#     my_first_tuple = tuple(my_collections)
#
#
#
# """ number 1 g) """
# def Course():
#
#     course_name = ""
#     mark_one = ""
#     mark_two = ""
#
#     course_name = input("Enter your course name: ")
#     mark_one = input("Enter mark one: ")
#     mark_two = input("Enter mark two: ")
#
#     avg_mark = (int(mark_one) + int(mark_two))/2
#     total_mark = (int(mark_one) + int(mark_two))
#
#     my_collections = [mark_one, mark_two, avg_mark, total_mark]
#
#     my_first_tuple = tuple(my_collections)

#     return "The reults of " + course_name + " are " + str(my_first_tuple)
#
# """ question 2 a) """
# def mainFunc():
#     caller  = Course()
#     return caller
#
# """ question 2 b) """
# print(mainFunc())
#
#
# """
# tuples alone
# question 3 a)
# """
# my_second_tuple = ("hello", 1, 3, 8.1, "there", 5, 10,)
#
#
# first = my_second_tuple[0]
# middle = my_second_tuple[int(len(my_second_tuple)/2)]
# last = my_second_tuple[-1]
# print(str(first)+" "+str(middle)+" "+str(last))
#
# """
# question 3 b)
# """
# to_list = list(my_second_tuple)
# to_list[0] = "JET"
# back_to_tuple = tuple(to_list)
# print(back_to_tuple)
#
# """
# _____Tuples and lists_____
#
#     --differences--
# >>>Tuples are immutable whereas lists are mutable
#    i.e. You cannot change anything in a tuple but you can in a list.
#
# >>>A tuple is created with ()-->just round-brackets with a leading comma(though not necessary with python 3.5+)
#    whereas lists are created with square brackets -->[].
#
#     --similarities--
# >>>accessing elements is the same i.e. by indexes.
#
# Tuples are said to be immutable coz you can't direct mutate/change any element in them.
# To do so, you need to first change them back to lists and mutate them and change them back to tuples as shown in the example above.
# """
# y=lambda a,b :a+b
#     print(y(2,7))
for x in range(0,100,10):
    print(x)