from find_ft_type import all_things_is_obj

ft_list = ["Hello", "tata"]
ft_tuple = ("Hello", "toto")
ft_set = {"Hello", "tutu"}
ft_dict = {"Hello" : "titi"}

all_things_is_obj(ft_list)
all_things_is_obj(ft_tuple)
all_things_is_obj(ft_set)
all_things_is_obj(ft_dict)
all_things_is_obj("Brian")
all_things_is_obj("Toto")
print(all_things_is_obj(10))