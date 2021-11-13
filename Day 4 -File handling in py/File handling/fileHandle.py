import time

filename = 'example3-10x5.txt'
input_file = open(filename)


# Read first line of file and store in no_of_polynomials 
no_of_polynomials=input_file.readline()

# Read second line of file and store in no_of_variables 
no_of_variables=input_file.readline()

# This code will store the data read from file in matrix
data_structure = 'matrix'
matrix = [line.replace('\n',' ').replace('\t',' ').split() for line in input_file]
for row in matrix:
    print(row)

# Close the open file  
input_file.close()


#Polynomial addition

start_time = time.time()

non_zero_values = 0

result = [0 for i in range(len(matrix[0]))]
for row in matrix:
    for index,value in enumerate(row):
        result[index]+=int(value)
        if value !=0:
            non_zero_values+=1
        
end_time = time.time()
total_time = end_time - start_time


#Displaying result in cmd 
print("\n*****************Result************************\n")
print(result)


#Adding result to the file
result_file = open('addtion_result.txt','w')
result_file.write(filename+'\n')
result_file.write(str(result))
result_file.close()


print("\n*****************Summary************************\n")
print(f"filename : {filename}\n")
print(f"no_of_polynomials : {no_of_polynomials}")
print(f"no_of_variables : {no_of_variables}")
print(f"non_zero_values : {non_zero_values}\n")
print(f"data_structure : {data_structure}\n")
print(f"Time taken for polynomial addition: {total_time} seconds\n")