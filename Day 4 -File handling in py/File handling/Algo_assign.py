import time

def using_matrix():
        
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


def using_linked_list():
    # Node class
    class Node:

        # Function to initialise the node object
        def __init__(self, data):
            self.data = data # Assign data
            self.next = None # Initialize next as null


    # Linked List class contains a Node object
    class LinkedList:

        # Function to initialize head
        def __init__(self):
            self.head = None


        # This function is defined in Linked List class
        # Appends a new node at the end. This method is
        # defined inside LinkedList class shown above */
        def append(self, new_data):

            # 1. Create a new node
            # 2. Put in the data
            # 3. Set next as None
            new_node = Node(new_data)

            # 4. If the Linked List is empty, then make the
            # new node as head
            if self.head is None:
                self.head = new_node
                return

            # 5. Else traverse till the last node
            last = self.head
            while (last.next):
                last = last.next

            # 6. Change the next of last node
            last.next = new_node


        # Utility function to print the linked list
        def printList(self):
            temp = self.head
            while (temp):
                print(temp.data) 
                temp = temp.next



    filename = 'example3-10x5.txt'
    input_file = open(filename)


    # Read first line of file and store in no_of_polynomials 
    no_of_polynomials=input_file.readline()

    # Read second line of file and store in no_of_variables 
    no_of_variables=input_file.readline()

    # This code will store the data read from file in linked_list
    data_structure = 'linked_list'
    linked_list = [line.replace('\n',' ').replace('\t',' ').split() for line in input_file]
    for row in linked_list:
        print(row)



    # Close the open file  
    input_file.close()


    #Polynomial addition

    start_time = time.time()

    non_zero_values = 0

    result = [0 for i in range(len(linked_list[0]))]
    for row in linked_list:
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




if __name__ == "__main__":
    
   
    while True:
    
        print(f"0.Exit")
        print(f"1.Matrix")
        print(f"2.Linked_list")
        option = int(input('Enter your option : '))
        if option == 0:
                break
        elif option == 1:
            using_matrix()
        elif option == 2:
            using_linked_list()
        else:
            print('Wrong choice....')