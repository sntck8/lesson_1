immutable_var = 1, 5, "строка" , False
print("Immutable tuple: ", (immutable_var))

#данные в кортеже (tuple) не изменяюся, в отличии от списков (list)

mutable_list = [4, 231, True,"лист"]
mutable_list[0]  = 55445
mutable_list[1] = float(555.666)
mutable_list[2] = str("изм. список")
mutable_list[3] = bool(False)
print("Mutable list: ", mutable_list)