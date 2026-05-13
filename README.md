# 任务管理系统 - ELK实战项目

这是一个完整的任务管理系统，使用Kubernetes部署，集成了ELK日志收集和分析系统。

## 项目架构

```
├── 前端服务 (React + Nginx)
├── 后端服务 (Flask + Python)
├── 数据库 (PostgreSQL)
├── 缓存 (Redis)
└── ELK日志系统
    ├── Elasticsearch - 日志存储
    ├── Logstash - 日志处理
    └── Kibana - 日志可视化
```

## 功能特性

- ✅ 任务创建、编辑、删除
- ✅ 实时日志收集和分析
- ✅ Kubernetes容器化部署
- ✅ ELK日志系统集成
- ✅ 健康检查和监控
- ✅ 环境变量配置

## 技术栈

- **前端**: React, Tailwind CSS
- **后端**: Flask, Python
- **数据库**: PostgreSQL
- **缓存**: Redis
- **容器化**: Docker, Kubernetes
- **日志系统**: ELK (Elasticsearch, Logstash, Kibana)
- **反向代理**: Nginx

## 部署指南

### 前提条件

- Kubernetes集群
- kubectl命令行工具
- Docker镜像仓库（可选）

### 部署步骤

1. **创建命名空间**
```bash
kubectl apply -f configs/namespace.yaml
```

2. **部署数据库**
```bash
kubectl apply -f configs/postgres-deployment.yaml
```

3. **部署Redis**
```bash
kubectl apply -f configs/redis-deployment.yaml
```

4. **部署ELK日志系统**
```bash
kubectl apply -f configs/elasticsearch-deployment.yaml
kubectl apply -f configs/logstash-deployment.yaml
kubectl apply -f configs/filebeat-deployment.yaml
kubectl apply -f configs/kibana-deployment.yaml
```

5. **部署应用服务**
```bash
kubectl apply -f configs/backend-deployment.yaml
kubectl apply -f configs/frontend-deployment.yaml
```

6. **部署Ingress**
```bash
kubectl apply -f configs/ingress.yaml
```

### 验证部署

1. **检查Pod状态**
```bash
kubectl get pods -n task-management
```

2. **访问应用**
- 前端应用: http://task-management.local/
- Kibana: http://task-management.local/kibana

3. **查看日志**
- 在Kibana中查看收集的日志
- 使用`task-management-logs-*`索引模式

## 日志分析

### Kibana仪表板

1. 登录Kibana: http://task-management.local/kibana
2. 创建索引模式: `task-management-logs-*`
3. 查看日志数据

### 常见日志查询

- 按服务过滤: `service: flask-backend`
- 按时间范围查询
- 错误日志分析

## 开发指南

### 本地开发

1. **启动后端服务**
```bash
cd services/backend
python app.py
```

2. **启动前端服务**
```bash
cd services/frontend
python -m http.server 8080
```

3. **访问**
- 前端: http://localhost:8080
- 后端API: http://localhost:5000

### 构建Docker镜像

```bash
# 后端
docker build -t your-registry/backend:latest services/backend

# 前端
docker build -t your-registry/frontend:latest services/frontend
```

## 配置说明

### 环境变量

| 服务 | 变量 | 默认值 | 描述 |
|------|------|--------|------|
| 后端 | DB_HOST | postgres | 数据库主机 |
| 后端 | DB_NAME | taskdb | 数据库名称 |
| 后端 | DB_USER | postgres | 数据库用户 |
| 后端 | DB_PASSWORD | password | 数据库密码 |
| 后端 | REDIS_HOST | redis | Redis主机 |
| 前端 | REACT_APP_API_URL | http://backend:5000 | API地址 |

### 日志配置

- **Filebeat**: 收集Flask应用日志
- **Logstash**: 处理和转发日志到Elasticsearch
- **Kibana**: 可视化日志数据

## 监控和运维

### 健康检查

- 后端服务提供健康检查端点: `/health`
- Kubernetes自动进行健康检查

### 日志管理

- 日志存储在Elasticsearch中
- 使用Kibana进行可视化分析
- 日志保留策略可通过Elasticsearch配置

## 扩展建议

1. **添加Prometheus监控**
2. **集成Grafana仪表板**
3. **实现CI/CD流水线**
4. **添加认证和授权**
5. **实现数据备份策略**

## 贡献指南

1. Fork项目
2. 创建功能分支
3. 提交更改
4. 创建Pull Request

## 许可证

本项目采用MIT许可证。