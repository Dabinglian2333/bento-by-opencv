import cv2
import numpy as np

# 读取图片
image = cv2.imread('D:/Hamburger.jpg')

# 将图片转换为HSV颜色空间
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# 定义汉堡肉的颜色范围
lower_brown = np.array([10, 50, 25])
upper_brown = np.array([20, 255, 126])

# 根据颜色范围创建掩膜
mask = cv2.inRange(hsv, lower_brown, upper_brown)

# 使用掩膜提取汉堡肉区域
result = cv2.bitwise_and(image, image, mask=mask)

# 查找轮廓
contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# 筛选出最大的轮廓，这个轮廓应该是汉堡肉
if contours:
    largest_contour = max(contours, key=cv2.contourArea)
    cv2.drawContours(image, [largest_contour], -1, (0, 255, 0), 3)

# 保存结果图像
output_path = 'D:/Hamburger_boundary.jpg'
cv2.imwrite(output_path, image)

output_path
