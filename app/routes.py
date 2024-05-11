from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models import db, Post, Comment, IssueReport, ContactMessage, Rating

main = Blueprint('main', __name__)

@main.route('/posts', methods=['GET', 'POST'])
@jwt_required(optional=True)
def posts():
    if request.method == 'POST':
        user_id = get_jwt_identity()
        data = request.get_json()
        new_post = Post(title=data['title'], content=data['content'], author_id=user_id)
        db.session.add(new_post)
        db.session.commit()
        return jsonify({'message': 'Post created'}), 201

    posts = Post.query.order_by(Post.created_at.desc()).all()
    return jsonify([{'id': post.id, 'title': post.title, 'content': post.content, 'created_at': post.created_at} for post in posts]), 200

@main.route('/posts/<int:post_id>', methods=['GET', 'PUT', 'DELETE'])
@jwt_required()
def post_detail(post_id):
    post = Post.query.get_or_404(post_id)
    if request.method == 'GET':
        post.views += 1
        db.session.commit()
        return jsonify({'title': post.title, 'content': post.content, 'views': post.views}), 200

    user_id = get_jwt_identity()
    if post.author_id != user_id:
        return jsonify({'message': 'Unauthorized'}), 403

    if request.method == 'PUT':
        data = request.get_json()
        post.title = data.get('title', post.title)
        post.content = data.get('content', post.content)
        db.session.commit()
        return jsonify({'message': 'Post updated'}), 200

    db.session.delete(post)
    db.session.commit()
    return jsonify({'message': 'Post deleted'}), 200

@main.route('/posts/<int:post_id>/comments', methods=['POST'])
@jwt_required()
def add_comment(post_id):
    user_id = get_jwt_identity()
    data = request.get_json()
    content = data['content']
    new_comment = Comment(content=content, post_id=post_id, author_id=user_id)
    db.session.add(new_comment)
    db.session.commit()
    return jsonify({'message': 'Comment added'}), 201

@main.route('/posts/<int:post_id>/rate', methods=['POST'])
@jwt_required()
def rate_post(post_id):
    user_id = get_jwt_identity()
    data = request.get_json()
    score = data['score']
    if not (1 <= score <= 5):
        return jsonify({'message': 'Rating must be between 1 and 5'}), 400
    new_rating = Rating(score=score, post_id=post_id, user_id=user_id)
    db.session.add(new_rating)
    db.session.commit()
    return jsonify({'message': 'Rating added'}), 201

@main.route('/report_issue', methods=['POST'])
@jwt_required()
def report_issue():
    user_id = get_jwt_identity()
    data = request.get_json()
    new_issue = IssueReport(title=data['title'], description=data['description'], user_id=user_id)
    db.session.add(new_issue)
    db.session.commit()
    return jsonify({'message': 'Issue reported'}), 201

@main.route('/contact_author', methods=['POST'])
@jwt_required()
def contact_author():
    user_id = get_jwt_identity()
    data = request.get_json()
    new_message = ContactMessage(subject=data['subject'], message=data['message'], user_id=user_id)
    db.session.add(new_message)
    db.session.commit()
    return jsonify({'message': 'Message sent to author'}), 201
