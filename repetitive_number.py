#code for displaying maximum repetive number

test_array=[]
n=int(raw_input("Enter the number of elements in the array 'n' : "))
test_array=raw_input("Enter n elements with spaces : ").strip().split()
#final_array=[int(i) for i in test_array]
arr=[int(i) for i in test_array]
max_count=1
sumx=1
multiple_element={}
         
for i in range(n):
    if arr[i] in multiple_element.keys():        
        sumx=sumx+1
        multiple_element[arr[i]]=sumx
        if(max_count<sumx):
            max_count=sumx
    else:
        sumx=1
        multiple_element[arr[i]]=sumx

#print(multiple_element)
#print(multiple_element.items())
print("The most repetitive length of element is : "+str(max_count))
for k,v in multiple_element.items():
    if(max_count==v):
        print("The maximum repeated number is "+ str(k))
