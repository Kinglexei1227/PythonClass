import pandas as pd
import plotly.express as px

# 작업 데이터 만들기
data = {
    "Task": ["기획", "디자인", "개발", "테스트"],
    "Start": ["2025-04-01", "2025-04-04", "2025-04-08", "2025-04-15"],
    "Finish": ["2025-04-03", "2025-04-07", "2025-04-14", "2025-04-17"]
}
df = pd.DataFrame(data)

# 날짜 문자열을 날짜 형식으로 바꾸기
df["Start"] = pd.to_datetime(df["Start"])
df["Finish"] = pd.to_datetime(df["Finish"])

# 간트차트 그리기 (plotly 사용)
fig = px.timeline(df, x_start="Start", x_end="Finish", y="Task", title="간트차트 예시")
fig.update_yaxes(categoryorder="total ascending")  # 작업 순서 위에서 아래로
fig.show()