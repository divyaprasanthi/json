import json
json_obj='{ "name":"david","class":"I","age":6 }'
python_obj=json.loads(json_obj)
print("\njson data:")
print(python_obj)
print("\nname:",python_obj["name"])
print("class: ",python_obj["class"])
print("age: ",python_obj["age"])
import json
python_obj={
    "name":"david",
    "class":"i",
    "age":6
    }
print(type(python_obj))
j_data=json.dumps(python_obj)
print(j_data)
# python program to convert python object into json strings.print all the values
import json
python_dict={"name": "david","age":6,"class":"I"}
python_list=["red","green","black"]
python_str="python json"
python_int=(1234)
python_float=(21.34)
python_T=(True)
python_F=(False)
python_N=(None)
json_dict=json.dumps(python_dict)
json_list=json.dumps(python_list)
json_str=json.dumps(python_str)
json_num1=json.dumps(python_int)
json_num2=json.dumps(python_float)
json_t=json.dumps(python_T)
json_f=json.dumps(python_F)
json_n=json.dumps(python_N)


print("json dict:", json_dict)
print("json list:",json_list)
print("json string:",json_str)
print("json number1:",json_num1)
print("json number2:",json_num2)
print("json true:",json_t)
print("json false:",json_f)
print("json null:",json_n)

