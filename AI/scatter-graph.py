import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

# 1. 상수 데이터 정의
# - 각 군집(Cluster)에 해당하는 2차원 좌표 5개씩 총 20개 점
# - 군집 간 시각적으로 구분되도록 좌표를 멀리 배치
X = [
    # Cluster 0 
    (2.0, 1.8), (1.8, 2.2), (2.2, 2.0), (1.9, 2.1), (2.1, 1.9),
    # Cluster 1
    (6.0, 2.1), (6.2, 1.8), (5.8, 2.0), (6.1, 2.2), (5.9, 1.9),
    # Cluster 2
    (2.0, 6.0), (2.2, 6.2), (1.8, 5.9), (2.1, 6.1), (1.9, 5.8),
    # Cluster 3
    (6.0, 6.0), (5.9, 6.2), (6.1, 5.8), (5.8, 5.9), (6.2, 6.1)
]

# 2. 각 점이 속한 군집 번호 정의
# - 0~3까지의정수로각 군집을 구분
# - 이 값은 산점도에서 색상을 결정하는 기준으로 사용됨
# [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3]
cluster_labels = [0]*5 + [1]*5 + [2]*5 + [3]*5

# 3. X 좌표와 Y 좌표를 분리
x = [pt[0] for pt in X]
y = [pt[1] for pt in X]

# 4. 색상 정의
# - tab10 컬러맵에서 앞의4가지 색만 추출하여 사용할 컬러맵 생성
# - 기본 colormap 사용 시 자동 정규화로 색상이 예상과 달라질 수 있으므로,
#   정확한 색상 제어를 위해 ListedColormap 사용
#   색상 인덱스: 0 -> 파랑, 1 -> 주황, 2 -> 초록, 3 -> 빨강
colors = [plt.cm.tab10(i) for i in range(4)]
custom_cmap = ListedColormap(colors)

# 5. 산점도 그리기
# - 각 점의 색상은 cluster_labels 값을 기반으로 custom_cmap 에서 선택됨
plt.scatter(x, y, c=cluster_labels, cmap=custom_cmap, s=100, alpha=0.8)

# 6. 그래프 제목과 축 라벨 설정
plt.title("4 Clusters (Colors mapped by ListedColormap from tab10)")
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")

# 7. 그래프 출력
plt.show()