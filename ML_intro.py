#Q1. From given list x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16], produce an output of [8, 9, 10, 11, 12]
#a) Do this by using slicing from the front (positive)
#b) Do this by using slicing from the back (negative)  
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
print(x[7:12])#positive 
print(x[-9:-4])#negative



#Q2.Print even number from x using list slicing only. 
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
print(x[1::2])




#Q3.Print every 4th number using list slicing only. 
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
print(x[::4])
