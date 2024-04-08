from langchain.prompts import PromptTemplate
# API KEY를 환경변수로 관리하기 위한 설정 파일
from dotenv import load_dotenv
load_dotenv()
# 오픈ai 사용가능한 랭체인 임포트
from langchain_openai import ChatOpenAI
from langchain.chains import LLMChain

# 질문 템플릿 형식 정의
template = "{country}의 수도는 뭐야?"

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

# 입력값
input_list = [{"country":"호주"}, {"country":"중국"},{"country":"네덜란드"}]

# input_list 에 대한 결과 반환
generated_result = llm_chain.generate(input_list)
print(generated_result)
# 토큰 사용량 출력
print(generated_result.llm_output)