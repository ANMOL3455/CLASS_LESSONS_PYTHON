#after the fundamental datatype we have collection
#collection datatype can be defined as the collection of datatyped under a format
#collection datatypes have list,set,tupple and dictionary
#-----------------------------
#1>>list
#-----------------------------
#list can be identified by looking its data enclosed inside a big bracket
#example
roll_list=[12,13,14,15,16]
print(roll_list)
#the output will be >>>>>> [12,13,14,15,16]
#we can also see the list datatype
#for that
print("the datatype of the roll_list is : ",type(roll_list))
#its acessig will be learnt while learning loops
#datas here can be changed
#datas here are in fixed order
#-----------------------------
#2>>tuple
#-----------------------------
#tuple can be identified by looking its data enclosed inside a small bracket
#datas here are in fixed order
#if no bracket and only data in collection format then it is tuple
#example
roll_tuple=(12,13,14,15,16)
print(roll_tuple)
#the output will be >>>>>> [12,13,14,15,16]
#we can also see the tuple datatype
#for that
print("the datatype of the roll_list is : ",type(roll_tuple))
#its acessig will be learnt while learning loops
#datas here cannot be changed
#-----------------------------
#3>>SET
#-----------------------------
#set can be identified by looking its data enclosed inside a curly bracket
#datas order are not fixed
#datas should be unique
#example
roll_set={12,13,14,15,16}
print(roll_set)
#the output will be >>>>>> {12,13,14,15,16}
#we can also see the set datatype
#for that
print("the datatype of the roll_list is : ",type(roll_set))
#datas here cannot be changed
#-----------------------------
#4>>DICTIONARY   (dict)
#-----------------------------
#dictionary can be identified by looking its data enclosed inside a curly bracket but should include key and value
#datas should have key and value
#key cannot be duplicated but values can be many
#a data should have single key but a key can have multiple data that is value
#key should be unique
#example
roll_dict={"age_1":12,"age_2":13,"age_3":14,"age_4":15,"age_5":16}
print(roll_dict)
#the output will be >>>>>> {"age_1":12,"age_2":13,"age_3":14,"age_4":15,"age_5":16}
#we can also see the set datatype
#for that
print("the datatype of the roll_list is : ",type(roll_dict))
#values here can  be changed