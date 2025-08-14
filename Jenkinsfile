pipeline {
    agent any

    environment {
        APP_NAME = "demo-python-fastapi"
        DOCKER_IMAGE = "your-dockerhub-username/${APP_NAME}:${env.BUILD_NUMBER}"
        DOCKER_CREDENTIALS_ID = "docker-hub-credentials" // Jenkins credential ID
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install uv & Dependencies') {
            steps {
                sh 'pip install uv'
                // Install dev dependencies for testing
                sh 'uv sync --frozen'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'uv run pytest tests'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh '''
                    docker build \
                        --build-arg APP_NAME=${APP_NAME} \
                        --cache-from=${DOCKER_IMAGE} \
                        -t ${DOCKER_IMAGE} .
                '''
            }
        }

        stage('Push Docker Image') {
            steps {
                withCredentials([
                    usernamePassword(
                        credentialsId: env.DOCKER_CREDENTIALS_ID,
                        usernameVariable: 'DOCKER_USERNAME',
                        passwordVariable: 'DOCKER_PASSWORD'
                    )
                ]) {
                    sh 'echo $DOCKER_PASSWORD | docker login -u $DOCKER_USERNAME --password-stdin'
                    sh 'docker push ${DOCKER_IMAGE}'
                }
            }
        }
    }

    post {
        always {
            sh 'docker logout || true'
        }
    }
}
