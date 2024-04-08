# API KEY를 환경변수로 관리하기 위한 설정 파일
from dotenv import load_dotenv
load_dotenv()
# 오픈ai 사용가능한 랭체인 임포트
from langchain_openai import ChatOpenAI
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler

# 객체 생성
llm = ChatOpenAI(
    temperature=0.1, # 창의성(0.0 ~ 2.0)
    max_tokens=2048, # 최대 토큰수
    model_name="gpt-3.5-turbo", # 모델명
    streaming=True,
    callbacks=[StreamingStdOutCallbackHandler()],
)

# 질의내용
question = "대한민국에 대해서 300자 내외로 최대한 상세히 알려줘"

# 스트리밍으로 답변 출력
response = llm.invoke(question)