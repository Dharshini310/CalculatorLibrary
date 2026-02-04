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
                bat 'pip install pytest'
            }
        }

        stage('Run Tests') {
            steps {
                bat 'pytest'
            }
        }
    }
}
