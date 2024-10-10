import pytest
from models import Student
from db import get_session, init_db


@pytest.fixture(scope='module', autouse=True)
def setup():
    init_db()


@pytest.fixture
def db_session():
    session = next(get_session())
    yield session
    session.close()


def test_add_student(db_session):
    new_student = Student(name="Test Student")
    db_session.add(new_student)
    db_session.commit()

    student = db_session.query(Student).filter_by(name="Test Student").first()
    assert student is not None


def test_update_student(db_session):
    student = db_session.query(Student).filter_by(name="Test Student").first()
    student.name = "Updated Student"
    db_session.commit()

    updated_student = db_session.query(
        Student).filter_by(name="Updated Student").first()
    assert updated_student is not None


def test_delete_student(db_session):
    student = db_session.query(Student).filter_by(
        name="Updated Student").first()
    db_session.delete(student)
    db_session.commit()

    deleted_student = db_session.query(
        Student).filter_by(name="Updated Student").first()
    assert deleted_student is None
