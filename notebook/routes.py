from flask import render_template, request, redirect

from notebook import app
from notebook.model import Note, Comment


@app.route('/')
def index():
    search_term = request.args.get('search', '')
    if search_term:
        notes = Note.search(search_term)
    else:
        notes = Note.get_all()
    return render_template('index.html', notes=notes, search_term=search_term)

@app.route('/note/<int:note_id>')
def view_note(note_id):
    note = Note.get(note_id)
    return render_template('note.html', note=note)

@app.route('/add', methods=['POST'])
def add_note():
    title = request.form['title']
    body = request.form['body']
    if title and body:
        Note.add(title, body)
    return redirect('/')

@app.route('/delete/<int:note_id>', methods=['POST'])
def delete_note(note_id):
    note = Note.get(note_id)
    note.delete()
    return redirect('/')

@app.route('/comment/<int:note_id>', methods=['POST'])
def add_comment(note_id):
    comment = request.form['comment']
    if comment:
        Comment.add(note_id, comment)
    return redirect(f'/note/{note_id}')