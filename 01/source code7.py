from langchain.prompts import PromptTemplate
# API KEY를 환경변수로 관리하기 위한 설정 파일
from dotenv import load_dotenv
load_dotenv()
# 오픈ai 사용가능한 랭체인 임포트
from langchain_openai import ChatOpenAI
from langchain.chains import LLMChain

# 질문 템플릿 형식 정의
template = "{area1} 와 {area2} 의 시차는 몇시간이야?"

# 객체 생성
llm = ChatOpenAI(
    temperature=0.1, # 창의성(0.0 ~ 2.0)
    max_tokens=2048, # 최대 토큰수
    model_name="gpt-3.5-turbo", # 모델명
)

# 템플릿 완성
prompt = PromptTemplate.from_template(template=template)
#print(prompt)

# 연결된 체인(Chain)객체 생성
llm_chain = LLMChain(prompt=prompt, llm=llm)

# 체인 실행: run()
print(llm_chain.invoke({"area1": "서울", "area2": "파리"}))

# 입력값
input_list = [
    {"area1": "파리", "area2": "뉴욕"},
    {"area1": "서울", "area2": "하와이"},
    {"area1": "켄버리", "area2": "베이징"},
]

# 반복문으로 결과 출력
result = llm_chain.apply(input_list)
for res in result:
    print(res["text"].strip())