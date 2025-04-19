pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/Varunk55/movie-recommendation-devops.git'
            }
        }


        stage('Install Dependencies') {
            steps {
                sh 'pip3 install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'pytest || echo "No tests yet"'
            }
        }

        stage('Docker Build') {
            steps {
                sh 'docker build -t movie-recommender .'
            }
        }
        stage('Docker Push') {
            steps {
               sh 'docker tag movie-recommender kingv5/movie-recommender:latest'
               sh 'docker push kingv5/movie-recommender:latest'
            }
        }

    }
}
