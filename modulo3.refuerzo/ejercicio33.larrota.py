def estadisticas_lista(nums):
    return {'min': min(nums), 'max': max(nums), 'sum': sum(nums), 'avg': sum(nums)/len(nums)}

if __name__ == '__main__':
    print(estadisticas_lista([1,2,3,4,5]))
