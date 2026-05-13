-- 创建数据库和用户
CREATE USER postgres WITH PASSWORD 'password';
CREATE DATABASE taskdb OWNER postgres;

-- 连接到taskdb数据库
\c taskdb;

-- 创建tasks表
CREATE TABLE tasks (
    id SERIAL PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 创建索引
CREATE INDEX idx_tasks_created_at ON tasks(created_at);

-- 插入示例数据
INSERT INTO tasks (title, description) VALUES 
('学习Kubernetes', '了解K8s的基本概念和架构'),
('配置ELK', '设置Elasticsearch, Logstash, Kibana'),
('部署微服务', '将应用部署到Kubernetes集群'),
('监控应用', '使用Prometheus和Grafana监控应用性能');