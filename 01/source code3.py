from langchain.prompts import PromptTemplate

# 질문 템플릿 형식 정의
template = "{country}의 수도는 뭐야?"

# 템플릿 완성
prompt = PromptTemplate.from_template(template=template)
print(prompt)