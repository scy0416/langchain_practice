# API KEY를 환경변수로 관리하기 위한 설정 파일
from dotenv import load_dotenv

# API KEY 정보 로드
load_dotenv()

from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser

template = """
당신은 영어를 가르치는 10년차 영어 선생님입니다. 상황에 [FORMAT]에 영어 회화를 작성해 주세요.
답변은 항상 한글로 작성해 주세요.
답변은 3문장 이상으로 작성해주세요.

질문:
{question}

FORMAT:
- 영어 회화:
- 한글 해석:
"""

prompt = PromptTemplate.from_template(template)

# OpenAI 챗모델을 초기화한다.
model = ChatOpenAI(model="gpt-4-turbo-preview")
# 문자열 출력 파서를 초기화한다.
output_parser = StrOutputParser()

# 프롬프트, 모델, 출력 파서를 연결하여  처리 체인을 구성한다.
chain = prompt | model | output_parser

print(chain.invoke({"question": "저는 식당에 가서 음식을 주문하고 싶어요"}))
print(chain.invoke({"question": "미국에서 피자 주문"}))