def quicksort(arr):
    """
    Função principal para ordenar um array usando o algoritmo Quicksort.
    """
    def _quicksort(arr, low, high):
        """
        Função recursiva para realizar o Quicksort.
        """
        if low < high:
            # Particiona o array e obtém o índice do pivô
            pivot_index = partition(arr, low, high)
            # Ordena as partes esquerda e direita do pivô
            _quicksort(arr, low, pivot_index - 1)
            _quicksort(arr, pivot_index + 1, high)

    def partition(arr, low, high):
        """
        Função para particionar o array em torno de um pivô.
        """
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    # Chama a função recursiva passando os índices iniciais
    _quicksort(arr, 0, len(arr) - 1)

# Teste
arr = [10, 7, 8, 9, 1, 5]
quicksort(arr)
print("Array ordenado:", arr)


def buscaLinear(arr, target):
    for i in range(len(arr)):
        if target <= arr[i]:
            return i
    return len(arr)
	
# [1, 5, 7, 8, 9, 10]

target = 6
resultado = buscaLinear(arr, target)
print(resultado)


