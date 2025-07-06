import numpy as np
import matplotlib.pyplot as plt
class operation:

    def __init__(self, int_array):
        if not isinstance(int_array, np.ndarray) or int_array.dtype!= int:
            raise ValueError("Enter a valid array of intergers!")
        
        self.int_array = int_array

    def display(self):
        print(self.int_array)

    def salary(self):
        arr_shape = self.int_array.shape
        money_per_product = np.full(arr_shape, 5)
        salaraies = self.int_array*money_per_product #or we can use int_array*5 too. We dont have to create a shape tbh

        print(f"people made {self.int_array} products and made the salaray of {salaraies}")
        
    def plot(self):
        x=np.arange(len(self.int_array))
        plt.plot(x, self.int_array, marker='o')
        plt.grid()
        plt.title("Employee rank-salary")
        plt.xlabel('Empleyee rank(products)')
        plt.ylabel('Employee salary')
        plt.xticks(x)
        plt.show()