from flask import Flask, request, jsonify
import redis
import psycopg2
import logging
from datetime import datetime
import os

app = Flask(__name__)

# 配置日志
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# 数据库连接
def get_db_connection():
    conn = psycopg2.connect(
        host=os.getenv('DB_HOST', 'postgres'),
        database=os.getenv('DB_NAME', 'taskdb'),
        user=os.getenv('DB_USER', 'postgres'),
        password=os.getenv('DB_PASSWORD', 'password')
    )
    return conn

# Redis连接
redis_client = redis.Redis(host=os.getenv('REDIS_HOST', 'redis'), port=6379, db=0)

@app.route('/tasks', methods=['POST'])
def create_task():
    data = request.json
    title = data.get('title')
    description = data.get('description', '')
    
    if not title:
        return jsonify({'error': 'Title is required'}), 400
    
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO tasks (title, description, created_at) VALUES (%s, %s, %s) RETURNING id",
        (title, description, datetime.now())
    )
    task_id = cur.fetchone()[0]
    conn.commit()
    cur.close()
    conn.close()
    
    # 记录日志
    logger.info(f"Task created: {task_id}, title: {title}")
    
    return jsonify({'id': task_id, 'title': title, 'description': description}), 201

@app.route('/tasks', methods=['GET'])
def get_tasks():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, title, description, created_at FROM tasks ORDER BY created_at DESC")
    tasks = cur.fetchall()
    cur.close()
    conn.close()
    
    return jsonify([{
        'id': task[0],
        'title': task[1],
        'description': task[2],
        'created_at': task[3].isoformat()
    } for task in tasks])

@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, title, description, created_at FROM tasks WHERE id = %s", (task_id,))
    task = cur.fetchone()
    cur.close()
    conn.close()
    
    if task:
        return jsonify({
            'id': task[0],
            'title': task[1],
            'description': task[2],
            'created_at': task[3].isoformat()
        })
    return jsonify({'error': 'Task not found'}), 404

@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    data = request.json
    title = data.get('title')
    description = data.get('description')
    
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(
        "UPDATE tasks SET title = %s, description = %s WHERE id = %s",
        (title, description, task_id)
    )
    conn.commit()
    cur.close()
    conn.close()
    
    logger.info(f"Task updated: {task_id}, title: {title}")
    
    return jsonify({'message': 'Task updated successfully'})

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM tasks WHERE id = %s", (task_id,))
    conn.commit()
    cur.close()
    conn.close()
    
    logger.info(f"Task deleted: {task_id}")
    
    return jsonify({'message': 'Task deleted successfully'})

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'healthy', 'timestamp': datetime.now().isoformat()})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)