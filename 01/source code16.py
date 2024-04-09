# API KEY를 환경변수로 관리하기 위한 설정 파일
from dotenv import load_dotenv

# API KEY 정보로드
load_dotenv()

from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate

from langchain_core.runnables import RunnableParallel

model = ChatOpenAI()

# {country} 의 수도를 물어보는 체인을 생성한다.
chain1 = ChatPromptTemplate.from_template("{country} 의 수도는 어디야?") | model

# {country}의 면적을 물어보는 체인을 생상한다.
chain2 = ChatPromptTemplate.from_template("{country} 의 면적은 얼마야?") | model
# 위의 2개 체인을 동시에 생성하는 병렬 실행 체인을 생성한다.
combined = RunnableParallel(capital=chain1, area=chain2)

# chain1 객체의 invoke 메서드를 호출하고, 'country' 키에 '대한민국' 값을 전달한다.
#print(chain1.invoke({"country": "대한민국"}))

# chain2 객체의 invoke 메서드를 호출하고, '미국'이라는 인자를 전달한다.
#print(chain2.invoke({"country": "미국"}))

# 주어진 'country'에 대해 'combined' 객체의 'invoked' 메서드를 호출한다.
#print(combined.invoke({"country": "대한민국"}))

# 배치 처리를 수행한다.
#print(chain1.batch([{"country": "대한민국"}, {"country": "미국"}]))

# 배치 처리를 수행한다.
#print(chain2.batch([{"country": "대한민국"}, {"country": "미국"}]))

# 주어진 데이터를 배치 처리로 수행한다.
print(combined.batch([{"country": "대한민국"}, {"country": "미국"}]))