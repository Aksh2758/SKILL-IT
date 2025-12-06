# SKILL-IT Deployment Guide

## Table of Contents
1. [Local Development Setup](#local-development-setup)
2. [Docker Deployment](#docker-deployment)
3. [Heroku Deployment](#heroku-deployment)
4. [AWS Deployment](#aws-deployment)
5. [Environment Variables](#environment-variables)
6. [Database Setup](#database-setup)
7. [CI/CD Pipeline](#cicd-pipeline)

---

## Local Development Setup

### Prerequisites
- Python 3.8+
- Node.js 14+
- MongoDB (local or Atlas)
- Git

### Backend Setup

```bash
# Clone the repository
git clone https://github.com/Aksh2758/SKILL-IT.git
cd SKILL-IT

# Navigate to backend
cd backend

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Download spaCy language model
python -m spacy download en_core_web_sm

# Create .env file
cp ../.env.example .env
# Edit .env with your configuration

# Run the backend server
python run.py
```

Backend will be available at: `http://localhost:5001`

### Frontend Setup

```bash
# Navigate to frontend (from project root)
cd frontend

# Install dependencies
npm install

# Create .env file
echo "REACT_APP_API_URL=http://localhost:5001" > .env

# Start development server
npm start
```

Frontend will be available at: `http://localhost:3000`

---

## Docker Deployment

### Using Docker Compose (Recommended)

```bash
# From project root
docker-compose up -d

# View logs
docker-compose logs -f

# Stop containers
docker-compose down

# Rebuild containers
docker-compose up -d --build
```

Services will be available at:
- Frontend: `http://localhost:3000`
- Backend: `http://localhost:5001`
- MongoDB: `localhost:27017`

### Individual Docker Containers

**Backend:**
```bash
cd backend
docker build -t skillit-backend .
docker run -p 5001:5001 \
  -e MONGO_URI=mongodb://host.docker.internal:27017/skillit \
  -e SECRET_KEY=your-secret-key \
  skillit-backend
```

**Frontend:**
```bash
cd frontend
docker build -t skillit-frontend .
docker run -p 3000:3000 skillit-frontend
```

---

## Heroku Deployment

### Prerequisites
- Heroku account
- Heroku CLI installed

### Backend Deployment

```bash
# Login to Heroku
heroku login

# Create Heroku app
heroku create skillit-backend

# Add MongoDB addon
heroku addons:create mongolab:sandbox

# Set environment variables
heroku config:set SECRET_KEY=$(openssl rand -hex 32)
heroku config:set FLASK_ENV=production

# Deploy
git subtree push --prefix backend heroku main

# Or if using separate repo:
cd backend
git init
heroku git:remote -a skillit-backend
git add .
git commit -m "Deploy backend"
git push heroku main
```

### Frontend Deployment

```bash
# Create Heroku app for frontend
heroku create skillit-frontend

# Set buildpack
heroku buildpacks:set mars/create-react-app

# Set environment variables
heroku config:set REACT_APP_API_URL=https://skillit-backend.herokuapp.com

# Deploy
git subtree push --prefix frontend heroku main
```

### Using Heroku.yml (Alternative)

Create `heroku.yml` in project root:

```yaml
build:
  docker:
    web: backend/Dockerfile
run:
  web: python backend/run.py
```

Then deploy:
```bash
heroku stack:set container
git push heroku main
```

---

## AWS Deployment

### Using AWS Elastic Beanstalk

**Backend:**
```bash
# Install EB CLI
pip install awsebcli

# Initialize EB
cd backend
eb init -p python-3.10 skillit-backend

# Create environment
eb create skillit-backend-env

# Set environment variables
eb setenv SECRET_KEY=your-secret-key MONGO_URI=your-mongodb-uri

# Deploy
eb deploy

# Open application
eb open
```

**Frontend (S3 + CloudFront):**
```bash
cd frontend

# Build production bundle
npm run build

# Install AWS CLI
pip install awscli

# Create S3 bucket
aws s3 mb s3://skillit-frontend

# Enable static website hosting
aws s3 website s3://skillit-frontend --index-document index.html

# Upload build files
aws s3 sync build/ s3://skillit-frontend --acl public-read

# Create CloudFront distribution (optional, for CDN)
aws cloudfront create-distribution --origin-domain-name skillit-frontend.s3.amazonaws.com
```

### Using AWS ECS (Docker)

```bash
# Build and tag images
docker build -t skillit-backend:latest ./backend
docker build -t skillit-frontend:latest ./frontend

# Tag for ECR
docker tag skillit-backend:latest <account-id>.dkr.ecr.<region>.amazonaws.com/skillit-backend:latest
docker tag skillit-frontend:latest <account-id>.dkr.ecr.<region>.amazonaws.com/skillit-frontend:latest

# Push to ECR
aws ecr get-login-password --region <region> | docker login --username AWS --password-stdin <account-id>.dkr.ecr.<region>.amazonaws.com
docker push <account-id>.dkr.ecr.<region>.amazonaws.com/skillit-backend:latest
docker push <account-id>.dkr.ecr.<region>.amazonaws.com/skillit-frontend:latest

# Deploy to ECS (use AWS Console or CLI)
```

---

## Environment Variables

### Backend (.env)

```env
# Required
MONGO_URI=mongodb://localhost:27017/skillit
SECRET_KEY=your-super-secret-key-change-in-production

# Optional
FLASK_ENV=production
GITHUB_CLIENT_ID=your_github_client_id
GITHUB_CLIENT_SECRET=your_github_client_secret
LINKEDIN_CLIENT_ID=your_linkedin_client_id
LINKEDIN_CLIENT_SECRET=your_linkedin_client_secret
```

### Frontend (.env)

```env
REACT_APP_API_URL=http://localhost:5001
```

### Production Environment Variables

**Generate secure SECRET_KEY:**
```bash
python -c "import secrets; print(secrets.token_hex(32))"
```

**Set in Heroku:**
```bash
heroku config:set SECRET_KEY=$(python -c "import secrets; print(secrets.token_hex(32))")
```

---

## Database Setup

### Local MongoDB

```bash
# Install MongoDB
# macOS:
brew install mongodb-community

# Start MongoDB
brew services start mongodb-community

# Verify
mongosh
```

### MongoDB Atlas (Cloud)

1. Create account at https://www.mongodb.com/cloud/atlas
2. Create cluster
3. Create database user
4. Whitelist IP addresses (0.0.0.0/0 for development)
5. Get connection string
6. Update MONGO_URI in .env

Example connection string:
```
mongodb+srv://username:password@cluster0.xxxxx.mongodb.net/skillit?retryWrites=true&w=majority
```

### Database Initialization

The application will automatically create collections on first use. No manual initialization required.

---

## CI/CD Pipeline

### GitHub Actions

The project includes a GitHub Actions workflow (`.github/workflows/ci-cd.yml`) that:

1. **Runs on every push/PR to main/develop**
2. **Backend Tests**: Linting, unit tests
3. **Frontend Tests**: Linting, build verification
4. **Docker Build**: Verifies Docker images build successfully
5. **Security Scan**: Trivy vulnerability scanning
6. **Deploy to Staging**: Automatic deployment on main branch

### Setup Secrets

Add these secrets in GitHub repository settings:

```
HEROKU_API_KEY=your-heroku-api-key
HEROKU_EMAIL=your-email@example.com
```

### Manual Deployment Trigger

```bash
# Trigger deployment
git tag -a v1.0.0 -m "Release version 1.0.0"
git push origin v1.0.0
```

---

## Health Checks

### Backend Health Check

```bash
curl http://localhost:5001/health
```

Add this endpoint to `backend/app/__init__.py`:

```python
@app.route('/health')
def health():
    return jsonify({"status": "healthy", "service": "backend"}), 200
```

### Frontend Health Check

Access: `http://localhost:3000`

---

## Monitoring & Logging

### Heroku Logs

```bash
# View logs
heroku logs --tail -a skillit-backend

# View specific number of lines
heroku logs -n 200 -a skillit-backend
```

### Application Monitoring

Recommended tools:
- **Sentry** - Error tracking
- **New Relic** - Performance monitoring
- **Datadog** - Infrastructure monitoring

---

## Troubleshooting

### Common Issues

**1. MongoDB Connection Failed**
```bash
# Check MongoDB is running
mongosh

# Verify connection string
echo $MONGO_URI
```

**2. Port Already in Use**
```bash
# Kill process on port 5001
lsof -ti:5001 | xargs kill -9

# Kill process on port 3000
lsof -ti:3000 | xargs kill -9
```

**3. Docker Build Fails**
```bash
# Clear Docker cache
docker system prune -a

# Rebuild without cache
docker-compose build --no-cache
```

**4. spaCy Model Not Found**
```bash
# Download model
python -m spacy download en_core_web_sm

# Verify installation
python -c "import spacy; nlp = spacy.load('en_core_web_sm'); print('Success')"
```

---

## Performance Optimization

### Production Checklist

- [ ] Set `FLASK_ENV=production`
- [ ] Use strong `SECRET_KEY`
- [ ] Enable HTTPS/SSL
- [ ] Configure CORS properly
- [ ] Add rate limiting
- [ ] Enable caching (Redis)
- [ ] Optimize database indexes
- [ ] Minify frontend assets
- [ ] Enable gzip compression
- [ ] Set up CDN for static files
- [ ] Configure monitoring
- [ ] Set up automated backups

---

## Backup & Recovery

### Database Backup

```bash
# Backup MongoDB
mongodump --uri="mongodb://localhost:27017/skillit" --out=./backup

# Restore MongoDB
mongorestore --uri="mongodb://localhost:27017/skillit" ./backup/skillit
```

### Automated Backups (Heroku)

```bash
# Schedule daily backups
heroku pg:backups:schedule DATABASE_URL --at '02:00 America/Los_Angeles' -a skillit-backend

# Create manual backup
heroku pg:backups:capture -a skillit-backend

# Download backup
heroku pg:backups:download -a skillit-backend
```

---

## Support

For deployment issues:
- Check logs first
- Review environment variables
- Verify database connection
- Check GitHub Actions workflow status

Contact: akshu290110@gmail.com
