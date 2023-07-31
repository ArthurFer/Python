linguagens = ["python", "C", "C++", "java", "angular"]
print(sorted(linguagens, key= lambda x: len(x))) #Mesma função do Sort, a diferença é que o Sorted é uma função built-in do python
print(sorted(linguagens, key= lambda x: len(x), reverse=True))