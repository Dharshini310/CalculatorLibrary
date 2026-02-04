pipeline {
    agent any

    stages {

        stage('Get Code') {
            steps {
                git 'https://github.com/Dharshini310/CalculatorLibrary'
            }
        }

        stage('Install Python Tools') {
            steps {
                sh 'pip install pytest'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'pytest'
            }
        }
    }
}
