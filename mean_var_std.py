def calculate(data):
    if not len(data) == 9:
        raise ValueError("List must contain nine numbers.")
    import numpy as np
    arr = np.array(data).reshape(3, 3)
    calculations = {
        'mean': [np.mean(arr, axis=0).tolist(), np.mean(arr, axis=1).tolist(), float(np.mean(arr))],
        'variance': [np.var(arr, axis=0).tolist(), np.var(arr, axis=1).tolist(), float(np.var(arr))],
        'standard deviation': [np.std(arr, axis=0).tolist(), np.std(arr, axis=1).tolist(), float(np.std(arr))],
        'max': [np.max(arr, axis=0).tolist(), np.max(arr, axis=1).tolist(), float(np.max(arr))],
        'min': [np.min(arr, axis=0).tolist(), np.min(arr, axis=1).tolist(), float(np.min(arr))],
        'sum': [np.sum(arr, axis=0).tolist(), np.sum(arr, axis=1).tolist(), int(np.sum(arr))]
    }
    return calculations
if __name__ == "__main__":
    c=calculate([0,1,2,3,4,5,6,7,8])
    print(c)
        