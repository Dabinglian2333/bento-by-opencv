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

# 查找轮廓
contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# 筛选出最大的轮廓，这个轮廓应该是汉堡肉
if contours:
    largest_contour = max(contours, key=cv2.contourArea)
    # 填充轮廓区域
    cv2.drawContours(image, [largest_contour], -1, (19, 69, 139), thickness=cv2.FILLED)
    # 绘制轮廓边界
    cv2.drawContours(image, [largest_contour], -1, (0, 0, 255), 3)

    # 计算重心
    M = cv2.moments(largest_contour)
    if M['m00'] != 0:
        cx = int(M['m10'] / M['m00'])
        cy = int(M['m01'] / M['m00'])
        # 标记重心
        cv2.circle(image, (cx, cy), 5, (255, 0, 0), -1)
        cv2.putText(image, 'Center of gravity', (cx - 40, cy - 20), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 0, 0), 3)

# 保存结果图像
output_path = 'D:/Hamburger_center of gravity.jpg'
cv2.imwrite(output_path, image)

output_path