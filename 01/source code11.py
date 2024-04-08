# API KEY를 환경변수로 관리하기 위한 설정 파일
from dotenv import load_dotenv

# API KEY 정보 로드
load_dotenv()

from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser

# prompt 를 PromptTemplate 객체로 생성
prompt = PromptTemplate.from_template("{topic} 에 대해 쉽게 설명해주세요.")

# OpenAI 챗모델을 초기화한다.
model = ChatOpenAI(model="gpt-4-turbo-preview")
# 문자열 출력 파서를 초기화한다.
output_parser = StrOutputParser()

# input 딕셔너리에 주제를 '양자역학'으로 설정한다.
input = {"topic": "양자역학"}

# prompt 객체의 invoke 메서드를 사용하여 input을 전달하고 대화형 프롬프트 값을 생서한다.
#print(prompt.invoke(input))

# prompt 객체와 model 객체를 파이프(|) 연산자로 연결하고 invoke 메서드를 사용하여 input을 전달한다.
# 이를 통해 AI 모델이 생성한 메시지를 반환한다.
#print((prompt | model).invoke(input))

# parse_output 메서드를 사용하여 AI 모델이 생성한 메시지 문자열로 출력한다.
print((prompt | model | output_parser).invoke(input))