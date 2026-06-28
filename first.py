import numpy as np
import matplotlib.pyplot as plt

marks = np.random.randint(0, 100, 1000) 

print("Average Mark hai:", marks.mean()) 
print("Sab se bara Mark hai:", marks.max()) 


plt.hist(marks, bins=20, color='hotpink', edgecolor='black') 

plt.title("Rida ki CSC Class - Marks ka Graph") 
plt.xlabel("Marks") 
plt.ylabel("Kitne Students") 
plt.show() 
