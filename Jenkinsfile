pipeline {
    //agent any
    agent {
        docker {
            image 'python:3.13' // Updated to Python 3.13
            args '-v /var/run/docker.sock:/var/run/docker.sock --user root'
        }
    }

    environment {
        IMAGE_NAME = 'python-fastapi'
        IMAGE_TAG = "v${new Date().format('yyyy-MM-dd')}"
        DOCKER_IMAGE = "qrsln/${IMAGE_NAME}"
        DOCKER_CREDENTIALS_ID = 'docker-hub-credentials'
    }

    stages {
        stage('Checkout') {
            steps {
                // Ensure clean workspace before checkout
                cleanWs()
                checkout scm
            }
        }

        stage('Setup and Test') {
            parallel {
                stage('Install Dependencies') {
                    steps {
                        script {
                            try {
                                sh '''
                                    pip install --user uv
                                    apt-get update && apt-get install -y docker.io
                                    uv sync --frozen
                                '''
                            } catch (Exception e) {
                                error "Failed to install dependencies: ${e.message}"
                            }
                        }
                    }
                }

                stage('Run Tests') {
                    steps {
                        script {
                            try {
                                sh 'uv run pytest tests --junitxml=test-results.xml'
                            } catch (Exception e) {
                                error "Tests failed: ${e.message}"
                            }
                        }
                    }
                }
            }
        }

        stage('Build Docker Images') {
            steps {
                script {
                    try {
                        // Build both tagged and latest images
                        sh """
                            docker build \
                                --build-arg APP_NAME=${IMAGE_NAME} \
                                --cache-from=${DOCKER_IMAGE}:${IMAGE_TAG} \
                                -t ${DOCKER_IMAGE}:${IMAGE_TAG} \
                                -t ${DOCKER_IMAGE}:latest .
                        """
                    } catch (Exception e) {
                        error "Docker build failed: ${e.message}"
                    }
                }
            }
        }

        stage('Push Docker Images') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: env.DOCKER_CREDENTIALS_ID,
                    usernameVariable: 'DOCKER_USERNAME',
                    passwordVariable: 'DOCKER_PASSWORD'
                )]) {
                    script {
                        try {
                            sh '''
                                echo $DOCKER_PASSWORD | docker login -u $DOCKER_USERNAME --password-stdin
                                docker push ${DOCKER_IMAGE}:${IMAGE_TAG}
                                docker push ${DOCKER_IMAGE}:latest
                            '''
                        } catch (Exception e) {
                            error "Docker push failed: ${e.message}"
                        }
                    }
                }
            }
        }

        stage('Clean Up') {
            steps {
                // Clean up Docker images to save space
                sh """
                    docker rmi ${DOCKER_IMAGE}:${IMAGE_TAG} || true
                    docker rmi ${DOCKER_IMAGE}:latest || true
                """
            }
        }
    }

    post {
        always {
            // Archive test results
            junit allowEmptyResults: true, testResults: 'test-results.xml'

            // Clean up workspace and Docker
            cleanWs()
            sh 'docker logout || true'
        }
        success {
            echo "Build and deployment of ${DOCKER_IMAGE}:${IMAGE_TAG} and ${DOCKER_IMAGE}:latest completed successfully!"
        }
        failure {
            echo "Pipeline failed! Please check the logs for details."
        }
    }
}
