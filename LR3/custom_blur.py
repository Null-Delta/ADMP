import math

def createGaussMatrix(width, height, a, b, d):
    matrix = []

    for x in range(width):
        matrix.append([])
        for y in range(height):
            matrix[x].append(
                (1 / ((2 * math.pi) * (d ** 2))) *
                math.exp(
                    -((x - a) ** 2 + (y - b) ** 2) / (2 * (d ** 2))
                )
            )

    return matrix

def normalizeMatrix(matrix):
    summ = 0
    normalized_matrix = matrix.copy()
    for x in range(len(matrix)):
        for y in range(len(matrix[0])):
            summ += matrix[x][y]

    for x in range(len(matrix)):
        for y in range(len(matrix[0])):
            normalized_matrix[x][y] /= summ
    
    return normalized_matrix 

def applyKernel(kernel, image, x, y):
    value = 0
    for x_t in range(len(kernel)):
        for y_t in range(len(kernel[0])):
            value += image[x_t + x][y_t + y] * kernel[x_t][y_t]
    
    return value

def gaussBlur(image, kernel):
    imageResult = image.copy()
    for x in range(len(image) - len(kernel)):
        for y in range(len(image[0]) - len(kernel[0])):
            imageResult[x + int(len(kernel) / 2)][y + int(len(kernel[0]) / 2)] = applyKernel(kernel, image, x, y)

    return imageResult[int(len(kernel) / 2): len(image) - len(kernel), int(len(kernel[0]) / 2): len(image[0]) - len(kernel[0])]
