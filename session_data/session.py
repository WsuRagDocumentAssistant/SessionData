from dataclasses import dataclass
from typing import Any


@dataclass
class Session:
    """세션 하나를 담는 객체. DB에서 온 값을 형태 그대로 담는다."""

    recent_conversations: Any  # 최근 5개 대화 (dict 리스트 등)
    current_topic: Any         # 현재 대화의 주제
    summary: Any               # 총 요약
