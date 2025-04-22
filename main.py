def numTrees(n):
    
    
    cache = {}
    
    def count_trees(n):
        
        if n <= 1:
            return 1
        
        
        if n in cache:
            return cache[n]
        
        total = 0
        
        for i in range(1, n + 1):
        
            left_trees = count_trees(i - 1)
            
        
            right_trees = count_trees(n - i)
            
        
            total += left_trees * right_trees
        
        
        cache[n] = total
        return total
    
    return count_trees(n)


def test_unique_bsts():
    print("Número de BSTs únicos para diferentes valores de n:")
    for i in range(1, 11):
        print(f"n = {i}: {numTrees(i)}")

# Executa os testes
if __name__ == "__main__":
    test_unique_bsts()