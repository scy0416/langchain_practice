# API KEY를 환경변수로 관리하기 위한 설정 파일
from dotenv import load_dotenv

# API KEY 정보로드
load_dotenv()

from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate

# ChatOpenAI 모델을 인스턴스화 한다.
model = ChatOpenAI()
# 주어진 토픽에 대한 설명 3문장을 요청하는 프롬프트 템플릿을 정의한다.
prompt = ChatPromptTemplate.from_template("{topic} 에 대하여 3문장으로 설명해줘.")
# 프롬프트와 모델을 연결하여 대화 체인을 생성한다.
chain = prompt | model

# 체인의 입력 스키마는 첫 번째 부분인 프롬프트의 입력 스키마이다.
print(chain.input_schema.schema())