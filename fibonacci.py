def fibonacci(numOfIter):
    fibSeriesList,nextEleInFib = [0],1
    for _ in range(numOfIter):
        fibSeriesList.append(nextEleInFib)
        nextEleInFib = fibSeriesList[-1]+fibSeriesList[-2]
    return fibSeriesList
        
 
print(fibonacci(5))
print(fibonacci(10))