#!/bin/bash

echo "=== 任务管理系统 - ELK实战项目部署脚本 ==="

# 检查kubectl是否安装
if ! command -v kubectl &> /dev/null; then
    echo "错误: kubectl未安装"
    exit 1
fi

# 创建命名空间
echo "1. 创建命名空间..."
kubectl apply -f configs/namespace.yaml

# 部署数据库
echo "2. 部署PostgreSQL数据库..."
kubectl apply -f configs/postgres-deployment.yaml

# 部署Redis
echo "3. 部署Redis缓存..."
kubectl apply -f configs/redis-deployment.yaml

# 部署ELK日志系统
echo "4. 部署ELK日志系统..."
kubectl apply -f configs/elasticsearch-deployment.yaml
kubectl apply -f configs/logstash-deployment.yaml
kubectl apply -f configs/filebeat-deployment.yaml
kubectl apply -f configs/kibana-deployment.yaml

# 部署应用服务
echo "5. 部署后端服务..."
kubectl apply -f configs/backend-deployment.yaml

echo "6. 部署前端服务..."
kubectl apply -f configs/frontend-deployment.yaml

# 部署Ingress
echo "7. 部署Ingress..."
kubectl apply -f configs/ingress.yaml

echo "=== 部署完成！ ==="
echo ""
echo "请等待所有Pod启动完成..."
echo ""

# 检查Pod状态
echo "检查Pod状态:"
kubectl get pods -n task-management

echo ""
echo "访问地址:"
echo "前端应用: http://task-management.local/"
echo "Kibana: http://task-management.local/kibana"
echo ""
echo "注意: 请确保在hosts文件中添加 task-management.local 指向Kubernetes集群的Ingress地址"