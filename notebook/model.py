from datetime import datetime
from sqlalchemy.exc import IntegrityError

from notebook import db


class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), unique=True, nullable=False)
    body = db.Column(db.Text, unique=False, nullable=False)
    time = db.Column(db.DateTime, default=datetime.now)
    comments = db.relationship('Comment', backref='parent_note', lazy=True)

    def __repr__(self):
        return f'Note {self.id} ({self.title}): {self.body}'
    
    @classmethod
    def add(cls, title, body):
        try:
            note = cls(title=title, body=body)
            db.session.add(note)
            db.session.commit()
            return str(note)
        except IntegrityError as e:
            db.session.rollback()
            return e
        
    @classmethod
    def get_all(cls):
        return cls.query.all()
    
    @classmethod
    def get(cls, note_id):
        return cls.query.get(note_id)
    
    @classmethod
    def search(cls, term):
        return cls.query.join(Comment, Comment.parent_note_id == cls.id).filter(
            (cls.title.ilike(f'%{term}%')) |
            (cls.body.ilike(f'%{term}%')) |
            (Comment.body.ilike(f'%{term}%'))
        ).distinct()

    def delete(self):
        try:
            for comment in self.comments:
                db.session.delete(comment)
            db.session.delete(self)
            db.session.commit()
        except IntegrityError as e:
            db.session.rollback()
            return e
        

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.Text, nullable=False)
    time = db.Column(db.DateTime, default=datetime.now)
    parent_note_id = db.Column(db.Integer, db.ForeignKey('note.id'), nullable=False)

    def __repr__(self):
        return f'Comment {self.id} under note {self.parent_note_id}: {self.body}'
    
    @classmethod
    def add(cls, note_id, comment):
        try:
            comment = cls(body=comment, parent_note_id=note_id)
            db.session.add(comment)
            db.session.commit()
            return str(comment)
        except IntegrityError as e:
            db.session.rollback()
            return e
        
    @classmethod
    def get(cls, note_id):
        return cls.query.filter_by(parent_note_id=note_id).all()