# Deployment Guide

This guide covers different deployment options for the Censys Data Summarizer application.

## 🚀 Quick Start (Local Development)

```bash
# 1. Clone repository
git clone <your-repo-url>
cd Proj_Deep

# 2. Install dependencies
pip install -r requirements.txt

# 3. Update API key in app.py
# Replace "your-api-key-here" with your Perplexity API key

# 4. Run application
python app.py

# 5. Open browser
# Navigate to http://127.0.0.1:5000
```

## 🐳 Docker Deployment

### Create Dockerfile
```dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python", "app.py"]
```

### Build and Run
```bash
# Build image
docker build -t censys-summarizer .

# Run container
docker run -p 5000:5000 -e PERPLEXITY_API_KEY=your-key-here censys-summarizer
```

## ☁️ Cloud Deployment

### Heroku
1. Create `Procfile`:
```
web: python app.py
```

2. Deploy:
```bash
heroku create your-app-name
heroku config:set PERPLEXITY_API_KEY=your-key-here
git push heroku main
```

### AWS EC2
1. Launch EC2 instance (Ubuntu 20.04)
2. Install dependencies:
```bash
sudo apt update
sudo apt install python3-pip nginx
pip3 install -r requirements.txt
```

3. Configure Nginx:
```nginx
server {
    listen 80;
    server_name your-domain.com;
    
    location / {
        proxy_pass http://127.0.0.1:5000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```

4. Run with Gunicorn:
```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

### Google Cloud Platform
1. Create Cloud Run service
2. Deploy with Cloud Build:
```yaml
# cloudbuild.yaml
steps:
  - name: 'gcr.io/cloud-builders/docker'
    args: ['build', '-t', 'gcr.io/$PROJECT_ID/censys-summarizer', '.']
  - name: 'gcr.io/cloud-builders/docker'
    args: ['push', 'gcr.io/$PROJECT_ID/censys-summarizer']
  - name: 'gcr.io/cloud-builders/gcloud'
    args: ['run', 'deploy', 'censys-summarizer', '--image', 'gcr.io/$PROJECT_ID/censys-summarizer', '--platform', 'managed', '--region', 'us-central1']
```

## 🔧 Environment Configuration

### Production Environment Variables
```bash
# .env file
PERPLEXITY_API_KEY=your-production-api-key
FLASK_ENV=production
FLASK_DEBUG=False
PORT=5000
```

### Security Considerations
- Store API keys in environment variables
- Use HTTPS in production
- Implement rate limiting
- Add input validation and sanitization
- Use a reverse proxy (Nginx)

## 📊 Monitoring and Logging

### Application Logs
```python
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('app.log'),
        logging.StreamHandler()
    ]
)
```

### Health Check Endpoint
```python
@app.route('/health')
def health_check():
    return jsonify({"status": "healthy", "timestamp": datetime.now().isoformat()})
```

## 🔄 CI/CD Pipeline

### GitHub Actions
```yaml
# .github/workflows/deploy.yml
name: Deploy to Production

on:
  push:
    branches: [main]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Deploy to Heroku
        uses: akhileshns/heroku-deploy@v3.12.12
        with:
          heroku_api_key: ${{secrets.HEROKU_API_KEY}}
          heroku_app_name: "your-app-name"
          heroku_email: "your-email@example.com"
```

## 🚨 Troubleshooting

### Common Issues

1. **API Key Not Working**
   - Verify key is correct
   - Check API quota/limits
   - Ensure key has proper permissions

2. **Port Already in Use**
   ```bash
   # Find process using port 5000
   lsof -i :5000
   # Kill process
   kill -9 <PID>
   ```

3. **Module Not Found**
   ```bash
   # Reinstall dependencies
   pip install -r requirements.txt --force-reinstall
   ```

4. **CORS Issues**
   - Ensure Flask-CORS is properly configured
   - Check browser console for errors

### Performance Optimization

1. **Enable Caching**
   ```python
   from flask_caching import Cache
   cache = Cache(app, config={'CACHE_TYPE': 'simple'})
   ```

2. **Database Integration**
   ```python
   from flask_sqlalchemy import SQLAlchemy
   db = SQLAlchemy(app)
   ```

3. **Async Processing**
   ```python
   import asyncio
   import aiohttp
   ```

## 📈 Scaling Considerations

- Use load balancers for multiple instances
- Implement database for session management
- Add Redis for caching
- Use message queues for background processing
- Monitor API usage and costs
- Implement proper error handling and retry logic


