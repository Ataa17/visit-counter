pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install & Test') {
            steps {
                sh 'python3 -m pip install --break-system-packages -r requirements-dev.txt'
                sh 'python3 -m pytest -q'
            }
        }

        stage('Build Docker image') {
            steps {
                sh 'docker build -t ataamars17/counter-app:${BUILD_NUMBER} -t ataamars17/counter-app:latest .'
            }
        }

        stage('Push to Docker Hub') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub-creds', usernameVariable: 'DOCKERHUB_USER', passwordVariable: 'DOCKERHUB_TOKEN')]) {
                    sh 'echo "$DOCKERHUB_TOKEN" | docker login -u "$DOCKERHUB_USER" --password-stdin'
                    sh 'docker push ataamars17/counter-app:${BUILD_NUMBER}'
                    sh 'docker push ataamars17/counter-app:latest'
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
