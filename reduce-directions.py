#Reduce Directions Algorithm created and written by Bahram Esmailian
#this algorithm gets rid of repetitive directions such as south then north, north then south, etc.

arr = ['NORTH', 'SOUTH', 'SOUTH', 'EAST', 'WEST', 'NORTH', 'WEST']
ew_set = [['EAST', 'WEST'],['WEST','EAST']]
ns_set = [['NORTH', 'SOUTH'],['SOUTH', 'NORTH']]
i = 0
while True:
    if i == len(arr)-1:
        print(arr)
        break
    if [arr[i],arr[i+1]] in ew_set:
            arr.pop(i)
            arr.pop(i)
            i = 0
            continue
    elif [arr[i],arr[i+1]] in ns_set:
            arr.pop(i)
            arr.pop(i)
            i = 0
            continue
    i +=1
print(arr)
