pipeline {
    agent any
    environment {
        DOCKER_IMAGE = "your-dockerhub-username/demo-python-fastapi:${env.BUILD_NUMBER}"
        DOCKER_CREDENTIALS_ID = "docker-hub-credentials" // Set this in Jenkins credentials
    }
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Install Dependencies') {
            steps {
                sh 'pip install uv'
                sh 'uv pip install --system -r pyproject.toml'
            }
        }
        stage('Run Tests') {
            steps {
                sh 'uv run pytest tests/test_main.py'
            }
        }
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $DOCKER_IMAGE .'
            }
        }
        stage('Push Docker Image') {
            steps {
                withCredentials([usernamePassword(credentialsId: env.DOCKER_CREDENTIALS_ID, usernameVariable: 'DOCKER_USERNAME', passwordVariable: 'DOCKER_PASSWORD')]) {
                    sh 'echo $DOCKER_PASSWORD | docker login -u $DOCKER_USERNAME --password-stdin'
                    sh 'docker push $DOCKER_IMAGE'
                }
            }
        }
    }
    post {
        always {
            sh 'docker logout'
        }
    }
}