from flask import Blueprint, request, jsonify, current_app
from flask_login import login_required, current_user
from .models import Post, Comment, PostRating, PostView, DeviceToken, IssueReport, db

main = Blueprint('main', __name__)

@main.route('/posts', methods=['GET'])
def get_posts():
    sort_by = request.args.get('sort_by', 'created_at')
    order = request.args.get('order', 'desc')
    query = request.args.get('query', '')

    if sort_by not in ['title', 'created_at']:
        sort_by = 'created_at'
    if order not in ['asc', 'desc']:
        order = 'desc'

    posts_query = Post.query
    if query:
        posts_query = posts_query.filter(Post.title.contains(query))

    if order == 'asc':
        posts_query = posts_query.order_by(getattr(Post, sort_by).asc())
    else:
        posts_query = posts_query.order_by(getattr(Post, sort_by).desc())

    posts = posts_query.all()
    posts_data = [{'id': post.id, 'title': post.title, 'content': post.content, 'author_id': post.author_id} for post in posts]
    return jsonify(posts_data), 200

@main.route('/posts/<int:post_id>', methods=['GET'])
def get_post(post_id):
    post = Post.query.get_or_404(post_id)
    post_view = PostView.query.filter_by(post_id=post_id).first()
    if post_view:
        post_view.view_count += 1
    else:
        db.session.add(PostView(post_id=post_id, view_count=1))
    db.session.commit()
    return jsonify({'title': post.title, 'content': post.content, 'view_count': post_view.view_count if post_view else 1}), 200

@main.route('/posts/<int:post_id>/comment', methods=['POST'])
@login_required
def add_comment(post_id):
    data = request.get_json()
    content = data.get('content')
    if not content:
        return jsonify({'message': 'Content is required'}), 400

    new_comment = Comment(content=content, post_id=post_id, author_id=current_user.id)
    db.session.add(new_comment)
    db.session.commit()

    return jsonify({'message': 'Comment added successfully'}), 201

@main.route('/posts/<int:post_id>/rate', methods=['POST'])
@login_required
def rate_post(post_id):
    data = request.get_json()
    rating = data.get('rating')
    if not rating or rating < 1 or rating > 5:
        return jsonify({'message': 'Rating must be between 1 and 5'}), 400

    new_rating = PostRating(rating=rating, post_id=post_id, user_id=current_user.id)
    db.session.add(new_rating)
    db.session.commit()

    return jsonify({'message': 'Post rated successfully'}), 200

@main.route('/report_issue', methods=['POST'])
@login_required
def report_issue():
    data = request.get_json()
    title = data.get('title')
    description = data.get('description')
    if not title or not description:
        return jsonify({'message': 'Title and description are required'}), 400

    new_issue = IssueReport(title=title, description=description, user_id=current_user.id)
    db.session.add(new_issue)
    db.session.commit()

    return jsonify({'message': 'Issue reported successfully'}), 201

@main.route('/save_device_token', methods=['POST'])
@login_required
def save_device_token():
    data = request.get_json()
    token = data.get('token')
    if not token:
        return jsonify({'message': 'Token is required'}), 400

    new_token = DeviceToken(token=token, user_id=current_user.id)
    db.session.add(new_token)
    db.session.commit()

    return jsonify({'message': 'Device token saved successfully'}), 200
