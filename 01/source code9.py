# API KEY를 환경변수로 관리하기 위한 설정 파일
from dotenv import load_dotenv

# API KEY 정보 로드
load_dotenv()

from langchain.prompts import PromptTemplate

# template 정의
template = "{country}의 수도는 어디인가요?"

# from_template 메소드를 이용하여 PromptTemplate 객체 생성
prompt_template = PromptTemplate.from_template(template)
#print(prompt_template)

from langchain_openai import ChatOpenAI

model = ChatOpenAI(
    model="gpt-3.5-turbo",
    max_tokens=2048,
    temperature=0.1,
)

from langchain_core.output_parsers import StrOutputParser

output_parser = StrOutputParser()

chain = prompt_template | model | output_parser

print(chain.invoke({"country": "대한민국"}))