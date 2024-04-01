from dotenv import load_dotenv
load_dotenv() # .env 파일에서 키들을 로드

import os
print(f"[API KEY]\n{os.environ['OPENAI_API_KEY']}") # OpenAI키에 접근해서 정삭적으로 로드되는지 확인
# 실행 후 OpenAI API키가 정상적으로 출력되어야 한다.