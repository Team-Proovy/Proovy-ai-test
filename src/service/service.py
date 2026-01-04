"""
FastAPI 서비스 엔트리포인트.

- lifespan 컨텍스트에서 LangGraph용 체크포인터/스토어/에이전트들을 초기화한다.
- /info, /invoke, /stream, /feedback, /history, /health 등의 HTTP 엔드포인트를 정의한다.
- LangGraph 에이전트 실행 결과를 이 서비스 전용 ChatMessage 스키마와
  SSE(text/event-stream) 형식으로 변환해 클라이언트에 반환한다.
"""