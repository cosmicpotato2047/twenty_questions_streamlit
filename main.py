import streamlit as st
from ollama_llm import get_ollama_llm

# 시스템 프롬프트 정의
SYSTEM_PROMPT = '''
You are playing a game of Twenty Questions. Think of an English noun. Ask yes/no questions to guess the noun within 20 questions. When you're ready to guess, ask in the form "Is it a [object]?".
'''

# 입력 처리 콜백
def handle_answer():
    ans = st.session_state.input.strip().lower()
    # 입력 초기화
    st.session_state.input = ''
    # 유효 답변 목록
    valid = ['yes', 'no', "i don't know", 'it depends', 'quit']
    if ans not in valid:
        # 오류 메시지를 히스토리에 추가하여 표시
        st.session_state.history.append({'role': 'assistant', 'content':
            "유효하지 않은 답변입니다. yes, no, I don’t know, it depends 중 하나로 다시 입력해 주세요."})
        return
    # 사용자 응답 기록
    st.session_state.history.append({'role': 'user', 'content': ans})
    last_q = st.session_state.history[-2]['content'].lower()
    # 종료 처리
    if ans == 'quit':
        st.session_state.history.append({'role': 'assistant', 'content': '게임을 종료합니다.'})
        st.session_state.game_over = True
        return
    if last_q.startswith('is it'):
        if ans == 'yes':
            st.session_state.history.append({'role': 'assistant', 'content': 'AI 승리!'})
        else:
            st.session_state.history.append({'role': 'assistant', 'content': 'AI 패배!'})
        st.session_state.game_over = True
        return
    # 다음 질문 생성
    if st.session_state.count < 20:
        llm = get_ollama_llm()
        prompt = "".join([
            f"{m['role']}: {m['content']}\n" for m in st.session_state.history
        ]) + "AI:"
        result = llm.generate([prompt])
        question = result.generations[0][0].text.strip()
        st.session_state.history.append({'role': 'assistant', 'content': question})
        st.session_state.count += 1
    else:
        # 20번째 이후 자동 추측
        llm = get_ollama_llm()
        prompt = "".join([
            f"{m['role']}: {m['content']}\n" for m in st.session_state.history
        ]) + "AI:"
        result = llm.generate([prompt])
        guess = result.generations[0][0].text.strip()
        st.session_state.history.append({'role': 'assistant', 'content': guess})
        st.session_state.count += 1

# 세션 상태 초기화
if 'history' not in st.session_state:
    st.session_state.history = [{'role': 'system', 'content': SYSTEM_PROMPT}]
    st.session_state.count = 0
    st.session_state.game_over = False
    st.session_state.input = ''

st.title("🕵️‍♂️ 스무고개 게임")

# 게임 시작 버튼
if st.button("새 게임 시작"):
    st.session_state.history = [{'role': 'system', 'content': SYSTEM_PROMPT}]
    st.session_state.count = 0
    st.session_state.game_over = False
    # 첫 질문 생성
    llm = get_ollama_llm()
    prompt = "".join([
        f"{m['role']}: {m['content']}\n" for m in st.session_state.history
    ]) + "AI:"
    result = llm.generate([prompt])
    question = result.generations[0][0].text.strip()
    st.session_state.history.append({'role': 'assistant', 'content': question})
    st.session_state.count += 1

# 대화 히스토리 출력
for msg in st.session_state.history[1:]:  # 시스템 메시지는 제외
    if msg['role'] == 'assistant':
        st.chat_message('assistant').write(msg['content'])
    elif msg['role'] == 'user':
        st.chat_message('user').write(msg['content'])

# 사용자 입력 텍스트박스 (엔터로 제출)
st.text_input(
    "A) yes / no / I don't know / it depends",
    key='input',
    on_change=handle_answer,
    disabled=st.session_state.game_over
)