# API KEY를 환경변수로 관리하기 위한 설정 파일
from dotenv import load_dotenv

# API KEY 정보로드
load_dotenv()

from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate

import asyncio

from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

model = ChatOpenAI()

template = """Answer the question based only on the following context:
{context}

Question: {question}
"""
prompt = ChatPromptTemplate.from_template(template)

vectorstore = FAISS.from_texts(
    ["테디가 살고 있는 곳은 대한민국 입니다."], embedding=OpenAIEmbeddings()
)
retriever = vectorstore.as_retriever()

retrieval_chain = (
    {
        "context": retriever.with_config(run_name="Docs"),
        "question": RunnablePassthrough(),
    }
    | prompt
    | model
    | StrOutputParser()
)

async def astream_log_test():
    async for chunk in retrieval_chain.astream_log(
        "테디가 살고 있는 곳은 어디인가요?", include_names=["Docs"]
    ):
        print("-" * 40)
        print(chunk)
#asyncio.run(astream_log_test())

async def astream_log_test2():
    async for chunk in retrieval_chain.astream_log(
        "테디가 살고 있는 곳은 어딘가요?", include_names=["Docs"], diff=False
    ):
        print("-" * 70)
        print(chunk)
asyncio.run(astream_log_test2())