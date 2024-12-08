import plotly.graph_objects as go



################################################################################
# 여기만 수정                                                                     #
################################################################################

# 🔥 상단에 선언된 변수들 (여기서만 변경하면 됩니다)
cone_color = 'black'  # 화살표(Cone)의 색상을 조절하는 변수
point_size = 5  # 데이터 점의 크기를 조절하는 변수
label_text_size = 15  # 데이터 점의 라벨 텍스트 크기를 조절하는 변수

x_text = 'Foundation<br>Vision Models'  # X 축 끝에 표시할 텍스트
y_text = 'Language Models'  # Y 축 끝에 표시할 텍스트
z_text = 'Text Alignment <br> Vision Models'  # Z 축 끝에 표시할 텍스트

# 🔥 자동으로 추가될 점과 라벨 정보
data = [
    # Ours
    ['Our Model', 0.5, 0.5, 0, 'b'],

    #

    #textmodel
    ['GPT3', 0, 0.7, 0, 'l'],
    ['LLaMA', 0, 0.8, 0, 'r'],
    ['Mixtral', 0, 0.78, 0.08, 'r'],
    ['Gemma', 0.08, 0.78, 0, 'l'],

    #VLM
    ['BLIP', 0, 0.6, 0.6, 'r'],
    ['LLaVA', 0, 0.5, 0.5, 'l'],
    ['Pali-Gemma', 0, 0.6, 0.5, 'b'],

    #text alignment
    ['CLIP', 0.0, 0.0, 0.7, 'l'],

    # vision output
    ['SAM', 0.5, 0, 0.5, 'r'],
    ['DINO', 0.6, 0, 0.6, 'l'],
    ['GLIP', 0.5, 0, 0.6, 'r'], # 그라운딩 다이노랑 똑같은 테스크인데 DINO가 좀 혼동될 수 있어서 대체

    # vision
    ['YOLO', 0.7, 0, 0, 'r'],
    ['ResNet', 0.8, 0, 0, 'l'],
    ['ViT', 0.78, 0, 0.08, 'l'],
]
################################################################################
################################################################################

#고정 변수
text_size = 20  # 텍스트 크기를 조절하는 변수
cone_size = 0.05  # 화살표(Cone)의 크기를 조절하는 변수

# RGB → HEX 변환 함수
def rgb_to_hex(r, g, b):
    """RGB 값을 HEX 코드로 변환합니다."""
    return f'#{int(r):02x}{int(g):02x}{int(b):02x}'

# X, Y, Z 축의 화살표 추가 (단순 화살표로 그리기)
axes = [
    # X 축 화살표 (시작점 0,0,0 끝점 1,0,0)
    go.Scatter3d(
        x=[0, 1], 
        y=[0, 0], 
        z=[0, 0], 
        mode='lines+markers+text', 
        line=dict(color='black', width=5),  # 색상 변경 (검정색)
        marker=dict(size=2, color='black'),  # 마커 색상 변경 (검정색)
        text=['', x_text],  # 화살표 끝에 X 텍스트 추가
        textfont=dict(size=text_size),  # 텍스트 크기 조절
        textposition='bottom center',  # 텍스트 위치 조정
        name=x_text
    ),
    # Y 축 화살표 (시작점 0,0,0 끝점 0,1,0)
    go.Scatter3d(
        x=[0, 0], 
        y=[0, 1], 
        z=[0, 0], 
        mode='lines+markers+text', 
        line=dict(color='black', width=5),  # 색상 변경 (검정색)
        marker=dict(size=2, color='black'),  # 마커 색상 변경 (검정색)
        text=['', y_text],  # 화살표 끝에 Y 텍스트 추가
        textfont=dict(size=text_size),  # 텍스트 크기 조절
        textposition='middle right',  # 텍스트 위치 조정
        name=y_text
    ),
    # Z 축 화살표 (시작점 0,0,0 끝점 0,0,1)
    go.Scatter3d(
        x=[0, 0], 
        y=[0, 0], 
        z=[0, 1], 
        mode='lines+markers+text', 
        line=dict(color='black', width=5),  # 색상 변경 (검정색)
        marker=dict(size=2, color='black'),  # 마커 색상 변경 (검정색)
        text=['', z_text],  # 화살표 끝에 Z 텍스트 추가
        textfont=dict(size=text_size),  # 텍스트 크기 조절
        textposition='middle right',  # 텍스트 위치 조정
        name=z_text
    )
]

# 🔥 data 리스트의 점과 라벨을 자동으로 추가
position_map = {'r': 'middle right', 'l': 'middle left', 't': 'top center', 'b': 'bottom center'}  # 라벨 위치 매핑
for point in data:
    name, x, y, z, position = point
    r = min(255, int(x * 255) + 100)  # 빨간색을 더 강조
    g = int(y * 255)
    b = int(z * 255)
    color = rgb_to_hex(r, g, b)  # RGB → HEX 변환
    text_position = position_map.get(position, 'bottom center') 
    if name == 'Our Model':
        # 🔥 Our Model을 노란색 별로 추가 (symbol='star-diamond' 사용)
        axes.append(
            go.Scatter3d(
                x=[x], 
                y=[y], 
                z=[z], 
                mode='markers+text', 
                marker=dict(size=point_size + 5, color=color, symbol='diamond'),  # 노란색 별 (대체됨)
                text=[name], 
                textfont=dict(size=label_text_size, color=color),  # 검정색 텍스트
                textposition=text_position,  
                name=name
            )
        )
        continue
      # 데이터 분할
    # x, y, z 값을 RGB로 변환 (0~1 -> 0~255로 스케일)
     # 기본값은 bottom center
    axes.append(
        go.Scatter3d(
            x=[x], 
            y=[y], 
            z=[z], 
            mode='markers+text', 
            marker=dict(size=point_size, color=color, symbol='circle'),  # 점의 크기를 조절하는 변수로 수정
            text=[name],  # 라벨 추가
            textfont=dict(size=label_text_size, color=color),  # 텍스트 크기와 색상
            textposition=text_position,  # 라벨 위치 조정
            name=name
        )
    )

# 레이아웃 설정 (그리드 및 배경 제거, X, Y, Z 글자 삭제)
layout = go.Layout(
    scene=dict(
        xaxis=dict(
            range=[-0.2, 1.2], 
            showbackground=False, 
            showgrid=False, 
            zeroline=False, 
            showticklabels=False,  
            title=''  
        ),
        yaxis=dict(
            range=[-0.2, 1.2], 
            showbackground=False, 
            showgrid=False, 
            zeroline=False, 
            showticklabels=False,  
            title=''  
        ),
        zaxis=dict(
            range=[-0.2, 1.2], 
            showbackground=False, 
            showgrid=False, 
            zeroline=False, 
            showticklabels=False,  
            title=''  
        )
    ),
    showlegend=True  
)

# 그래프 통합
fig = go.Figure(data=axes, layout=layout)
fig.show()