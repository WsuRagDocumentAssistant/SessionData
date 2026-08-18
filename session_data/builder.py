from .session import Session


def build_session(recent_conversations, current_topic, summary):
    """DB에서 꺼내온 값을 받아 Session 객체로 만들어 반환한다.

    값은 변환하지 않고 들어온 형태 그대로 담는다.
    """
    return Session(
        recent_conversations=recent_conversations,
        current_topic=current_topic,
        summary=summary,
    )
