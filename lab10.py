import cv2
import matplotlib.pyplot as plt

# Đọc ảnh xám
img = cv2.imread("image.png", 0)

# Kiểm tra ảnh
if img is None:
    print("Không tìm thấy ảnh")
    exit()

# Các kiểu threshold
ret1, th1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
ret2, th2 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)
ret3, th3 = cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC)
ret4, th4 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)
ret5, th5 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO_INV)

titles = [
    'Original',
    'BINARY',
    'BINARY_INV',
    'TRUNC',
    'TOZERO',
    'TOZERO_INV'
]

images = [img, th1, th2, th3, th4, th5]

# Hiển thị kết quả
for i in range(6):
    plt.subplot(2, 3, i + 1)
    plt.imshow(images[i], cmap='gray')
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])

plt.show()