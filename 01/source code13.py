import json

# 스키마를 출력하는 함수를 정의한다.
def print_schema(schema):
    # 스키마를 JSON 형식으로 출력한다.
    print(json.dumps(schema, indent=4))

# 입력 스키마를 정의한다.
input_schema = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "age": {"type": "integer", "minimum": 0},
    },
    "required": ["name", "age"],
}

# 스키마를 출력하는 함수를 호출한다.
print_schema(input_schema)