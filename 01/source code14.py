# API KEY를 환경변수로 관리하기 위한 설정 파일
from dotenv import load_dotenv

# API KEY 정보로드
load_dotenv()

from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate

import asyncio

# ChatOpenAI 모델을 인스턴스화 한다.
model = ChatOpenAI()
# 주어진 토픽에 대한 설명 3문장을 요청하는 프롬프트 템플릿을 정의한다.
prompt = ChatPromptTemplate.from_template("{topic} 에 대하여 3문장으로 설명해줘.")
# 프롬프트와 모델을 연결하여 대화 체인을 생성한다.
chain = prompt | model

# 체인의 입력 스키마는 첫 번째 부분인 프롬프트의 입력 스키마이다.
#print(chain.input_schema.schema())

# 모델의 입력 스키마를 출력한다.
#print(model.input_schema.schema())

# 체인의 출력 스키마는 마지막 부분의 출력 스키마이다. 이 경우 ChatModel의 출력 스키마로, ChatMessage를 출력한다.
#print(chain.output_schema.schema())

# chain.stream 메서드를 사용하여 '멀티모달' 토픽에 대한 스트림을 생성하고 반복한다.
'''
for s in chain.stream({"topic": "멀티모달"}):
    # 스트림에서 받은 데이터의 내용을 출력한다. 줄바꿈 없이 이어서 출력하고, 버퍼를 즉시 비운다.
    print(s.content, end="", flush=True)
'''

# chain 객체의 invoke 메서드를 호출하고, 'ChatGPT'라는 주제로 딕셔너리를 전달한다.
#print(chain.invoke({"topic": "ChatGPT"}))

# 주어진 토픽 리스트를 batch 처리하는 함수 호출
#print(chain.batch([{"topic": "ChatGPT"}, {"topic": "Instagram"}]))

'''
result = chain.batch(
    [
        {"topic": "ChatGPT"},
        {"topic": "Instagram"},
        {"topic": "멀티모달"},
        {"topic": "프로그래밍"},
        {"topic": "머신러닝"},
    ],
    config={"max_concurrency": 3},
)
print(result)
'''

'''
async def astream_test():
    # 비동기 스트림을 사용하여 'YouTube' 토픽의 메시지를 처리한다.
    async for s in chain.astream({"topic": "YouTube"}):
        # 메시지 내용을 출력한다. 줄바꿈 없이 바로 출력하고 버퍼를 비운다.
        print(s.content, end="", flush=True)
asyncio.run(astream_test())
'''

'''
async def ainvoke_test():
    # 비동기 체인 객체의 'ainvoke' 메서드를 호출하여 'NVDA' 토픽을 처리한다.
    result = await chain.ainvoke({"topic": "NVDA"})
    print(result)
asyncio.run(ainvoke_test())
'''

async def abatch_test():
    # 주어진 토픽에 대해 비동기적으로 일괄 처리를 수행한다.
    print(await chain.abatch(
        [{"topic": "YouTube"}, {"topic": "Instagram"}, {"topic": "Facebook"}]
    ))
asyncio.run(abatch_test())