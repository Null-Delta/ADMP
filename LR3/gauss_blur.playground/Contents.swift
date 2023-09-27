import Cocoa
import Foundation

func gaussMatrix(width: Int, height: Int, a: Float, b: Float, d: Float) -> [[Float]] {
    var matrix: [[Float]] = .init(repeating: .init(Array(repeating: 0.0, count: height)), count: width)

    for x in 0..<width {
        for y in 0..<height {
            matrix[x][y] = (1 / (2 * Float.pi) * powf(d, 2)) / expf(
                -(powf(Float(x) - a, 2) + powf(Float(y) - b, 2)) / (2 * powf(d, 2))
            )
        }
    }

    return matrix
}

func normalizeMatrix(matrix: [[Float]]) -> [[Float]] {
    var sum: Float = 0
    var output: [[Float]] = .init(repeating: .init(Array(repeating: 0.0, count: matrix[0].count)), count: matrix.count)

    for x in 0..<matrix.count {
        for y in 0..<matrix[0].count {
            sum += matrix[x][y]
        }
    }

    for x in 0..<matrix.count {
        for y in 0..<matrix[0].count {
            output[x][y] = matrix[x][y] / sum
        }
    }

    return output
}

func applyKernel(kernel: [[Float]], image: [[Float]], x: Int, y: Int) -> Float {
    var value: Float = 0.0

    for xt in 0..<kernel.count {
        for yt in 0..<kernel[0].count {
            value += image[xt + x][yt + y] * kernel[xt][yt]
        }
    }

    return value
}

func gaussBlur(kernel: [[Float]], image: [[Float]]) -> [[Float]] {
    var output: [[Float]] = .init(repeating: .init(Array(repeating: 0.0, count: image[0].count - kernel[0].count)), count: image.count - kernel.count)

    for x in 0..<image.count - kernel.count {
        for y in 0..<image[0].count - kernel[0].count {
            output[x][y] = applyKernel(kernel: kernel, image: image, x: x, y: y)
        }
    }

    return output
}

var image: [[Float]] = .init(repeating: .init(Array(repeating: 0.0, count: 50)), count: 50)

for x in 0..<50 {
    for y in 0..<50 {
        image[x][y] = ((x + y) % 2) == 0 ? 5 : 10
    }
}

let matrix = normalizeMatrix(matrix: gaussMatrix(width: 5, height: 5, a: 2, b: 2, d: 5))

let blur = gaussBlur(kernel: matrix, image: image)

print(blur)
print("aboba")
