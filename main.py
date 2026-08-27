import streamlit as st
import time

# 1. 페이지 기본 설정
st.set_page_config(
    page_title="✨ MBTI 궁극의 직업 탐험대 ✨",
    page_icon="🎨",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. 커스텀 CSS (화려하고 알록달록한 스타일링)
st.markdown("""
    <style>
    /* 전체 배경에 무지개 빛 밝은 그라데이션 적용 */
    .stApp {
        background: linear-gradient(135deg, #ff9a9e 0%, #fecfef 50%, #a1c4fd 100%);
    }
    
    /* 메인 타이틀 */
    .main-title {
        font-size: 3.2rem !important;
        font-weight: 900;
        color: #ffffff;
        text-shadow: 3px 3px 12px rgba(0, 0, 0, 0.25);
        text-align: center;
        padding: 25px;
        background: rgba(255, 255, 255, 0.25);
        border-radius: 25px;
        backdrop-filter: blur(12px);
        margin-bottom: 20px;
        border: 2px solid rgba(255, 255, 255, 0.5);
    }

    /* 서브 타이틀 */
    .sub-title {
        text-align: center;
        color: #333333;
        font-weight: bold;
        font-size: 1.4rem;
        margin-bottom: 25px;
    }

    /* 메인 직업 추천 카드 */
    .job-card {
        background: rgba(255, 255, 255, 0.9);
        border-radius: 20px;
        padding: 22px;
        box-shadow: 0 10px 20px rgba(0,0,0,0.08);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
        margin-bottom: 15px;
        border: 2px solid #ffffff;
        height: 100%;
    }
    
    /* 탭 스타일 조정 */
    .stTabs [data-baseweb="tab-list"] {
        gap: 12px;
    }

    .stTabs [data-baseweb="tab"] {
        height: 55px;
        white-space: pre-wrap;
        background-color: rgba(255, 255, 255, 0.7);
        border-radius: 15px 15px 0px 0px;
        padding: 10px 20px;
        font-weight: bold;
        font-size: 1.1rem;
    }

    .stTabs [aria-selected="true"] {
        background-color: #ffffff !important;
        color: #FF4B4B !important;
        border-top: 4px solid #FF4B4B;
    }

    /* 확장 카드 박스 */
    .extra-job-box {
        background-color: #ffffff;
        border-radius: 15px;
        padding: 15px;
        border-left: 6px solid #6C5CE7;
        margin-bottom: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# 3. 확장된 MBTI별 직업 데이터베이스 (메인 직업 + 기타 탐색 직업)
mbti_db = {
    "INTJ": {
        "title": "🧠 용의주도한 전략가 (INTJ)",
        "desc": "전체적인 그림을 그리고 거대한 시스템을 설계하는 데 능숙한 당신! 🏛️",
        "jobs": [
            {"name": "💻 AI 연구원 / 데이터 과학자", "reason": "복잡한 패턴을 분석하고 미래를 예측하는 일에 완벽해요!"},
            {"name": "🏗️ 시스템 아키텍트", "reason": "거대하고 효율적인 IT 인프라를 직접 설계합니다."},
            {"name": "📈 투자분석가 (퀀트)", "reason": "철저한 논리와 데이터로 시장의 흐름을 지배해요."}
        ],
        "other_jobs": [
            {"name": "🔐 사이버 보안 전략가", "icon": "🛡️", "summary": "최첨단 보안 시스템을 기획하고 사이버 위협을 방어합니다.", "detail": "시스템의 허점을 미리 파악하고 안전한 네트워크망을 구축하는 직업입니다. 높은 분석력과 논리적 사고가 필수예요!", "tag": "IT/보안"},
            {"name": "🎓 대학교수 / 연구원", "icon": "📚", "summary": "자신이 관심 있는 전문 분야를 끝까지 탐구하고 가르칩니다.", "detail": "깊이 있는 지식 탐구와 지적 독립성을 선호하는 INTJ에게 최적의 학문적 환경을 제공합니다.", "tag": "교육/학문"},
            {"name": "🧬 바이오 공학자", "icon": "🔬", "summary": "생명공학기술을 활용해 신약이나 치료법을 개발합니다.", "detail": "미래 기술을 바탕으로 인류의 삶을 개선하는 거대한 프로젝트를 이끌어갈 수 있습니다.", "tag": "과학/의학"}
        ],
        "tip": "💡 **성장 팁:** 혼자 일하는 것도 좋지만, 팀원들과 적극적으로 소통하는 법도 익혀보세요!"
    },
    "INTP": {
        "title": "🧪 아이디어 파판 아이디어상 (INTP)",
        "desc": "호기심이 넘쳐나고 끝없는 지적 호기심을 가진 아이디어 천재! 💡",
        "jobs": [
            {"name": "🔬 이론 물리학자 / 연구원", "reason": "세상의 비밀을 파헤치고 새로운 이론을 정립합니다."},
            {"name": "⚙️ 백엔드 개발자", "reason": "보이지 않는 알고리즘과 논리 구조를 만드는 데 최적!"},
            {"name": "🧩 게임 디자이너", "reason": "독창적이고 복잡한 세계관과 시스템을 창조해요."}
        ],
        "other_jobs": [
            {"name": "🤖 로봇 공학자", "icon": "🤖", "summary": "지능형 로봇의 제어 알고리즘과 작동 원리를 연구합니다.", "detail": "새로운 문제 해결 방식을 고민하고 복잡한 원리를 실험하는 과정을 매우 즐겁게 수행할 수 있습니다.", "tag": "공학/IT"},
            {"name": "📊 통계학자", "icon": "📉", "summary": "방대한 데이터 속에서 숨겨진 패턴과 원리를 밝혀냅니다.", "detail": "수학적 수수께끼를 풀듯 현실 데이터의 원인을 분석하는 지적 탐구 직업입니다.", "tag": "데이터"},
            {"name": "✍️ 철학자 / 칼럼니스트", "icon": "✒️", "summary": "세상과 인간의 본질에 대해 깊이 고찰하고 글을 씁니다.", "detail": "독창적인 관점으로 세상을 분석하고 비판적 사고를 글로 펼쳐낼 수 있습니다.", "tag": "인문/글쓰기"}
        ],
        "tip": "💡 **성장 팁:** 반짝이는 아이디어를 내는 것만큼 끝까지 완성해내는 집념도 보여주세요!"
    },
    "ENTJ": {
        "title": "👑 대담한 통솔자 (ENTJ)",
        "desc": "비전을 제시하고 목표를 향해 무섭게 돌진하는 비전 리더! 🚀",
        "jobs": [
            {"name": "💼 전문 경영인 (CEO)", "reason": "조직을 이끌고 단과 성과를 만들어내는 데 타고났어요."},
            {"name": "📊 경영 컨설턴트", "reason": "기업의 문제를 비판적으로 분석하고 솔루션을 제공합니다."},
            {"name": "⚖️ 변호사 / 법조인", "reason": "논리적인 설득과 주도권 싸움에서 압도적인 능력을 발휘해요."}
        ],
        "other_jobs": [
            {"name": "🏙️ 도시 계획가", "icon": "🏙️", "summary": "미래 도시의 구조와 발전 방향을 대규모로 기획합니다.", "detail": "장기적인 비전을 설정하고 복잡한 이해관계를 조정하여 효율적인 공간을 만듭니다.", "tag": "기획/건축"},
            {"name": "🎬 영화 감독 / 제작자", "icon": "🎥", "summary": "수많은 스태프와 배우를 지휘하여 대작 영화를 완성합니다.", "detail": "자신의 비전을 현실로 구현하기 위해 팀을 강력하게 리드하는 매력적인 직업입니다.", "tag": "엔터테인먼트"},
            {"name": "📢 Venture Capitalist (투자심사역)", "icon": "💎", "summary": "유망한 스타트업을 발굴하고 대대적인 투자를 집행합니다.", "detail": "시장 분석력과 비즈니스 통찰력을 살려 미래 혁신 기업을 육성합니다.", "tag": "금융/투자"}
        ],
        "tip": "💡 **성장 팁:** 목표 달성도 좋지만, 함께 달리는 동료들의 감정과 마음도 챙겨주세요!"
    },
    "ENTP": {
        "title": "⚡ 뜨거운 논쟁을 즐기는 변론가 (ENTP)",
        "desc": "고정관념을 깨부수고 끊임없이 새로운 도전을 즐기는 혁신가! 💥",
        "jobs": [
            {"name": "🚀 스타트업 창업가", "reason": "남들이 생각지 못한 새로운 시장을 개척합니다."},
            {"name": "📢 마케팅 기획자", "reason": "통쾌하고 참신한 캠페인으로 사람들의 시선을 사로잡아요."},
            {"name": "🎬 방송 PD / 유튜버", "reason": "지루할 틈 없는 흥미진진한 콘텐츠를 기획합니다."}
        ],
        "other_jobs": [
            {"name": "💡 크리에이티브 디렉터", "icon": "🎨", "summary": "브랜드의 파격적이고 독창적인 콘셉트를 전반적으로 총괄합니다.", "detail": "새로운 시도와 기발한 아이디어로 대중들에게 강렬한 영감을 선사합니다.", "tag": "디자인/광고"},
            {"name": "🎙️ 정치인 / 시사 평론가", "icon": "🎤", "summary": "사회적 이슈에 대해 논리적으로 토론하고 대안을 제시합니다.", "detail": "말싸움과 논리 대결에서 우위를 점하며 사회의 변화를 이끄는 도전적인 역할입니다.", "tag": "정치/언론"},
            {"name": "🌐 신사업 개발자 (BDM)", "icon": "🗺️", "summary": "기존에 없던 완전히 새로운 비즈니스 모델을 기획하고 실험합니다.", "detail": "모험적인 시도를 두려워하지 않고 과감하게 판을 벌이는 ENTP에게 최적입니다.", "tag": "비즈니스"}
        ],
        "tip": "💡 **성장 팁:** 시작한 일을 중간에 팽개치지 않도록 마무리까지 집중해 보세요!"
    },
    "INFJ": {
        "title": "🔮 통찰력 있는 선의의 옹호자 (INFJ)",
        "desc": "깊은 통찰력으로 세상을 더 좋게 만들고자 하는 따뜻한 이상가! 🌟",
        "jobs": [
            {"name": "🧠 심리상담사", "reason": "타인의 아픔을 깊이 공감하고 마음을 치유해 줍니다."},
            {"name": "✍️ 작가 / 시인", "reason": "글을 통해 깊은 사색과 메시지를 세상에 전합니다."},
            {"name": "🌿 환경 및 사회운동가", "reason": "더 나은 사회를 만들기 위한 가치 있는 일에 열정을 쏟아요."}
        ],
        "other_jobs": [
            {"name": "🎨 아트 테라피스트 (미술치료사)", "icon": "🖌️", "summary": "예술 활동을 통해 사람들의 마음속 상처를 보듬습니다.", "detail": "직관력과 공감 능력을 결합하여 사람들의 정서적 안정을 돕는 신기한 직업입니다.", "tag": "상담/치료"},
            {"name": "📚 도서관 사서 / 큐레이터", "icon": "📖", "summary": "지식과 문화 콘텐츠를 수집하고 조용한 가치를 나눕니다.", "detail": "조용하고 차분한 환경에서 사람들에게 영감을 주는 문헌과 예술을 전달합니다.", "tag": "문화/지식"},
            {"name": "🕊️ 인권 활동가", "icon": "🤝", "summary": "소외된 사람들의 목소리를 대변하고 신념을 실천합니다.", "detail": "자신의 강한 도덕적 신념과 이상을 실현할 수 있는 가치 중심의 직업입니다.", "tag": "사회공헌"}
        ],
        "tip": "💡 **성장 팁:** 남을 돕는 것도 좋지만, 자신의 에너지가 방전되지 않게 스스로도 챙기세요!"
    },
    "INFP": {
        "title": "🎨 열정적인 중재자 (INFP)",
        "desc": "풍부한 감수성과 나만의 독창적인 예술 세계를 품은 꿈꾸는 사람! 🌈",
        "jobs": [
            {"name": "🎨 일러스트레이터 / 웹툰 작가", "reason": "머릿속의 아름다운 상상력을 시각적으로 표현해요."},
            {"name": "🎵 음악 프로듀서 / 작곡가", "reason": "감성을 자극하는 아름다운 선율과 가사를 만듭니다."},
            {"name": "📚 출판 기획자 / 에디터", "reason": "좋은 글을 발굴하고 한 권의 아름다운 책으로 엮어냅니다."}
        ],
        "other_jobs": [
            {"name": "🎬 애니메이터", "icon": "🎞️", "summary": "캐릭터에 생명력을 불어넣고 따뜻한 스토리를 만듭니다.", "detail": "풍부한 상상력과 서사적인 스토리텔링 감각을 마음껏 발휘할 수 있는 분야입니다.", "tag": "영상/미디어"},
            {"name": "🌱 조경 디자이너", "icon": "🪴", "summary": "자연과 인간이 어우러지는 아름다운 정원과 공원을 꾸밉니다.", "detail": "자연을 사랑하고 아름다움을 추구하는 감성적인 마음을 공간으로 실현합니다.", "tag": "디자인/자연"},
            {"name": "🐾 동물 행동 교정사", "icon": "🐶", "summary": "말 없는 동물의 마음을 이해하고 행동을 교정해 줍니다.", "detail": "깊은 공감 능력과 인내심으로 동물과 보호자 사이의 교감을 돕습니다.", "tag": "동물/복지"}
        ],
        "tip": "💡 **성장 팁:** 현실적인 계획과 실행력을 조금만 더하면 꿈을 현실로 쉽게 만들 수 있어요!"
    },
    "ENFJ": {
        "title": "🌟 정의로운 주인공 (ENFJ)",
        "desc": "선한 영향력으로 주변 사람들의 잠재력을 끌어내는 따뜻한 리더! 🤝",
        "jobs": [
            {"name": "🏫 교육자 / 교사", "reason": "학생들에게 영감을 주고 성장하는 과정을 함께합니다."},
            {"name": "📢 PR 및 홍보 전문가", "reason": "선한 가치와 브랜드를 세상에 진정성 있게 전달해요."},
            {"name": "🤝 HR (인사) 담당자", "reason": "사람들의 적성을 찾고 올바른 길로 안내해 줍니다."}
        ],
        "other_jobs": [
            {"name": "🎙️ 아나운서 / 리포터", "icon": "📻", "summary": "진정성 있는 목소리로 소식과 감동을 사람들에게 전합니다.", "detail": "우수한 소통 능력과 대중을 끌어당기는 매력으로 신뢰감을 줍니다.", "tag": "방송/언론"},
            {"name": "🏃 라이프 코치 (동기부여가)", "icon": "🔥", "summary": "사람들의 목표 달성과 인생의 긍정적 변화를 이끌어 줍니다.", "detail": "상대방의 가능성을 누구보다 잘 찾아내고 진심 어린 응원을 보낼 수 있습니다.", "tag": "코칭/자기계발"},
            {"name": "🏥 보건 행정 전문가", "icon": "🩺", "summary": "지역사회의 건강과 복지 향상을 위해 정책을 세웁니다.", "detail": "공공의 유익과 사람들의 삶의 질 향상을 도모하는 가람 직무입니다.", "tag": "의료/행정"}
        ],
        "tip": "💡 **성장 팁:** 모든 사람을 다 만족시킬 수는 없어요. 때로는 정중하게 거절하는 법도 배워보세요!"
    },
    "ENFP": {
        "title": "🎉 재기발랄한 활동가 (ENFP)",
        "desc": "에너지가 넘치고 매 순간 인생의 즐거움을 찾아 떠나는 모험가! 🎈",
        "jobs": [
            {"name": "🎨 크리에이티브 디렉터", "reason": "통통 튀는 아이디어로 새로운 컨셉을 연출합니다."},
            {"name": "✈️ 여행 기획자 / 가이드", "reason": "전 세계를 누비며 사람들에게 잊지 못할 추억을 선물해요."},
            {"name": "🎪 행사 및 축제 기획자", "reason": "모두가 신나게 즐길 수 있는 유쾌한 장을 만듭니다."}
        ],
        "other_jobs": [
            {"name": "🎭 뮤지컬 배우 / 연기자", "icon": "💃", "summary": "무대 위에서 다양한 무대 장치와 음악 속에서 감정을 분출합니다.", "detail": "사람들과 호흡하며 폭발적인 열정과 예술적 감성을 나눌 수 있는 최고 무대입니다.", "tag": "공연/예술"},
            {"name": "🛍️ 팝업스토어 기획자", "icon": "🎁", "summary": "짧은 기간 동안 강렬한 경험을 선사하는 트렌디한 공간을 만듭니다.", "detail": "트렌드에 민감하고 흥미진진한 체험 요소를 다채롭게 구상해 냅니다.", "tag": "마케팅/공간"},
            {"name": "📻 팟캐스트 / 라디오 진행자", "icon": "🎧", "summary": "솔직하고 유쾌한 입담으로 입체적인 청취자 팬덤을 구축합니다.", "detail": "사람들과 이야기 나누기를 좋아하는 ENFP의 친근함이 가장 잘 드러납니다.", "tag": "미디어"}
        ],
        "tip": "💡 **성장 팁:** 흥미가 쉽게 식지 않도록 큰 목표를 작은 단위로 나누어 실행해 보세요!"
    },
    "ISTJ": {
        "title": "🛡️ 청렴결백한 논리주의자 (ISTJ)",
        "desc": "신뢰성 100%! 매사에 철저하고 책임감이 강한 완벽주의자! 📐",
        "jobs": [
            {"name": "📑 회계사 / 세무사", "reason": "숫자 하나 틀리지 않는 꼼꼼함으로 자산을 관리합니다."},
            {"name": "🏛️ 공무원 / 행정가", "reason": "법과 규칙을 준수하며 사회의 질서를 유지해요."},
            {"name": "🔍 데이터 품질 관리자", "reason": "티끌 하나 없는 데이터의 정확성을 완벽하게 보장합니다."}
        ],
        "other_jobs": [
            {"name": "📦 Supply Chain Manager (물류관리사)", "icon": "🚚", "summary": "원자재 입고부터 제품 배송까지 체계적 흐름을 총괄합니다.", "detail": "치밀한 계획 수립과 프로세스 관리를 통해 지연 없는 최적의 시스템을 구축합니다.", "tag": "물류/운영"},
            {"name": "⚖️ 법무 담당자 (Compliance Officer)", "icon": "📜", "summary": "기업의 모든 활동이 법률과 규정에 맞는지 감독합니다.", "detail": "원칙과 정직함을 바탕으로 조직을 위험으로부터 철저히 보호하는 파수꾼입니다.", "tag": "법률/기업"},
            {"name": "🔬 품질 보증 엔지니어 (QA)", "icon": "🔍", "summary": "제품 출시 전 엄격한 테스트를 거쳐 불량을 잡아냅니다.", "detail": "디테일 하나 놓치지 않는 세심함으로 완벽한 품질 기준을 지켜냅니다.", "tag": "IT/제조"}
        ],
        "tip": "💡 **성장 팁:** 때로는 예외 상황을 인정하는 유연함과 새로운 방식에 마음을 열어보세요!"
    },
    "ISFJ": {
        "title": "💐 용감한 수호자 (ISFJ)",
        "desc": "소중한 사람들을 따뜻하게 지키고 묵묵히 헌신하는 세심한 가디언! 🕊️",
        "jobs": [
            {"name": "🩺 간호사 / 의료진", "reason": "따뜻한 손길로 환자들을 세심하게 돌봅니다."},
            {"name": "🧸 유치원 교사 / 보육교사", "reason": "아이들에게 무한한 사랑과 안전한 환경을 제공해요."},
            {"name": "💼 비서 / 행정 지원가", "reason": "보이지 않는 곳에서 완벽하게 업무를 지원합니다."}
        ],
        "other_jobs": [
            {"name": "🍰 파티시에 / 베이커", "icon": "🧁", "summary": "정성스러운 정량 계량과 손길로 달콤한 빵을 만듭니다.", "detail": "정확한 레시피 준수와 사람들에게 작은 행복을 선물한다는 보람이 함께합니다.", "tag": "요리/제과"},
            {"name": "🏛️ 박물관 학예사 (큐레이터)", "icon": "🖼️", "summary": "역사적 유물과 작품을 안전하게 보존하고 관리합니다.", "detail": "소중한 전통과 기록을 온전히 보존하고 설명하는 데 큰 보람을 느낍니다.", "tag": "역사/문화"},
            {"name": "💊 약사", "icon": "💊", "summary": "정확한 처방과 친절한 복약 지도 및 건강 케어를 제공합니다.", "detail": "꼼꼼한 주의력과 이웃에 대한 따뜻한 케어가 조화를 이루는 안정적 직업입니다.", "tag": "의학/보건"}
        ],
        "tip": "💡 **성장 팁:** 자신의 욕구와 원하는 바를 솔직하게 표현하는 연습도 꼭 필요해요!"
    },
    "ESTJ": {
        "title": "📊 엄격한 관리자 (ESTJ)",
        "desc": "체계적인 규칙과 질서를 바탕으로 조직을 완벽히 이끄는 효율 전문가! 🏛️",
        "jobs": [
            {"name": "🏭 프로젝트 매니저 (PM)", "reason": "일정과 자원을 차질 없이 완벽하게 관리합니다."},
            {"name": "👮 경찰 / 군인", "reason": "투철한 사명감으로 법과 사회 질서를 수호해요."},
            {"name": "🏢 지점장 / 운영 이사", "reason": "조직의 효율성을 극대화하여 최고의 성과를 냅니다."}
        ],
        "other_jobs": [
            {"name": "📊 펀드 매니저", "icon": "💵", "summary": "철저한 위험 분석과 신속한 결정으로 자산을 운영합니다.", "detail": "명확한 데이터 분석과 논리적인 시장 판단을 기반으로 성과를 창출합니다.", "tag": "금융/투자"},
            {"name": "🏗️ 건설 현장 소장", "icon": "👷", "summary": "대규모 공사 현장의 안전과 작업 공정을 총괄 감독합니다.", "detail": "현장의 많은 인력을 기강 있게 리드하고 정해진 기한 내 안전하게 건축을 완수합니다.", "tag": "건설/엔지니어링"},
            {"name": "✈️ 항공기 기장 (파일럿)", "icon": "✈️", "summary": "철저한 매뉴얼을 준수하며 승객의 안전한 비행을 책임집니다.", "detail": "비상 상황 시 단호하고 신속한 결정 능력과 규율 준수 태도가 빛을 발합니다.", "tag": "항공/운송"}
        ],
        "tip": "💡 **성장 팁:** 타인의 감정적 상황이나 개성을 배려하는 너그러움을 더해보세요!"
    },
    "ESFJ": {
        "title": "🤝 사교적인 외교관 (ESFJ)",
        "desc": "친절과 친화력으로 분위기를 화기애애하게 만드는 분위기 메이커! 🌸",
        "jobs": [
            {"name": "🛎️ 호텔 지배인 / 서비스 전문가", "reason": "고객에게 최상의 친절과 감동을 선사합니다."},
            {"name": "📋 이벤트 코디네이터", "reason": "사람들의 관계를 모으고 따뜻한 모임을 조율해요."},
            {"name": "🩺 병원 코디네이터", "reason": "환자들에게 편안함을 주고 원활한 소통을 돕습니다."}
        ],
        "other_jobs": [
            {"name": "✈️ 객실 승무원 (스튜어디스)", "icon": "🛫", "summary": "비행 중 승객의 안전과 쾌적한 서비스를 친절히 담당합니다.", "detail": "다양한 사람들을 밝은 미소로 맞이하고 상호 협력하는 분위기를 만듭니다.", "tag": "항공/서비스"},
            {"name": "🏫 초등학교 교사", "icon": "🎒", "summary": "어린이들의 기본 생활 습관과 바른 성장을 온화하게 지도합니다.", "detail": "따뜻한 공동체 의식을 함양하고 아이들의 사소한 변화도 진심으로 챙겨줍니다.", "tag": "교육"},
            {"name": "🏡 리얼터 (부동산 중개사)", "icon": "🔑", "summary": "고객의 니즈에 딱 맞는 따뜻한 안식처를 연결해 줍니다.", "detail": "우수한 친화력과 신뢰를 바탕으로 사람 간의 거래를 완벽하게 조율합니다.", "tag": "영업/중개"}
        ],
        "tip": "💡 **성장 팁:** 남의 비판에 너무 깊게 상처받지 말고 객관적으로 바라보세요!"
    },
    "ISTP": {
        "title": "🛠️ 만능 재주꾼 (ISTP)",
        "desc": "도구와 기계를 잘 다루며 냉철한 이성으로 문제를 해결하는 해결사! 🔧",
        "jobs": [
            {"name": "🏎️ 카레이서 / 카메카닉", "reason": "순발력과 담력으로 스릴 넘치는 기계를 다룹니다."},
            {"name": "💻 사이버 침투 대응 전문가", "reason": "시스템의 허점을 파악하고 날카롭게 문제를 해결합니다."},
            {"name": "🛠️ 메카트로닉스 엔지니어", "reason": "복잡한 기계의 원리를 파악하고 수리하는 데 타고났어요."}
        ],
        "other_jobs": [
            {"name": "🛩️ 드론 조종 전문가", "icon": "🚁", "summary": "정밀한 기계 조작으로 촬영, 조사, 물류를 수행합니다.", "detail": "최신 기술 장비를 능숙하게 조작하고 기계적 원리를 파악하는 흥미로운 직업입니다.", "tag": "기술/항공"},
            {"name": "🕵️ 사설 탐정 / 조사관", "icon": "🔍", "summary": "현장의 증거를 냉철히 수집하고 사건의 진실을 추적합니다.", "detail": "관찰력이 뛰어난 ISTP가 직접 발로 뛰며 논리적 추론을 펼칠 수 있습니다.", "tag": "조사/안전"},
            {"name": "💉 응급구조사 (EMT)", "icon": "🚑", "summary": "긴급한 현장에서 신속하고 임기응변으로 구급 처치를 합니다.", "detail": "위기 상황에서도 당황하지 않고 냉정하게 즉각 조치하는 능력이 뛰어납니다.", "tag": "의료/구조"}
        ],
        "tip": "💡 **성장 팁:** 긴급 상황이 아니더라도 평소에 주변 사람들과 소통하는 습관을 가져보세요!"
    },
    "ISFP": {
        "title": "🎨 호기심 많은 예술가 (ISFP)",
        "desc": "현재의 순간을 즐기며 삶을 아름답고 감각적으로 표현하는 감성파! 🌿",
        "jobs": [
            {"name": "💄 메이크업 아티스트 / 스타일리스트", "reason": "남다른 미적 감각으로 사람을 아름답게 꾸며줍니다."},
            {"name": "📷 사진작가 (포토그래퍼)", "reason": "찰나의 순간에 담긴 아름다움을 카메라로 담아내요."},
            {"name": "🪴 플로리스트 / 가드너", "reason": "자연의 아름다움을 살려 감성적인 공간을 연출합니다."}
        ],
        "other_jobs": [
            {"name": "👗 패션 디자이너", "icon": "🧵", "summary": "원단과 색상을 조화롭게 조합해 아름다운 옷을 만듭니다.", "detail": "나만의 개성과 트렌디한 시각을 의상이라는 매개체로 유연하게 풀어냅니다.", "tag": "패션/예술"},
            {"name": "🛋️ 인테리어 디자이너", "icon": "🛋️", "summary": "사람들이 머무는 공간을 감각적이고 편안하게 코디합니다.", "detail": "시각적 디테일과 따뜻한 감성이 어우러져 공간을 매력적으로 변신시킵니다.", "tag": "디자인/공간"},
            {"name": "🐾 애견 미용사 (애완동물 스타일리스트)", "icon": "✂️", "summary": "반려동물을 안전하고 예쁘게 가꾸어 줍니다.", "detail": "동물에 대한 애정과 손재주를 살려 온화하게 작업할 수 있습니다.", "tag": "동물/미용"}
        ],
        "tip": "💡 **성장 팁:** 중요한 결정을 자꾸 미루기보다 가끔은 담대하게 실행해 보세요!"
    },
    "ESTP": {
        "title": "🏄 모험을 즐기는 사업가 (ESTP)",
        "desc": "스릴과 액션을 좋아하며 온몸으로 문제에 부딪히는 에너지왕! ⚡",
        "jobs": [
            {"name": "📈 트레이더 / 자산관리사", "reason": "순간적인 판단력으로 위험을 관리하고 과감히 투자합니다."},
            {"name": "🚨 소방관 / 특수구조대", "reason": "위급한 현장에서 빛나는 위기 관리 능력과 순발력을 발휘해요."},
            {"name": "⚽ 스포츠 코치 / 에이전트", "reason": "역동적인 활동을 통해 사람들에게 에너지를 전달합니다."}
        ],
        "other_jobs": [
            {"name": "🏗️ 부동산 개발업자 (디벨로퍼)", "icon": "🏙️", "summary": "가치 있는 땅을 발굴하여 과감한 투자와 개발을 주도합니다.", "detail": "위험을 두려워하지 않는 대담성과 탁월한 비즈니스 협상 능력을 요구합니다.", "tag": "부동산/사업"},
            {"name": "🎥 익스트림 스포츠 촬영 감독", "icon": "📹", "summary": "위험천만한 스포츠 현장을 역동적으로 카메라에 담아냅니다.", "detail": "몸을 아끼지 않는 행동력과 순간적인 피사체 포착 감각이 매우 뛰어납니다.", "tag": "미디어/액션"},
            {"name": "📢 펀딩 매니저 / 영업 이사", "icon": "🤝", "summary": "직접 사람을 만나 현장에서 설득하고 빠른 시일 내 계약을 맺습니다.", "detail": "뛰어난 순발력과 인간적인 매력으로 현장 계약 성공률이 극대화됩니다.", "tag": "영업/마케팅"}
        ],
        "tip": "💡 **성장 팁:** 충동적인 결정 대신 장기적인 계획을 세우는 습관을 들여보세요!"
    },
    "ESFP": {
        "title": "🎤 자유로운 영혼의 연예인 (ESFP)",
        "desc": "가는 곳마다 풍성한 즐거움을 선사하며 무대를 지배하는 슈퍼스타! 🌟",
        "jobs": [
            {"name": "🎭 배우 / 뮤지컬 배우", "reason": "넘치는 끼와 감정 표현으로 무대 위에서 빛을 발합니다."},
            {"name": "🎈 레크리에이션 강사", "reason": "유쾌한 에너지로 사람들에게 웃음과 행복을 줍니다."},
            {"name": "🛍️ 쇼호스트 / 패션 크리에이터", "reason": "화려한 입담과 매력으로 상품을 매력적으로 어필해요."}
        ],
        "other_jobs": [
            {"name": "🎈 테마파크 공연 연출가", "icon": "🎡", "summary": "꿈과 환상의 퍼레이드와 이벤트를 신나게 기획합니다.", "detail": "사람들에게 오락적 즐거움과 생동감을 선사하며 함께 축제 분위기를 만듭니다.", "tag": "공연/이벤트"},
            {"name": "✈️ 크루즈 승무원 / 메인 호스트", "icon": "🚢", "summary": "화려한 크루즈 여행 선상에서 승객들의 엔터테인먼트를 담당합니다.", "detail": "세계 곳곳을 여행하며 다양한 사람들과 매일 즐거운 파티를 엽니다.", "tag": "관광/서비스"},
            {"name": "🐶 동물 매개 치료사", "icon": "🐕", "summary": "귀여운 동물과 함께 마음이 아픈 사람들을 활력 있게 치료합니다.", "detail": "밝은 에너지와 친근함으로 피치못할 슬픔을 따뜻한 웃음으로 치유해 줍니다.", "tag": "복지/치료"}
        ],
        "tip": "💡 **성장 팁:** 즐거움 뒤에 오는 행정적이고 단순 반복적인 업무도 차분하게 처리해 보세요!"
    }
}

# 4. 헤더 및 로고 영역
st.markdown('<div class="main-title">🚀✨ MBTI 꿈의 직업 탐험대 ✨🚀</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">🔮 나의 성격 유형에 딱 맞는 운명적인 미래 직업을 탐색해보세요! 🔮</div>', unsafe_allow_html=True)

# 5. 사이드바 구성
st.sidebar.header("🎯 **내 성격 유형 선택하기**")
selected_mbti = st.sidebar.selectbox(
    "👉 아래에서 당신의 MBTI를 골라주세요!",
    list(mbti_db.keys()),
    index=0
)

st.sidebar.markdown("---")
st.sidebar.write("🎁 **효과 설정**")
show_animation = st.sidebar.checkbox("🎉 결과 검색 시 축하 폭죽 터뜨리기", value=True)

# 6. 메인 탐색 로직
mbti_info = mbti_db[selected_mbti]

# 검색 버튼
if st.button(f"🔍 {selected_mbti} 추천 직업 및 서브 탭 탐색하기!", use_container_width=True):
    if show_animation:
        st.balloons()
        st.snow()
    
    with st.spinner("🔮 당신의 성격 데이터베이스와 미래 직업을 매칭하는 중입니다..."):
        time.sleep(0.4)

st.markdown("---")
st.markdown(f"## {mbti_info['title']}")
st.info(f"✨ **성격 요약:** {mbti_info['desc']}")

# 7. 하위 탭 구성 (Tab 1: BEST 3 대표 직업 | Tab 2: 기타 추천 직업 클릭 탐색 | Tab 3: 진로 성장 꿀팁)
tab1, tab2, tab3 = st.tabs([
    "🏆 BEST 3 대표 직업", 
    "📂 기타 직업 상세 탐색 (클릭!)", 
    "💡 진로 성장 가이드"
])

# ----- Tab 1: 대표 추천 직업 3가지 -----
with tab1:
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("### 💼 **당신을 가장 빛나게 해 줄 핵심 직업 3가지**")
    cols = st.columns(3)
    
    for idx, job in enumerate(mbti_info["jobs"]):
        with cols[idx]:
            st.markdown(f"""
                <div class="job-card">
                    <h3 style="color: #6C5CE7; margin-top:0;">{job['name']}</h3>
                    <hr>
                    <p style="font-size: 0.95rem;"><b>🔍 추천 이유:</b></p>
                    <p style="color: #444; font-size: 0.95rem;">{job['reason']}</p>
                </div>
            """, unsafe_allow_html=True)

# ----- Tab 2: 기타 직업 클릭 시 상세 설명 팝업/아코디언 -----
with tab2:
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("### 🔍 **클릭하면 상세 설명이 펼쳐지는 기타 추천 직업 목록!**")
    st.caption("👇 관심 있는 직업 항목을 클릭하면 어떤 일을 하는지 세부 정보가 나옵니다.")

    for item in mbti_info["other_jobs"]:
        # expander를 활용하여 클릭 시 직업 설명이 나타나도록 구현
        with st.expander(f"{item['icon']} **{item['name']}**  |  🏷️ {item['tag']}"):
            col_a, col_b = st.columns([1, 4])
            with col_a:
                st.markdown(f"<h1 style='text-align: center;'>{item['icon']}</h1>", unsafe_allow_html=True)
            with col_b:
                st.markdown(f"#### **{item['name']}**")
                st.markdown(f"📌 **한 줄 요약:** {item['summary']}")
                st.markdown(f"📖 **상세 직업 설명:** {item['detail']}")
                st.markdown(f"🎯 **분류 카테고리:** `{item['tag']}`")

# ----- Tab 3: 진로 성장 가이드 -----
with tab3:
    st.markdown("<br>", unsafe_allow_html=True)
    st.success(mbti_info['tip'])
    
    st.markdown("""
        #### 🌈 **선생님이 전하는 미래 진로 조언**
        1. **MBTI는 가이드북일 뿐이에요!** 모든 것을 결정짓는 절대적인 기준은 아니랍니다.
        2. **다양한 경험을 해보세요:** 흥미가 가는 일은 직접 체험해보거나 관련 책을 읽어보는 것이 최고의 진로 교육입니다.
        3. **자신만의 강점을 키우세요:** 당신이 좋아하는 일과 잘하는 일의 접점을 찾으면 행복한 직업을 가질 수 있어요!
    """)

# 8. 푸터
st.markdown("<br><br><br>", unsafe_allow_html=True)
st.markdown(
    "<div style='text-align: center; color: #666; font-size: 0.85rem;'>💖 진로 교육용 Streamlit 웹앱 | 청소년의 꿈을 응원합니다 💖</div>", 
    unsafe_allow_html=True
)
```eof

The updated Streamlit app code has been generated with:
- **Sub-tabs (`st.tabs`)**: Separating core recommendations, additional interactive jobs, and career development tips.
- **Clickable Extra Jobs (`st.expander`)**: Users can click any secondary career to view a detailed popup card featuring summaries, deep descriptions, and category tags.
- **Colorful Visual Styling**: Expanded emojis, color badges, balloons, and gradient cards for an engaging student experience.
