# 02에 나오는 코드들
# API KEY를 환경변수로 관리하기 위한 설정 파일
from dotenv import load_dotenv

# API KEY 정보로드
load_dotenv()
import openai

print(openai.__version__)
