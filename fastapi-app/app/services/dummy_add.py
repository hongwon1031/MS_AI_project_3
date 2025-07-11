'''
더미 데이터를 추가하는 함수

'''

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from sqlalchemy.ext.asyncio import AsyncSession
from db.models.family import Family
from db.models.user import User
from db.models.photo import Photo
from db.models.conversation import Conversation
from db.models.mention import Mention
from db.models.anomalies_report import AnomaliesReport

import asyncio
from datetime import datetime
import uuid

def get_uuid():
    return uuid.uuid4()

async def add_dummy_family(session: AsyncSession) -> uuid.UUID:
    family_id = get_uuid()
    family = Family(
        id=family_id,
        family_code="FAMILY001",
        created_at=datetime.utcnow()
    )
    session.add(family)
    await session.commit()
    return family_id

async def add_dummy_user(session: AsyncSession, family_id: uuid.UUID) -> uuid.UUID:
    user_id = get_uuid()
    user = User(
        id=user_id,
        kakao_id="kakao123",
        username="홍길동",
        gender="male",
        birthday=datetime(1950, 1, 1),
        profile_img="http://example.com/profile.jpg",
        family_id=family_id,
        family_role="할아버지",
        created_at=datetime.utcnow()
    )
    
    session.add(user)
    await session.commit()
    return user_id

async def add_dummy_photo(session: AsyncSession, family_id: uuid.UUID) -> uuid.UUID:
    photo_id = get_uuid()
    photo = Photo(
        id=photo_id,
        photo_name="가족사진",
        photo_url="http://example.com/photo.jpg",
        story_year=datetime(1985, 5, 1),
        story_season="spring",
        story_nudge={"keyword": "소풍"},
        summary_text="봄에 가족들과 소풍을 간 날",
        summary_voice="http://example.com/voice.mp3",
        family_id=family_id,
        uploaded_at=datetime.utcnow()
    )
    session.add(photo)
    await session.commit()
    return photo_id

async def add_dummy_conversation(session: AsyncSession, photo_id: uuid.UUID) -> uuid.UUID:
    conv_id = get_uuid()
    conv = Conversation(
        id=conv_id,
        photo_id=photo_id,
        created_at=datetime.utcnow()
    )
    session.add(conv)
    await session.commit()
    return conv_id

async def add_dummy_mention(session: AsyncSession, conv_id: uuid.UUID) -> uuid.UUID:
    mention_id = get_uuid()
    mention = Mention(
        id=mention_id,
        conv_id=conv_id,
        question_answer={
            "q_text": "이 사진은 언제 찍으셨어요?",
            "a_text": "1985년 봄이었던 것 같아",
            "q_voice": "http://example.com/q.mp3",
            "a_voice": "http://example.com/a.mp3"
        },
        recorded_at=datetime.utcnow()
    )
    session.add(mention)
    await session.commit()
    return mention_id

async def add_dummy_anomaly(session: AsyncSession, conv_id: uuid.UUID):
    report = AnomaliesReport(
        id=get_uuid(),
        conv_id=conv_id,
        event_report="대화 흐름이 갑작스럽게 멈춤",
        event_interval="00:02~00:04"
    )
    session.add(report)
    await session.commit()

from db.database import async_session

async def main():
    async with async_session() as session:
        family_id = await add_dummy_family(session)
        await add_dummy_user(session, family_id)
        photo_id = await add_dummy_photo(session, family_id)
        conv_id = await add_dummy_conversation(session, photo_id)
        await add_dummy_mention(session, conv_id)
        await add_dummy_anomaly(session, conv_id)


if __name__ == "__main__":
    asyncio.run(main())
