# 使用国内Nginx镜像作为基础
FROM registry.aliyuncs.com/library/nginx:alpine

# 复制前端文件到Nginx的HTML目录
COPY public/ /usr/share/nginx/html/

# 暴露端口
EXPOSE 80

# 启动Nginx
CMD ["nginx", "-g", "daemon off;"]